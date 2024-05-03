import os, winreg, vdf, json, shutil

def read_reg(ep, p = r"", k = ''):
    try:
        key = winreg.OpenKeyEx(ep, p)
        value = winreg.QueryValueEx(key,k)
        if key:
            winreg.CloseKey(key)
        return value[0]
    except Exception as e:
        return None

SteamPath = str(read_reg(ep = winreg.HKEY_LOCAL_MACHINE, p = r"SOFTWARE\Wow6432Node\Valve\Steam", k = 'InstallPath'))
assert SteamPath, "No Steam InstallPath found"
WinCountry = str(read_reg(ep = winreg.HKEY_CURRENT_USER, p = r"Control Panel\International", k = 'LocaleName'))
print(f"loaded system language: {WinCountry}")

idpath = os.listdir(SteamPath+r"\config\avatarcache")
steamid = list(map(lambda sub:int(''.join(filter(str.isnumeric, sub))), idpath))
steamID = steamid[0]
print(f"loaded steamID: {steamID}")

loginusers=(SteamPath+r"\config\loginusers.vdf")
assert loginusers, "No user found"
loadvdf=vdf.load(open(loginusers))
PersonaName=loadvdf["users"][f"{steamID}"]["PersonaName"]
print(f"loaded personaname from dynamic location: {loginusers}")

with open("data/languages/"+WinCountry+".json", encoding="utf8") as lang:
    glang=json.load(lang)
print("loaded language")

avatardir=SteamPath+rf"\config\avatarcache\{steamID}.png"
shutil.copy(avatardir, "data/user")
assert avatardir, "No avatar found"
print("copied avatar from cache")