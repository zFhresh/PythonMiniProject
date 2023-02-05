import requests
import json
# https://tr1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Fhresh  ?api_key=
user = "Fhresh"
RiotApiKey = "RGAPI-ddc20092-a864-460e-aaa4-e9819cd59e45"
api_url = ""
FullURL = "https://tr1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + user + "?api_key=" + RiotApiKey
a = requests.get(FullURL)
a =  json.loads(a.text)
print(a)
#print("Kullanıcı adı:" + a["name"] + "\nLevel:" + str(a["summonerLevel"]))