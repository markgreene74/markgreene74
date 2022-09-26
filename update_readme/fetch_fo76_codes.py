import requests
import os
import re

FILENAME = "fo76"
FULL_PATH = os.path.join("./", FILENAME)
NC_URL = "https://nukacrypt.com/"

ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
nc_content = str(requests.get(NC_URL, headers={"User-Agent": ua}).content)
silos = re.findall(r"\>(ALPHA|BRAVO|CHARLIE)\<", nc_content)
codes = re.findall(r"\>(\d+)\<", nc_content)

# >>> silos
# ['ALPHA', 'BRAVO', 'CHARLIE']
# >>> codes
# ['61436701', '36758567', '79473176']
# >>> list(zip(silos, codes))
# [('ALPHA', '61436701'), ('BRAVO', '36758567'), ('CHARLIE', '79473176')]

s_c_list = [f"{s}:{c}" for s, c in list(zip(silos, codes))]
file_content = "\n".join(s_c_list)

with open(FULL_PATH, "w") as f:
    f.write(file_content)

print(file_content)
