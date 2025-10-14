"""
Wimbledon
Estimate: 10 minutes
Actual:   12 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    champion_to_wins = {}
    champions_and_countries = unpack_champion_and_country(FILENAME)
    countries = set((pair[0] for pair in champions_and_countries))
    for country, champion in champions_and_countries:
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    display_output(champion_to_wins, countries)


def unpack_champion_and_country(filename):
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        return [line.strip().split(",")[1:3] for line in in_file.readlines()[1:]]


def display_output(champion_to_wins, countries):
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion} {wins}")
    print("\nThese 12 countries have won Wimledon: ")
    print(", ".join(sorted(countries)))


main()
