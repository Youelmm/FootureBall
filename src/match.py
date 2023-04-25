class Match:
    current_id = 0

    def __init__(self, first_team, second_team, championship_edition, matchday):
        # Unique ID
        self.id = Match.current_id
        Match.current_id += 1

        self.first_team = first_team
        self.second_team = second_team
        self.championship_edition = championship_edition
        self.matchday = matchday
        self.is_game_in_progress = False
        self.is_game_over = False
        # Match statistics
        self.statistics = {
            self.first_team.id: TeamMatchStatistics(
                self, self.first_team),
            self.second_team.id: TeamMatchStatistics(
                self, self.second_team)
        }

    def __str__(self) -> str:
        return f"{self.first_team} - {self.second_team}, {self.championship_edition.championship.name} {self.championship_edition.period} Matchday {self.matchday.number}"

    def play(self):
        self.is_game_in_progress = True
        # TODO: play mechanism


class TeamMatchStatistics:
    labels = {
        "GF": "Goals For",
        "GA": "Goals Against"}

    def __init__(self, match, team):
        self.match = match
        self.team = team
        self.statistics = {label: 0 for label in list(
            TeamMatchStatistics.labels.keys())}

    def add_goal_for(self):
        self.statistics["GF"] += 1

    def add_goal_against(self):
        self.statistics["GA"] += 1

    def get(self, label):
        data = self.statistics.get(label)
        assert data != None, "No statistic data found for this label"
        return data


class Matchday:
    current_id = 0

    def __init__(self, championship_edition, number):
        # Unique ID
        self.id = Matchday.current_id
        Matchday.current_id += 1

        self.championship_edition = championship_edition
        self.number = number
        self.matches = []

    def __str__(self) -> str:
        result = ""
        for match in self.matches:
            result += f"{match}\n"
        result += "\n"
        return result

    def add(self, match):
        self.matches.append(match)
