from flask import render_template, abort
from . import app
from .forms import Intform
import requests
import pendulum





def fetch_from_api():
    pass


@app.route("/")
def test():

    # https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/

    response = requests.get("https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?appid=236850&key=04A1FBD87DB7129B11BD2B3BF36983FA&steamid=76561198308805136&format=json")

    game_data = response.json()["game"]["availableGameStats"]["achievements"]

    response = requests.get("http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid=236850&key=04A1FBD87DB7129B11BD2B3BF36983FA&steamid=76561198308805136&format=json")
    
    percent_data = response.json()["achievementpercentages"]["achievements"]


    response = requests.get("http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=236850&key=04A1FBD87DB7129B11BD2B3BF36983FA&steamid=76561198308805136&format=json")
    if response.status_code < 200 and response.status_code >= 400:
        abort(500)

    data = response.json()
    # Kontrollera att vi inte fått ett felmeddelande
    if error := data["playerstats"].get("error"):
        return error

    player_data = {}
    for a in  data["playerstats"]["achievements"]:
        player_data[a["apiname"]] = {
            "achieved": a["achieved"], 
            "unlocktime": pendulum.from_timestamp(a["unlocktime"])
            }

    return render_template("test.html", game_data=game_data, player_data=player_data, percent_data=percent_data)
