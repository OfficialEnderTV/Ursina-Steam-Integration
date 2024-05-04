# Ursina-Steam-Integration
"Integrates" Steam with Ursina Engine for python  
THIS IS NOT SUPPORTED BY VALVE
  
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

app=Ursina()

Button("Open my Steam account", on_click=lambda:webbrowser.open((f"steam://url/SteamIDPage/{steamID}")))

app.run()
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
from ursina import *

app=Ursina()

Text(glang["menu.text"])

app.run()
```
json name needs to be one of Language Culture Names, json example:
```json
{
  "menu.text":"<green>example text"
}
```
also supports buttons
