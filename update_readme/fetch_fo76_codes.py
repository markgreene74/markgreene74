import requests
import os
import re

FILENAME = "fo76"
FULL_PATH = os.path.join("./", FILENAME)
URL = "https://www.falloutbuilds.com"

ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
content = str(requests.get(URL, headers={"User-Agent": ua}).content)
silos = re.findall(r"\>(ALPHA|BRAVO|CHARLIE)\<", content)
codes = re.findall(r"\>(\d+\s*\d+\s*\d+)\<", content)

# >>> silos
# ['ALPHA', 'BRAVO', 'CHARLIE']
# >>> codes
# ['841 38 947', '676 23 748', '512 39 897']
# >>> list(zip(silos, codes))
# [('ALPHA', '841 38 947'), ('BRAVO', '676 23 748'), ('CHARLIE', '512 39 897')]

s_c_list = [f"{s}:{c}" for s, c in list(zip(silos, codes))]
file_content = "\n".join(s_c_list)

with open(FULL_PATH, "w") as f:
    f.write(file_content)

print(file_content)
