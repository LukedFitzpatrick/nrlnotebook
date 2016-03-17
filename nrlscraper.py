from lxml import html
import requests

# the master class: completely specifies an NRL game.
class Match:
    def __init__(self):
        # setting everything by passing into constructor here would get way too hectic.
        # we break encapsulation by letting the outside world just straight change the members, but alternate solutions would be too time consuming.
        self.teamAScore = -1
        self.teamBScore = -1
        self.teamAPossPercent = -1
        self.teamBPossPercent = -1
        

def buildMatchData(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    m = Match()
    
    # there's nothing in the <head> section that interests us
    for t in tree[1].iter():
        print t.tag, ": ",
        print t.text

    return m


m = buildMatchData('http://live.nrlstats.com/matches/nrl/match35724.html')
