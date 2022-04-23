import requests
import json
import os

FILENAME = "fo_76"
FULL_PATH = os.path.join("../", FILENAME)
NC_URL = "https://nukacrypt.com/codes.json"

nc_content = requests.get(NC_URL).content
j = json.loads(nc_content)

file_content = ""

for silo in ["alpha", "bravo", "charlie"]:
    file_content += f"|{silo}:{j[silo]}|\n"

with open(FULL_PATH, "w") as f:
    f.write(file_content)

print(file_content)