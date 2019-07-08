from urllib.request import urlopen as uReq # uReq also known as url_Request
from bs4 import BeautifulSoup as soup      # soup

# Set my_url to the URL page
my_url = 'https://www.op.gg/summoner/userName=hide+in+bush'

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

print("SKT T1: Faker Stats\n")

kda_index = 8
for game in games:

    # Game type
    game_type = game.div.div.div.div.text.strip()

    # Game result, Victory/Defeat/None
    game_result_container = game.findAll("div",{"class":"GameResult"})
    game_result = game_result_container[0].text.strip()

    # Champion Played
    champion = game.findAll("div",{"class":"ChampionName"})
    champion_played = champion[0].text.strip()

    # Game KDA, kill, death, assist

    kill_container = page_soup.findAll("span", {"class":"Kill"})
    game_kills = kill_container[kda_index].text.strip()

    death_container = page_soup.findAll("span", {"class":"Death"})
    game_deaths = death_container[kda_index].text.strip()

    assist_container = page_soup.findAll("span", {"class":"Assist"})
    game_assists = assist_container[kda_index].text.strip()

    kda_index += 1



    print(game_type + ": " + game_result)
    print("Champion: " + champion_played)
    print("Kill(s): " + game_kills)
    print("Death(s): " + game_deaths)
    print("Assist(s): " + game_assists)
    print("\n")

# Pete Aguirre II - 2019
