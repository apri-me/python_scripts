import requests
from prettytable import PrettyTable

def get_table(stats):
    pt = PrettyTable(['CASE', 'NEW', 'TOTAL'])
    pt.add_row(["Confirmed", stats['NewConfirmed'], stats['TotalConfirmed']])
    pt.add_row(['Death', stats['NewDeaths'], stats['TotalDeaths']])
    pt.add_row(['Recovered', stats['NewRecovered'], stats['TotalRecovered']])
    return pt

url = "https://api.covid19api.com/summary"

response = requests.get(url)

summary_dict = response.json()

global_summary = summary_dict['Global']

global_table = get_table(global_summary)

countries = summary_dict['Countries']

countries_showlist = [(country['Country'], country['CountryCode']) for country in countries ]

res = 0

while True:
    print("""Options:
    1. Countries list
    2. Select Country by code
    3. Quite""")
    res = input("Select an option:")
    if res == '1':
        print(countries_showlist)
        print()
        input("Enter to continue...")
    elif res == '2':
        code = input("Country code: ")
        country = list(filter(lambda x: code == x['CountryCode'], countries))[0]
        print(get_table(country))
        input('Enter to continue...')
    elif res == '3':
        break
    else:
        print("Select a valid option")

print('Goodbye!')