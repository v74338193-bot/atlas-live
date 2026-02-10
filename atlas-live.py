import requests, re
from requests.structures import CaseInsensitiveDict
import os

# Colors
Re = '\033[1;31m'
Gr = '\033[1;32m'
Blu = '\033[1;34m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'

# Clean the terminal
def clean():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# URL
url = "http://www.insecam.org/en/jsoncountries/"

headers = CaseInsensitiveDict()
headers["User-Agent"] = "Mozilla/5.0"

resp = requests.get(url, headers=headers)
data = resp.json()
countries = data['countries']

# Banner 1
def banner():
    camhack = f"""{Re}

      █████╗ ████████╗██╗      █████╗ ███████╗
     ██╔══██╗╚══██╔══╝██║     ██╔══██╗██╔════╝
     ███████║   ██║   ██║     ███████║███████╗
     ██╔══██║   ██║   ██║     ██╔══██║╚════██║
     ██║  ██║   ██║   ███████╗██║  ██║███████║
     ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝

           {Wh}|----------------------------------------|
           {Wh}| {Gr}ATLAS LIVE                           {Wh}|
           {Wh}| {Gr}https://t.me/Atlas_2x                {Wh}|
           {Wh}|----------------------------------------|
    """
    print(camhack)

# Banner 2
def banner2():
    camhack1 = f"""{Wh}

{Cy}     .'``'.      ...           {Wh}|----------------------------------------|
{Cy}     :o  o `....'`  ;          {Wh}| {Gr}ATLAS LIVE                             {Wh}|
{Cy}     `. O         :'           {Wh}| {Gr}https://t.me/Atlas_2x                  {Wh}|
{Cy}       `':          `.         {Wh}|----------------------------------------|
{Cy}         `:.          `.
{Cy}          : `.         `.
{Cy}         `..'`...       `.
{Cy}                 `...     `.
{Cy}                   ``...  `.
{Cy}                          `````.
    """
    print(camhack1)


def camapp():
    clean()
    banner()

    columns = 3
    count = 0

    for key, value in countries.items():
        print(f'{Gr}({key}) {value["country"]} ({value["count"]})'.ljust(30), end=' ')
        count += 1
        if count % columns == 0:
            print()

    if count % columns != 0:
        print()

    try:
        # ⬅ إدخال بسيط بدون (┌─[CCTV-Live…])
        country = input(f"\n{Wh}$ ").lower()

        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}", headers=headers
        )

        last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

        all_ips = []

        for page in range(int(last_page)):
            res = requests.get(
                f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
                headers=headers
            )
            find_ip = re.findall(r"http://\d+\.\d+\.\d+\.\d+:\d+", res.text)
            all_ips.extend(find_ip)

        clean()
        banner2()

        if not all_ips:
            print(f"{Re}No cameras found for this country.")
        else:
            for ip in all_ips:
                print(f"{Re}{ip}")

        input(f"\n{Blu}Press Enter to continue...")
        camapp()

    except Exception as e:
        print(f"Errore: {e}")

# Run
if __name__ == '__main__':
    try:
        camapp()
    except KeyboardInterrupt:
        clean()
        exit()
