import sublime
import sublime_plugin
import re
import platform


class SyntaxMgrCriteria():
    def __init__(self, S):
        self.S = S

    def apply(self, view):
        settings = self.S.get("settings", [])
        for key, value in settings.items():
            view.settings().set(key, value)

    def match_scopes(self, view):
        scopes = self.S.get("scopes", [])
        scopes = [scopes] if isinstance(scopes, str) else scopes
        scopes_excluded = self.S.get("scopes_excluded", [])
        scopes_excluded = [scopes_excluded] if isinstance(scopes_excluded, str) else scopes_excluded

        return (not scopes or any([view.score_selector(0, s) > 0 for s in scopes])) \
            and all([view.score_selector(0, s) == 0 for s in scopes_excluded])

    def match_extensions(self, view):
        extensions = self.S.get("extensions", [])
        extensions = [extensions] if isinstance(extensions, str) else extensions

        if not extensions:
            return True

        fname = view.file_name()
        extensions = ["." + e for e in extensions]
        return fname and fname.lower().endswith(tuple(extensions))

    def match_platform(self, view):
        platforms = self.S.get("platforms", [])
        platforms = [platforms] if isinstance(platforms, str) else platforms

        if not platforms:
            return True

        return sublime.platform() in [p.lower() for p in platforms]

    def match_firstline(self, view):
        firstlinepat = self.S.get("first_line_match", self.S.get("firstline", ""))
        firstlinepat = [firstlinepat] if isinstance(firstlinepat, str) else firstlinepat

        if not firstlinepat:
            return True

        for pat in firstlinepat:
            first_line = view.substr(view.line(view.text_point(0, 0)))
            if re.match(pat, first_line):
                return True

        return False

    def match_hostname(self, view):
        hostnames = self.S.get("hostnames", [])
        hostnames = [hostnames] if isinstance(hostnames, str) else hostnames

        if not hostnames:
            return True

        return platform.node() in hostnames

    def match(self, view):
        return self.match_scopes(view) and self.match_extensions(view) and \
            self.match_platform(view) and self.match_firstline(view) and self.match_hostname(view)


class SyntaxMgrListener(sublime_plugin.EventListener):

    def load_syntax_mgr(self, view):
        if view.settings().get('is_widget'):
            return

        if view.size() == 0 and not view.file_name():
            return

        if not view.settings().has("syntax_mgr_loaded"):
            view.settings().set("syntax_mgr_loaded", True)
            view.run_command("syntax_mgr_reload")

    def on_new(self, view):
        # need a small delay here to give he view a chance to prepare
        # itself
        sublime.set_timeout(lambda: self.load_syntax_mgr(view), 0)

    def on_load(self, view):
        self.load_syntax_mgr(view)

    def on_activated(self, view):
        self.load_syntax_mgr(view)


class SyntaxMgrReload(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        settings = sublime.load_settings('SyntaxMgr.sublime-settings')
        for s in settings.get("syntaxmgr_settings", []):
            criteria = SyntaxMgrCriteria(s)
            if criteria.match(view):
                criteria.apply(view)
