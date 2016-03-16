import csv

class Match:
    def __init__(self, date, time, homeTeam, awayTeam, homeScore, awayScore, homeOdds, drawOdds, awayOdds):
        self.date = date
        self.time = time
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.homeScore = homeScore
        self.awayScore = awayScore
        self.homeOdds = homeOdds
        self.drawOdds = drawOdds
        self.awayOdds = awayOdds

matches = []


with open('bookmakers.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        match = Match(str(row[0]), str(row[1]), str(row[2]), str(row[3]), int(row[4]), int(row[5]), float(row[8].strip()), float(row[9].strip()), float(row[10].strip()))
        matches.append(match)

for match in matches:
    print match.homeTeam + " vs " + match.awayTeam
