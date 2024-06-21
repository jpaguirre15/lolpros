# What we can learn from here:
# - Recently, Smeb has a Double Kill, so the game_kills detects Double Kill
#   instead of a number of kill he has.
# - Challenges: some websites aren't consistent 

from urllib.request import urlopen as uReq # uReq also known as url_Request
from bs4 import BeautifulSoup as soup      # soup

# Set my_url to the URL page
my_url = 'https://www.op.gg/summoner/userName=%EC%B6%98%EB%B4%89%EB%B0%95'

# Grab the webpage and download it, store it in the web client
uClient = uReq(my_url)

# Read the HTML page and store it at page_html
page_html = uClient.read()

# Close the web client
uClient.close()

# HTML parser
page_soup = soup(page_html, "html.parser")

# Grab each game information
games = page_soup.findAll("div", {"class":"GameItemWrap"})

print("KT Rolster: Smeb Stats\n")

kda_index = 8
for game in games:

    # Game type
    game_type = game.div.div.div.div.text.strip()

    # Game result, Victory/Defeat/None
    game_result_container = game.findAll("div",{"class":"GameResult"})
    game_result = game_result_container[0].text.strip()
    print(game_type + ": " + game_result)

    # Champion Played
    champion = game.findAll("div",{"class":"ChampionName"})
    champion_played = champion[0].text.strip()
    print("Champion: " + champion_played)

    # Game KDA, kill, death, assist
    kill_container = page_soup.findAll("span", {"class":"Kill"})
    game_kills = kill_container[kda_index].text.strip()
    if game_kills is not 'Double Kill' or 'Triple Kill':
        print("Kill(s): ", game_kills)
    else:
        kda_index +=1
        print("Kill(s): ", game_kills)

    #death_container = page_soup.findAll("span", {"class":"Death"})
    #game_deaths = death_container[kda_index].text.strip()

    #assist_container = page_soup.findAll("span", {"class":"Assist"})
    #game_assists = assist_container[kda_index].text.strip()

    #kda_ratio = (int(game_kills) + int(game_assists))/int(game_deaths)

    kda_index += 1



    #print(game_type + ": " + game_result)
    #print("Champion: " + champion_played)
    #print("Kill(s): ", game_kills)
    #print("Death(s): " + game_deaths)
    #print("Assist(s): " + game_assists)
    #print("KDA Ratio: %d", kda_ratio)
    print("\n")

# Pete Aguirre II - 2019
