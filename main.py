import requests, json
from datetime import datetime
import tzlocal  

def filter_achievement(achievements, name):
    if type(name) == type([]):
        return [el for el in achievements if el['apiname'] in name]
    else:
        return [el for el in achievements if el['apiname'] == name][0]



response = requests.get("http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=236850&key=04A1FBD87DB7129B11BD2B3BF36983FA&steamid=76561198308805136&format=json")
Ach1 = response.json()

achievements = Ach1['playerstats']['achievements']
print( filter_achievement(achievements, 'achievement_one_faith') )
print( filter_achievement(achievements, ['achievement_grand_army', 'achievement_true_heir_of_timur']) )
Time = Ach1['playerstats']['achievements']['unlocktime']


unix_timestamp = float("1616083250")
local_timezone = tzlocal.get_localzone() 
local_time = datetime.fromtimestamp(unix_timestamp, local_timezone)

print(local_time.strftime("%Y-%m-%d %H:00"))


