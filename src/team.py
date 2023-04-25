import random


class Team:
    current_id = 0

    def __init__(self, name, abbreviation, country):
        # Unique ID
        self.id = Team.current_id
        Team.current_id += 1

        self.name = name
        self.abbreviation = abbreviation
        self.country = country
        self.championship_editions = []

    def __str__(self) -> str:
        return self.name

    def add_championship_edition(self, championship_edition):
        self.championship_editions.append(championship_edition)


class ChampionshipEditionTeamStatus:
    current_id = 0

    def __init__(self, team, championship_edition):
        # Unique ID
        self.id = ChampionshipEditionTeamStatus.current_id
        ChampionshipEditionTeamStatus.current_id += 1

        self.team = team
        self.championship_edition = championship_edition

        """ Status parameters (initially randomly generated) """
        self.parameters = [
            self.Parameter("Team History", 0.5),
            self.Parameter("Rival Team History", 1.5),
            self.Parameter("Team Championship Edition Current Strength", 4),
            self.Parameter(
                "Rival Team Championship Edition Current Strength", 3.5),
            self.Parameter("Upcoming Match Importance", 3)
        ]

    def current_match_win_probability(self):
        return sum(parameter.value * parameter.weight for parameter in self.parameters) / sum(parameter.weight for parameter in self.parameters)

    class Parameter:
        current_id = 0

        def __init__(self, label, weight, positiveness_value=random.random()):
            # Unique ID
            self.id = ChampionshipEditionTeamStatus.Parameter.current_id
            ChampionshipEditionTeamStatus.Parameter.current_id += 1

            self.label = label
            self.weight = weight
            self.positiveness_value = positiveness_value
