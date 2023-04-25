import collections
import random
import match
import datetime


class Championship:
    current_id = 0

    def __init__(self, name, team_count, country):
        # Unique ID
        self.id = Championship.current_id
        Championship.current_id += 1

        self.name = name
        self.team_count = team_count
        self.matchday_count = (self.team_count - 1) * 2
        self.match_count_by_matchday = self.team_count // 2
        self.country = country
        self.championship_editions = []

    def is_country_championship(self):
        return self.country != None


class ChampionshipEdition:
    current_id = 0

    def __init__(self, championship, period, teams):
        # Unique ID
        self.id = ChampionshipEdition.current_id
        ChampionshipEdition.current_id += 1

        self.championship = championship
        # Add this edition to its corresponding championship
        championship.championship_editions.append(self)

        self.period = period
        self.teams = teams
        # Check team count
        assert len(
            teams) == championship.team_count, "Team count does not match championship's"
        self.leaderboard = Leaderboard(teams, self)
        # Add this championship edition to team's
        for team in self.teams:
            team.add_championship_edition(self)
        # Generate matchdays
        self.schedule_matchdays()

    def schedule_matchdays(self):
        rotation_teams = self.teams.copy()
        random.shuffle(rotation_teams)
        self.matchdays = [match.Matchday(self, i + 1)
                          for i in range(self.championship.matchday_count)]
        for i in range(self.championship.matchday_count // 2):
            for j in range(0, self.championship.team_count, 2):
                # Home match
                home_match = match.Match(
                    rotation_teams[j], rotation_teams[j + 1], self, self.matchdays[i])
                self.matchdays[i].add(home_match)
                # Away match
                away_match = match.Match(
                    rotation_teams[j + 1], rotation_teams[j], self, self.matchdays[i + self.championship.matchday_count //
                                                                                   2])
                self.matchdays[i + self.championship.matchday_count //
                               2].add(away_match)
            # Rotation. Example: [6, 19, 2, 1, 3, 26] -> [6, 26, 19, 2, 1, 3] -> [6, 3, 26, 19, 2, 1] -> [6, 1, 3, 26, 19, 2] -> [6, 2, 1, 3, 26, 19]
            rotation_teams = [rotation_teams[0]] + \
                [rotation_teams[-1]] + rotation_teams[1:-1]

    def play_matchday(self):
        for matchday in self.matchdays:
            print(matchday)

    def __str__(self) -> str:
        result = ""
        for matchday in self.matchdays:
            result += matchday.__str__()
        return result


class Leaderboard:
    current_id = 0

    def __init__(self, teams, championship_edition):
        # Unique ID
        self.id = Leaderboard.current_id
        Leaderboard.current_id += 1
        self.championship_edition = championship_edition
        # Initialize team statistics for all teams (for modification)
        self.modification_data_structure = collections.deque()
        for team in teams:
            championship_edition_team_statistics = ChampionshipEditionTeamStatistics(
                team, self.championship_edition)
            self.modification_data_structure.append(
                championship_edition_team_statistics)


class ChampionshipEditionTeamStatistics:
    labels = {"MP": "Matches Played",
              "W": "Wins",
              "D": "Draws",
              "L": "Losses",
              "GF": "Goals For",
              "GA": "Goals Against",
              "GD": "Goal Difference",
              "P": "Points"}

    def __init__(self, team, championship_edition):
        self.team = team
        self.championship_edition = championship_edition
        self.statistics = {label: 0 for label in list(
            ChampionshipEditionTeamStatistics.labels.keys())}

    def add_match_played(self):
        self.statistics["MP"] += 1

    def add_win(self, match):
        self.add_match_played()
        self.statistics["W"] += 1
        self.statistics["P"] += 3

    def add_draw(self, match):
        self.add_match_played()
        self.statistics["D"] += 1
        self.statistics["P"] += 1

    def add_loss(self, match):
        self.add_match_played()
        self.statistics["L"] += 1

    def handle_goals(self, match):
        self.statistics["GF"] += match.statistics[self].get("GF")
        self.statistics["GA"] += match.statistics[self].get("GA")
        self.statistics["GD"] = self.statistics["GF"] - self.statistics["GA"]

    def get(self, label):
        data = self.statistics.get(label)
        assert data != None, "No statistic data found for this label"
        return data
