import requests
# pip3 install requests
from bs4 import BeautifulSoup
# pip3 install bs4
from prettytable import PrettyTable
BASE_URL = 'https://www.theguardian.com'
url = f"{BASE_URL}/football/tables"

res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

tables = soup.findAll('table', attrs={'class': 'table table--football table--league-table table--responsive-font table--striped'})

table_links_dict = dict()
for table in tables:
    name_tag = table.find('a', attrs={'class': 'football-matches__heading'})
    link_tag = table.find('a', attrs={'class': 'full-table-link'})
    if name_tag and link_tag:
        name = name_tag.text
        link = f'{BASE_URL}{link_tag.get("href")}'
        table_links_dict[name] = link

print("------------------------------------------------")
for name in table_links_dict:
    print(name)
print("------------------------------------------------")
choice = input("Choose between leagues: ")

chosen_link = table_links_dict[choice]

res = requests.get(chosen_link)
soup = BeautifulSoup (res.content, 'html.parser')

table = soup.find("table", attrs={'class': 'table table--football table--league-table table--responsive-font table--striped'})
tbody = table.find('tbody')
trs = tbody.findAll('tr')
teams = []
for tr in trs:
    tds = tr.findAll('td')
    tds = tds[:len(tds) - 1]
    team = {
        'place' : tds[0].text,
        'name' : tds[1].text.strip(),
        'plays' : tds[2].text,
        'wins' : tds[3].text,
        'draws' : tds[4].text,
        'loses' : tds[5].text,
        'goal_scored' : tds[6].text,
        'goal_gotten' : tds[7].text,
        'goal_delta' : tds[8].text,
        'pts' : tds[9].text
    }
    teams.append(team)

pt = PrettyTable(['P', 'Team', 'GP', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts'])
for team in teams:
    pt.add_row([team['place'], team['name'], team['plays'], team['wins'], team['draws'], team['loses'],
                team['goal_scored'], team['goal_gotten'], team['goal_delta'], team['pts'] ])

print(pt)