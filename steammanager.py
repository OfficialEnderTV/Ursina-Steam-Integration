import os, winreg, vdf, shutil, json

def read_reg(ep, p = r"", k = ''):
    try:
        key = winreg.OpenKeyEx(ep, p)
        value = winreg.QueryValueEx(key,k)
        if key:
            winreg.CloseKey(key)
        return value[0]
    except Exception as e:
        return None

#read registry
WinCountry = str(read_reg(ep = winreg.HKEY_CURRENT_USER, p = r"Control Panel\International", k = 'LocaleName'))
SteamPath = str(read_reg(ep = winreg.HKEY_LOCAL_MACHINE, p = r"SOFTWARE\Wow6432Node\Valve\Steam", k = 'InstallPath'))

#load some data
UserVDF=(SteamPath+r"\config\loginusers.vdf")
ACache = os.listdir(SteamPath+r"\config\avatarcache")

#load users steamID
steamid = list(map(lambda sub:int(''.join(filter(str.isnumeric, sub))), ACache))
steamID = steamid[0]

#copy avatar from cache
Avatardir = SteamPath+rf"\config\avatarcache\{steamID}.png"
shutil.copy(Avatardir, "data/user")

#get users nickname
VDF=vdf.load(open(UserVDF))
PersonaName = VDF["users"][f"{steamID}"]["PersonaName"]

#Language
#with open("data/languages/"+WinCountry+".json", encoding="utf8") as lang:
#    glang=json.load(lang)

assert Avatardir, "No avatar found"
assert SteamPath, "No Steam Installation Path found"
assert UserVDF, "No user found"

print(f"SteamPath: {SteamPath}\nLang: {WinCountry}\nUserVDF: {UserVDF}\nSteamID: {steamID}\nAvatardir: {Avatardir}")
