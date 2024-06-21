import requests
from bs4 import BeautifulSoup
import json
import boto3

# AWS S3 Configuration
s3 = boto3.client(
    's3',
    region_name='insert region name',  # e.g., 'us-west-2'
    aws_access_key_id='insert access key',
    aws_secret_access_key='insert secret access key'
)
bucket_name = 'lck-stats'

def scrape_teams():
    base_url = 'https://gol.gg'
    url = 'https://gol.gg/teams/list/season-ALL/split-ALL/tournament-LCK%20Summer%202024/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        print(response.text)
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    table = soup.find('table', {'class': 'table_list'})
    if table is None:
        print("Could not find the table with class 'table_list'")
        return []
    
    teams = []
    
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        team_name = cols[0].text.strip()
        relative_link = cols[0].find('a')['href']
        team_link = f'{base_url}{relative_link}'
        win_rate = cols[4].text.strip()
        kda = cols[5].text.strip()
        
        gold_per_minute = cols[6].text.strip()
        gold_differential_per_minute = cols[7].text.strip()
        game_duration = cols[8].text.strip()
        kills_per_game = cols[9].text.strip()
        deaths_per_game = cols[10].text.strip()
        towers_lost = cols[12].text.strip()
        first_blood_rate = cols[13].text.strip()
        first_tower_rate = cols[14].text.strip()
        dragons_killed_per_game = cols[15].text.strip()
        dragon_percentage = cols[16].text.strip()
        voidgrubs_killed_per_game = cols[17].text.strip()
        herald_killed_per_game = cols[18].text.strip()
        herald_percentage = cols[19].text.strip()
        drag_at_15 = cols[20].text.strip()
        tower_differential_at_15 = cols[21].text.strip()
        gold_differential_at_15 = cols[22].text.strip()
        tower_plates_per_game = cols[23].text.strip()
        baron_killed_per_game = cols[24].text.strip()
        baron_percentage = cols[25].text.strip()
        creeps_per_minute = cols[26].text.strip()
        damage_per_minute = cols[27].text.strip()
        wards_per_minute = cols[28].text.strip()
        vision_wards_per_minute = cols[29].text.strip()
        wards_cleared_per_minute = cols[30].text.strip()
        
        team = {
            'team_name': team_name,
            'team_link': team_link,
            'win_rate': win_rate,
            'kda': kda,
            'gold_per_minute': gold_per_minute,
            'gold_differential_per_minute': gold_differential_per_minute,
            'game_duration': game_duration,
            'kills_per_game': kills_per_game,
            'deaths_per_game': deaths_per_game,
            'towers_lost': towers_lost,
            'first_blood_rate': first_blood_rate,
            'first_tower_rate': first_tower_rate,
            'dragons_killed_per_game': dragons_killed_per_game,
            'dragon_percentage': dragon_percentage,
            'voidgrubs_killed_per_game': voidgrubs_killed_per_game,
            'herald_killed_per_game': herald_killed_per_game,
            'herald_percentage': herald_percentage,
            'drag_at_15': drag_at_15,
            'tower_differential_at_15': tower_differential_at_15,
            'gold_differential_at_15': gold_differential_at_15,
            'tower_plates_per_game': tower_plates_per_game,
            'baron_killed_per_game': baron_killed_per_game,
            'baron_percentage': baron_percentage,
            'creeps_per_minute': creeps_per_minute,
            'damage_per_minute': damage_per_minute,
            'wards_per_minute': wards_per_minute,
            'vision_wards_per_minute': vision_wards_per_minute,
            'wards_cleared_per_minute': wards_cleared_per_minute
        }
        teams.append(team)
    
    return teams

def store_data_in_s3(data, filename):
    s3.put_object(Bucket=bucket_name, Key=filename, Body=json.dumps(data, indent=4))

def scrape_and_store_data():
    teams = scrape_teams()
    store_data_in_s3(teams, 'lck_teams_stats.json')
    print("Data scraped and stored in S3 successfully.")

if __name__ == "__main__":
    scrape_and_store_data()
