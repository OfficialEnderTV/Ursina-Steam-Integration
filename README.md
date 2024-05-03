# Ursina-Steam-Integration
"Integrates" Steam with Ursina Engine for python

Basic usage:
```py
from steammanager import SteamPath
```
Imports path to steam no matter where it is installed

```py
from steammanager import steamID
```
Imports users steam ID, you can use this to open users profile, example:
```py
from steammanager import steamID
import webbrowser
from ursina import *

Button("Open my Steam account", on_click=lambda:webbrowser.open((f"steam://url/SteamIDPage/{steamID}")))
```

```py
from steammanager import PersonaName
```
Imports users Username

Other functions:  
-Saves Avatar automatically to directory you choose  
-Supports language settings, usage:  
line 29-30  
```py
with open("your path to lang files\"+WinCountry+".json", encoding="utf8") as lang:
    glang=json.load(lang)
```
other files:
```py
from steammanager import glang
Text(glang["menu.text"])
```
json name needs to be one of Language Culture Names, json example:
```json
{
  "menu.text":"<green>example text"
}
```
also supports buttons
