from dash.dependencies import Input, Output, State
import dash_html_components as html
from app import app
import requests
import json
import pickle
from dataclasses import dataclass

api_key = "RGAPI-e4b12d62-46c8-4ebd-b4e2-a5e8843a09d9"
#Dataclasses for the player and match
@dataclass
class Player:
    summonerName: str
    
    def accountId(self) -> str:
        url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.summonerName}?api_key=RGAPI-e4b12d62-46c8-4ebd-b4e2-a5e8843a09d9"
        search = requests.get(url).json()
        return search['accountId']
    #method to get list of match ids
    def recentMatch(self) -> list:
        url = requests.get(f'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/{self.accountId()}?endIndex=1&queue=420&api_key=RGAPI-e4b12d62-46c8-4ebd-b4e2-a5e8843a09d9').json()
        return url['matches'][0]['gameId']



image_ref = {
    '0': 'https://s3.us-east-2.amazonaws.com/leultranscribes/Test/lol-emblems/Emblem_Iron.png',
    '1': 'https://s3.us-east-2.amazonaws.com/leultranscribes/Test/lol-emblems/Emblem_Bronze.png',
    '2': 'https://s3.us-east-2.amazonaws.com/leultranscribes/Test/lol-emblems/Emblem_Silver.png',
    '3': 'https://s3.us-east-2.amazonaws.com/leultranscribes/Test/lol-emblems/Emblem_Gold.png',
    '4': 'https://s3.us-east-2.amazonaws.com/leultranscribes/Test/lol-emblems/Emblem_Platinum.png',
    '5': 'https://s3.us-east-2.amazonaws.com/leultranscribes/Test/lol-emblems/Emblem_Diamond.png',
    '6': 'https://s3.us-east-2.amazonaws.com/leultranscribes/Test/lol-emblems/Emblem_Master.png',
    '7': 'https://s3.us-east-2.amazonaws.com/leultranscribes/Test/lol-emblems/Emblem_Challenger.png',
}   

title_ref = {
    '0':'Iron',
    '1': 'Bronze',
    '2': 'Silver',
    '3': 'Gold',
    '4': 'Platinum',
    '5': 'Diamond',
    '6': 'Master',
    '7': 'Challenger',

}
def convert_title(num):
    return title_ref[num]

@dataclass
class Participant:
    stats: dict
    timeline: dict
    
    #stats related items
    def win(self):
        try:
            return convert_tf(self.stats['win'])
        except:
            return None
    def items(self):
        return 7
    def kills(self):
        try:
            return self.stats['kills']
        except:
            return None
    
    def deaths(self):
        try:
            return self.stats['deaths']
        except:
            return None
    
    def assists(self):
        try:
            return self.stats['assists']
        except:
            return None
    
    def largestKillingSpree(self):
        try:
            return self.stats['largestKillingSpree']
        except:
            return None
    
    def largestMultiKill(self):
        try:
            return self.stats['largestMultiKill']
        except:
            return None
    
    def killingSprees(self):
        try:
            return self.stats['killingSprees']
        except:
            return None
    
    def longestTimeSpentLiving(self):
        try:
            return self.stats['longestTimeSpentLiving']
        except:
            return None
    
    def doubleKills(self):
        try:
            return self.stats['doubleKills']
        except:
            return None
    
    def tripleKills(self):
        try:
            return self.stats['tripleKills']
        except:
            return None
    
    def quadraKills(self):
        try:
            return self.stats['quadraKills']
        except:
            return None
    
    def pentaKills(self):
        try:
            return self.stats['pentaKills']
        except:
            return None
    
    def unrealKills(self):
        try:
            return self.stats['unrealKills']
        except:
            return None
    
    def totalDamageDealtToChampions(self):
        try:
            return self.stats['totalDamageDealtToChampions']
        except:
            return None

    def totalHeal(self):
        try:
            return self.stats['totalHeal']
        except:
            return None
    
    def totalUnitsHealed(self):
        try:
            return self.stats['totalUnitsHealed']
        except:
            return None
    
    def damageSelfMitigated(self):
        try:
            return self.stats['damageSelfMitigated']
        except:
            return None

    def damageDealtToObjectives(self):
        try:
            return self.stats['damageDealtToObjectives']
        except:
            return None

    def visionScore(self):
        try:
            return self.stats['visionScore']
        except:
            return None

    def timeCCingOthers(self):
        try:
            return self.stats['timeCCingOthers']
        except:
            return None

    def totalDamageTaken(self):
        try:
            return self.stats['totalDamageTaken']
        except:
            return None

    def goldEarned(self):
        try:
            return self.stats['goldEarned']
        except:
            return None
    
    def goldSpent(self):
        try:
            return self.stats['goldSpent']
        except:
            return None
    
    def turretKills(self):
        try:
            return self.stats['turretKills']
        except:
            return None
    
    def inhibitorKills(self):
        try:
            return self.stats['inhibitorKills']
        except:
            return None
    
    def totalMinionsKilled(self):
        try:
            return self.stats['totalMinionsKilled']
        except:
            return None
    
    def totalTimeCrowdControlDealt(self):
        try:
            return self.stats['totalTimeCrowdControlDealt']
        except:
            return None
    
    def champLevel(self):
        try:
            return self.stats['champLevel']
        except:
            return None
    
    def wardsPlaced(self):
        try:
            return self.stats['wardsPlaced']
        except:
            return None
    
    def wardsKilled(self):
        try:
            return self.stats['wardsKilled']
        except:
            return None
    
    def firstBloodKill(self):
        try:
            return convert_tf(self.stats['firstBloodKill'])
        except:
            return None
    
    def firstBloodAssist(self):
        try:
            return convert_tf(self.stats['firstBloodAssist'])
        except:
            return None
    
    def firstTowerKill(self):
        try:
            return convert_tf(self.stats['firstTowerKill'])
        except:
            return None
    
    def firstTowerAssist(self):
        return convert_tf(self.stats['firstTowerAssist'])
    
    def firstInhibitorKill(self):
        try:
            return convert_tf(self.stats['firstInhibitorKill'])
        except:
            return None
        
    def firstInhibitorAssist(self):
        try:
            return convert_tf(self.stats['firstInhibitorAssist'])
        except:
            return None

    
    #timeline related items
    #creeps per/min
    def creeps_early(self):
        try:
            return self.timeline['creepsPerMinDeltas']['0-10']
        except:
            return None
    
    def creeps_mid(self):
        try:
            return self.timeline['creepsPerMinDeltas']['10-20']
        except:
            return None
    
    def creeps_late(self):
        try:
            return self.timeline['creepsPerMinDeltas']['20-30']
        except:
            return None
        
    def creeps_end(self):
        try:
            return self.timeline['creepsPerMinDeltas']['30-end']
        except:
            return None
      #xp per/min
    def xp_early(self):
        try:
            return self.timeline['xpPerMinDeltas']['0-10']
        except:
            return None
    
    def xp_mid(self):
        try:
            return self.timeline['xpPerMinDeltas']['10-20']
        except:
            return None
    
    def xp_late(self):
        try:
            return self.timeline['xpPerMinDeltas']['20-30']
        except:
            return None
        
    def xp_end(self):
        try:
            return self.timeline['xpPerMinDeltas']['30-end']
        except:
            return None
     #gold per/min
    def gold_early(self):
        try:
            return self.timeline['goldPerMinDeltas']['0-10']
        except:
            return None
    
    def gold_mid(self):
        try:
            return self.timeline['goldPerMinDeltas']['10-20']
        except:
            return None
    
    def gold_late(self):
        try:
            return self.timeline['goldPerMinDeltas']['20-30']
        except:
            return None
        
    def golds_end(self):
        try:
            return self.timeline['goldPerMinDeltas']['30-end']
        except:
            return None
        #cs diff per/min
    def csdiff_early(self):
        try:
            return self.timeline['csDiffPerMinDeltas']['0-10']
        except:
            return None
    
    def csdiff_mid(self):
        try:
            return self.timeline['csDiffPerMinDeltas']['10-20']
        except:
            return None
    
    def csdiff_late(self):
        try:
            return self.timeline['csDiffPerMinDeltas']['20-30']
        except:
            return None
        
    def  csdiff_end(self):
        try:
            return self.timeline['csDiffPerMinDeltas']['30-end']
        except:
            return None
        
                #xp diff per/min
    def xpdiff_early(self):
        try:
            return self.timeline['xpDiffPerMinDeltas']['0-10']
        except:
            return None
    
    def xpdiff_mid(self):
        try:
            return self.timeline['xpDiffPerMinDeltas']['10-20']
        except:
            return None
    
    def xpdiff_late(self):
        try:
            return self.timeline['xpDiffPerMinDeltas']['20-30']
        except:
            return None
        
    def  xpdiff_end(self):
        try:
            return self.timeline['xpDiffPerMinDeltas']['30-end']
        except:
            return None
        
        #dmg taken per/min
    def dmgtaken_early(self):
        try:
            return self.timeline['damageTakenPerMinDeltas']['0-10']
        except:
            return None
    
    def dmgtaken_mid(self):
        try:
            return self.timeline['damageTakenPerMinDeltas']['10-20']
        except:
            return None
    
    def dmgtaken_late(self):
        try:
            return self.timeline['damageTakenPerMinDeltas']['20-30']
        except:
            return None
        
    def  dmgtaken_end(self):
        try:
            return self.timeline['damageTakenPerMindmgtaken']['30-end']
        except:
            return None
        
                #dmg taken diff per/min
    def dmgtaken_diff_early(self):
        try:
            return self.timeline['damageTakenDiffPerMinDeltas']['0-10']
        except:
            return None
    
    def dmgtaken_diff_mid(self):
        try:
            return self.timeline['damageTakenDiffPerMinDeltas']['10-20']
        except:
            return None
    
    def dmgtaken_diff_late(self):
        try:
            return self.timeline['damageTakenDiffPerMinDeltas']['20-30']
        except:
            return None
        
    def  dmgtaken_diff_end(self):
        try:
            return self.timeline['damageTakenDiffPerMinDeltas']['30-end']
        except:
            return None
        
stat_columns = ['assists',
 'champLevel',
 'creeps_early',
 'creeps_end',
 'creeps_late',
 'creeps_mid',
 'csdiff_early',
 'csdiff_end',
 'csdiff_late',
 'csdiff_mid',
 'damageDealtToObjectives',
 'damageSelfMitigated',
 'deaths',
 'dmgtaken_diff_early',
 'dmgtaken_diff_end',
 'dmgtaken_diff_late',
 'dmgtaken_diff_mid',
 'dmgtaken_early',
 'dmgtaken_end',
 'dmgtaken_late',
 'dmgtaken_mid',
 'doubleKills',
 'goldEarned',
 'goldSpent',
 'gold_early',
 'gold_late',
 'gold_mid',
 'golds_end',
 'inhibitorKills',
 'items',
 'killingSprees',
 'kills',
 'largestKillingSpree',
 'largestMultiKill',
 'longestTimeSpentLiving',
 'pentaKills',
 'quadraKills',
 'timeCCingOthers',
 'totalDamageDealtToChampions',
 'totalDamageTaken',
 'totalHeal',
 'totalMinionsKilled',
 'totalTimeCrowdControlDealt',
 'totalUnitsHealed',
 'tripleKills',
 'turretKills',
 'unrealKills',
 'visionScore',
 'wardsKilled',
 'wardsPlaced',
 'win',
 'xp_early',
 'xp_end',
 'xp_late',
 'xp_mid',
 'xpdiff_early',
 'xpdiff_end',
 'xpdiff_late',
 'xpdiff_mid'
      ]        
    
        
    

def convert_image(number):
    return image_ref[number]


pkl_filename = 'rfpickledModel.pkl'
pickle_model = pickle.load( open( "rfpickledModel.pkl", "rb" ) )

def convert_tf(statement):
    if statement == True:
        return 1
    else:
        return 0


def get_accid(input1,input2):
    id_url = f"https://{input2}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{input1}?api_key=RGAPI-e4b12d62-46c8-4ebd-b4e2-a5e8843a09d9"
    search = requests.get(id_url).json()
    return search['id']
def pull_stats(acc_id,region):
    stats_url = requests.get(f"https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{acc_id}?api_key=RGAPI-e4b12d62-46c8-4ebd-b4e2-a5e8843a09d9").json()
    # leaguePoints    wins    losses    veteran    inactive    hotStreak    freshBlood
    return stats_url

@app.callback(
    Output('home-page', 'children'),
    [Input('home-link', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

@app.callback(Output('output', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('input-1-state', 'value'),
               State('input-2-state', 'value')])
def update_output(n_clicks, input1, input2):
    player = Player(input1)
    stats_url = requests.get(f'https://na1.api.riotgames.com/lol/match/v4/matches/{player.recentMatch()}?api_key=RGAPI-e4b12d62-46c8-4ebd-b4e2-a5e8843a09d9').json()
    args = []
    for i in range(len(stats_url['participantIdentities'])):
        if stats_url['participantIdentities'][i]['player']['summonerName'] == player.summonerName:
            args.append(stats_url['participants'][i]['stats'])
            args.append(stats_url['participants'][i]['timeline'])
        else:
            continue

    player_stats = Participant(args[0],args[1])
    data = [player_stats.__getattribute__(r)() for r in stat_columns]
    playerdata = [0 if v is None else v for v in data]
    predicted = pickle_model.predict([playerdata])
    predicted_number = str(predicted[0])
    img_link = convert_image(predicted_number)
    rank_title = convert_title(predicted_number)

    return html.Figure(children = [
        html.Img(src=img_link),
        html.Figcaption(children=rank_title),
    ]),
    
    





