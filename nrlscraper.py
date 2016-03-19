from lxml import html
from lxml import etree
import requests


# the master class: completely specifies an NRL game.
class Match:
    def __init__(self):
        # setting everything by passing into constructor here would get way too hectic.
        # we break encapsulation by letting the outside world just straight change the members, but alternate solutions would be too time consuming.
        pass

def recursivePrintChildrenWithIndex(root, indentLine):
    count = 0
    for child in root:
        #try:
        if child.text == None:
            text = ""
        else:
            text = child.text

        print str(indentLine) + "[" + str(count) + "]: " + text.encode('utf-8')
        #except:
        #    print "ASCII Error!"
        recursivePrintChildrenWithIndex(child, "  " + indentLine + "["+str(count)+"]")
        count += 1

def buildMatchData(url):
    m = Match()

    page = requests.get(url)
    tree = html.fromstring(page.content).body
    
    
    m.date = tree[0][6][0][1][1][0][0][0][1].text
    m.weather = tree[0][6][0][1][1][0][1][1][1].text
    m.surface = tree[0][6][0][1][1][0][1][2][1].text
    m.referee = tree[0][6][0][1][1][0][2][0][1].text
    m.touchJudges = tree[0][6][0][1][1][0][2][1][1].text
    m.videoReferee = tree[0][6][0][1][1][0][2][2][1].text
    m.injuries = tree[0][6][0][1][1][0][5][0][1].text
    m.crowd = int(tree[0][6][0][1][1][0][6][0][1].text)
    m.teamAName = tree[0][6][0][0][1][0][0][0].text
    m.teamBName = tree[0][6][0][0][1][0][0][2].text
    m.teamAScore = int(tree[0][6][1][0][1][2][0][1][0][0].text)
    m.teamBScore = int(tree[0][6][1][0][1][2][0][1][2][0].text)
    m.teamATries = int(tree[0][6][1][0][1][2][0][2][0][0].text)
    m.teamBTries = int(tree[0][6][1][0][1][2][0][2][2][0].text)
    m.teamAConversions = tree[0][6][1][0][1][2][0][3][0][0].text
    m.teamBConversions = tree[0][6][1][0][1][2][0][3][2][0].text
    m.teamAPenaltyGoals = tree[0][6][1][0][1][2][0][4][0][0].text
    m.teamBPenaltyGoals = tree[0][6][1][0][1][2][0][4][2][0].text

    return m



m = buildMatchData('http://live.nrlstats.com/matches/nrl/match35154.html')

print m.date
print m.weather
print m.surface
print m.referee
print m.touchJudges
print m.videoReferee
print m.injuries
print m.crowd
print m.teamAName
print m.teamBName
print m.teamAScore
print m.teamBScore
print m.teamAConversions
print m.teamBConversions
print m.teamAPenaltyGoals
print m.teamBPenaltyGoals
