import requests
import pandas as pd
import json
url = "https://d3fmsgjb23nf52.cloudfront.net/api/user/?format=json&limit=10000"
res = requests.get(url)
res = res.json()["results"]
data = []
for i in res:
    profile = i["profile"]

    if profile:
        profile.update({"username": i["username"]})
        profile.update({"first_name": i["first_name"]})
        profile.update({"last_name": i["last_name"]})
        profile.update({"email": i["email"]})
    else:
        profile = {
            "username": i["username"],
            "first_name": i["first_name"],
            "last_name": i["last_name"],
            "email": i["email"]
        }

    data.append(profile)
df = pd.json_normalize(data)
df.to_csv("samplecsv.csv")