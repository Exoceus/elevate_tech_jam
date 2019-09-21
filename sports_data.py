import http.client
from bs4 import BeautifulSoup

conn = http.client.HTTPSConnection("api.sportradar.us")

sports = ['basketball', 'hockey', 'football']
sport_keys = ['utym8e56jrenbwnu3ajxms45',
              'jksnx2yj7eh9krhbeqf9qwkp', 'md3ntb4d22jr27s26egss5wf']

print('What sport do you like')
for i in range(len(sports)):
    print(i+1, ': ', sports[i])

input_num = int(input('Enter the number here: '))-1
sports_interest, key = sports[input_num], sport_keys[input_num]

if sports_interest == 'basketball':
    request1 = 'http://api.sportradar.us/nba/trial/v7/en/games/'

elif sports_interest == 'hockey':
    request1 = 'http://api.sportradar.us/nhl/trial/v6/en/games/'

elif sports_interest == 'football':
    request1 = 'http://api.sportradar.us/nfl/official/trial/v5/en/games/'

request2 = '/REG/schedule.xml?api_key='
year = str(2019)

conn.request(
    "GET", request1 + year + request2 + key)

res = conn.getresponse()
data = res.read()

html_doc = data.decode("utf-8")
soup = BeautifulSoup(html_doc, 'html.parser')

games = soup.find_all('game')
fav_team = input('Enter your team shortname (three letter): ')

fav_games = []

for i in range(len(games)):
    if games[i].home['alias'] == fav_team:
        fav_games.append(games[i])

    elif games[i].away['alias'] == fav_team:
        fav_games.append(games[i])

for i in range(len(fav_games)):
    home_team = fav_games[i].home['name'] + \
        ' (' + fav_games[i].home['alias'] + ')'
    away_team = fav_games[i].away['name'] + \
        ' (' + fav_games[i].away['alias'] + ')'
    game_time = fav_games[i]['scheduled']
    game_time = game_time[0:10]

    try:
        broadcast_channel_number = games[i].broadcast['channel']
        broadcast_channel_network = games[i].broadcast['network']
    except (TypeError, KeyError):
        broadcast_channel_number = '123'
        broadcast_channel_network = 'ESPN'

    print('Hey there, the ' + home_team + ' are playing the ' +
          away_team + ' on the ' + game_time + '!\nYou can catch them on ' + broadcast_channel_network + '!\nWe don\'t want you to miss out. So, we are giving you a 40% discount on the ' + sports_interest + ' bundle!!')
