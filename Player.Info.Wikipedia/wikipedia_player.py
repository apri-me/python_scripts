from wikipediaapi import Wikipedia

player_name = input("Enter player name: ")
wiki = Wikipedia(language='en')
page = wiki.page(player_name)

for s in page.sections:
    if 'Club career' in s.title:
        print(s.title)
        for p in s.sections:
            print("\t"+p.title)
            if p.sections != None:
                for q in p.sections:
                    print("\t\t"+q.title)