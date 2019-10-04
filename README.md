# Syntax Manager for Sublime Text 2/3

It helps in applying settings to given syntaxes and extensions.

I don't understand why Sublime Text makes it so difficult to apply the same setting across several different syntaxes.
For example, if someone want to enable `auto_match_enabled` for `python` and `c`, they has to create two files:
- `Packages/User/Python.sublime-settings`
- `Packages/User/C.sublime-settings`

Then, in each of the files, add:

        "auto_match_enabled": true


This plugin makes it easier by considering following setting in Syntax Manger:


        "syntaxmgr_settings": [
            {
                "scopes": ["source.c", "source.python"],
                "settings": {
                    "auto_match_enabled" : true
                }
            }
        ]


## Installation

### By Package Control

1. Download & Install **`Sublime Text 3`** (https://www.sublimetext.com/3)
1. Go to the menu **`Tools -> Install Package Control`**, then,
   wait few seconds until the installation finishes up
1. Now,
   Go to the menu **`Preferences -> Package Control`**
1. Type **`Add Channel`** on the opened quick panel and press <kbd>Enter</kbd>
1. Then,
   input the following address and press <kbd>Enter</kbd>
   ```
   https://raw.githubusercontent.com/evandrocoan/StudioChannel/master/channel.json
   ```
1. Go to the menu **`Tools -> Command Palette...
   (Ctrl+Shift+P)`**
1. Type **`Preferences:
   Package Control Settings – User`** on the opened quick panel and press <kbd>Enter</kbd>
1. Then,
   find the following setting on your **`Package Control.sublime-settings`** file:
   ```js
       "channels":
       [
           "https://packagecontrol.io/channel_v3.json",
           "https://raw.githubusercontent.com/evandrocoan/StudioChannel/master/channel.json",
       ],
   ```
1. And,
   change it to the following, i.e.,
   put the **`https://raw.githubusercontent...`** line as first:
   ```js
       "channels":
       [
           "https://raw.githubusercontent.com/evandrocoan/StudioChannel/master/channel.json",
           "https://packagecontrol.io/channel_v3.json",
       ],
   ```
   * The **`https://raw.githubusercontent...`** line must to be added before the **`https://packagecontrol.io...`** one, otherwise,
     you will not install this forked version of the package,
     but the original available on the Package Control default channel **`https://packagecontrol.io...`**
1. Now,
   go to the menu **`Preferences -> Package Control`**
1. Type **`Install Package`** on the opened quick panel and press <kbd>Enter</kbd>
1. Then,
search for **`SyntaxManager`** and press <kbd>Enter</kbd>

See also:
1. [ITE - Integrated Toolset Environment](https://github.com/evandrocoan/ITE)
1. [Package control docs](https://packagecontrol.io/docs/usage) for details.


## Usage

Open `Preference` -> `Syntax Manager`. Below is a sample of what you can specify in the settings file.
For each item, you need to provide at least one of the filters

- `scopes`
- `scopes_excluded`
- `extensions`
- `platforms`
- `hostnames`
- `first_line_match`

```js
{
    "syntaxmgr_settings": [
        {
            // platforms, can be osx, windows or linux
            "platforms": ["linux", "windows"],
            "settings": {
                "font_size" : 14
            }
        },
        {
            // match a specific computer based on hostname
            // the hostname can be found by running
            //
            //     import platform
            //     platform.node()
            //
            // at sublime console (ctrl + ` )
            //
            "hostnames": ["some-hostname"],
            "settings": {
                "font_size" : 12
            }
        },
        {
            // multiple filters can be applied to the same item
            "platforms": ["linux", "windows"],
            "hostnames": ["some-hostname"],
            "settings": {
                "font_size" : 12
            }
        },
        {
            // apply this setting when first line matches
            "first_line_match": ["#!/.*?/sh"],
            "settings": {
                // the syntax can be identified by running
                //
                //     view.settings().get("syntax")
                //
                // at sublime console (ctrl + ` )
                //
                "syntax" : "Packages/ShellScript/Shell-Unix-Generic.tmLanguage"
            }
        },
        {
            // the scope of the document can be obtained by pressing
            // cmd+alt+p (mac) or ctrl+alt+shift+p (linux / windows)

            // for c and python files
            "scopes": ["source.c", "source.python"],
            "settings": {
                "trim_trailing_white_space_on_save_scope" : true,
                "auto_match_enabled" : true
            }
        },
        {
            // all text files
            "scopes": ["text"],
            "settings": {
                "spell_check": true,
                "color_scheme": "Packages/Color Scheme - Default/Twilight.tmTheme"
            }
        },
        {
            // use latex syntex for these extensions
            // make sure the syntax is applied first and then the settings
            "extensions": ["ltx", "latex", "l"],
            "settings": {
                "syntax": "Packages/LaTeX/LaTeX.tmLanguage"
            }
        },
        {
            // for all text files, excluding latex files
            "scopes": ["text"],
            "scopes_excluded": ["text.tex"],
            "settings": {
                "spell_check": false
            }
        }
    ]
}
```

### Reload Settings

Occasionally, syntax manager may fail to apply settings automatically,
especially when creating new file. Reloading syntax manger will be helpful in
this situation. To reload settings, launch comment palette (`C+shift+p`) and type "Syntax Manager: Reload Settings".


## License
See the `LICENSE.txt` file under this repository.

