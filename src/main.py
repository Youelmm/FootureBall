import championship
import country
import team

country = country.Country("Listenbourg")
teams = [team.Team(f"Team {i}", f"T{i}", country) for i in range(1, 21)]
championship_ = championship.Championship("Python League", 20, country)
championship_edition = championship.ChampionshipEdition(
    championship_, "2022/2023", teams)

print(championship_edition)
