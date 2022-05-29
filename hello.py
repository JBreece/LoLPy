from riotwatcher import LolWatcher, ApiError
import pandas as pd
import pprint as pp
from tabulate import tabulate

# golbal variables
api_key = 'RGAPI-d1cf6fb6-d177-4e30-9f80-87811f1c4056'
watcher = LolWatcher(api_key)
my_region = 'na1'

summoner_name = input("Enter your summoner name: ")
me = watcher.summoner.by_name(my_region, summoner_name)
pp.pprint(me)

# Return the rank status
my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
pp.pprint(my_ranked_stats)

my_matches = watcher.match.matchlist_by_puuid(my_region, me['puuid'])

# fetch last match detail
last_match = my_matches[0]
match_detail = watcher.match.by_id(my_region, last_match)

participants = []
for row in match_detail['info']['participants']:
    participants_row = {}
    participants_row['champion'] = row['championId']
    participants_row['spell1'] = row['spell1Casts']
    participants_row['spell2'] = row['spell2Casts']
    participants_row['win'] = row['win']
    participants_row['kills'] = row['kills']
    participants_row['deaths'] = row['deaths']
    participants_row['assists'] = row['assists']
    participants_row['totalDamageDealt'] = row['totalDamageDealt']
    participants_row['goldEarned'] = row['goldEarned']
    participants_row['champLevel'] = row['champLevel']
    participants_row['totalMinionsKilled'] = row['totalMinionsKilled']
    participants_row['item0'] = row['item0']
    participants_row['item1'] = row['item1']
    participants.append(participants_row)
df = pd.DataFrame(participants)
print(tabulate(df, headers = 'keys', tablefmt = 'psql'))