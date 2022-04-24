import requests
import os
import re

FILENAME = "FO_76"
FULL_PATH = os.path.join("./", FILENAME)
NC_URL = "https://nukacrypt.com/"

nc_content = str(requests.get(NC_URL).content)
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
