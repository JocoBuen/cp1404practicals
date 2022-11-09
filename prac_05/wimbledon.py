"""
Wimbledon
Estimate: 90 minutes
Actual:   105 minutes
"""
FILENAME = "wimbledon.csv"


def main():
    records = get_records(FILENAME)
    print(records)
    champion_to_count = count_the_champions(records)
    countries = get_the_country_of_champions(records)
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")
    print(f"\nThese {len(countries)} have won Wimbledon:")
    for country in countries:
        print(country, end=", ")


def get_the_country_of_champions(records):
    countries = set()
    for record in records:
        countries.add(record[1])
    return countries


def count_the_champions(records):
    champion_to_count = {}
    for record in records:
        count = champion_to_count.get(record[2], 0)
        champion_to_count[record[2]] = count + 1
    return champion_to_count


def get_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as input_file:
        input_file.readline()
        for line in input_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
