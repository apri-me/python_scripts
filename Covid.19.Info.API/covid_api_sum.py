import time
import requests
from prettytable import PrettyTable
import json



def typing(string, centi_sec = 5):
    string = str(string)
    for letter in string + "\n":
        print(letter, end='', sep="", flush=True)
        time.sleep(.01 * centi_sec)

def get_stat_table(stat_dict):
    pt = PrettyTable(["Case Type", "New", "Total"])
    pt.add_row(["Confirmed", stat_dict['NewConfirmed'], stat_dict['TotalConfirmed']])
    pt.add_row(["Deaths", stat_dict['NewDeaths'], stat_dict['TotalDeaths']])
    pt.add_row(["Recovered", stat_dict['NewRecovered'], stat_dict['TotalRecovered']])
    return pt

summary_url = "https://api.covid19api.com/summary"
r = requests.get(summary_url)

js = r.json()

typing("Hi pal. This is Covid19 API.")
typing("-------------------------------", 4)
typing("Global Stats")
pt = get_stat_table(js['Global'])

typing(pt, 1)

countries_stats = js['Countries']
countries_list = [ (country['Country'], country['CountryCode']) for country in countries_stats ]

ans = ""
while True:
    typing("""Options:
    1. Show Countries List
    2. Choose a Country By Country Code
    3. Quite""")
    ans = input("Select By Number: ")
    if ans == "1":
        print(countries_list)
        input("Enter to continue...")
    elif ans == "2":
        country_code = input("Enter Country Code: ")
        country = filter(lambda c: c['CountryCode'] == country_code, countries_stats)
        country = list(country)[0]
        typing(f"{country['Country']} Stats")
        print(get_stat_table(country))
        input("Enter to continue")
    elif ans == "3":
        break
    else:
        typing("Please Enter The Correct Option!")

typing("Thank you!")
typing("Goodbye!")

