import requests
import os
from bs4 import BeautifulSoup

url = "https://free-proxy-list.net/"
cwd = os.getcwd()

# ANSI COLORS
RED  = '\033[1;31m' 
GREEN  = '\033[1;32m'
CLOSE = '\x1b[0m'

try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("tr")

    if len(rows) > 0:
        proxies = []
        for row in rows:
            columns = row.find_all("td")
            if len(columns) >= 2:
                ip = columns[0].get_text()
                port = columns[1].get_text()
                proxies.append(f"{ip}:{port}")

        proxies = [proxy for proxy in proxies if not proxy.startswith(("Total:", " US:", " IN:", " KH:", " BD:", " JP:", " VE:", " DO:"))]

        with open(f"{cwd}/Files/proxys.txt", "w") as file:
            file.write("\n".join(proxies))

        print("\n{GREEN}[+] Proxys saved in /Files/proxys.txt {CLOSE}\n")
    else:
        raise Exception("{RED}[-] No table rows found containing proxy information {CLOSE}")

except requests.exceptions.RequestException as e:
    print(f"{RED}[-] Error{CLOSE}: Failed to retrieve text from {url}. Exception: {e}")
except Exception as e:
    print(f"{RED}[-] Error{CLOSE}: {e}")
    
