import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("countries-data.json")


def _load_countries(countries=None):
    if countries is not None:
        return countries

    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def most_spoken_languages(countries=None, n=10, limit=None):
    """Return the most widely spoken languages as (language, country count)."""
    if isinstance(countries, int):
        countries, n = None, countries
    if limit is not None:
        n = limit

    if n not in (10, 20):
        raise ValueError("n must be 10 or 20")

    counts = {}
    for country in _load_countries(countries):
        languages = country.get("languages", {})
        if isinstance(languages, dict):
            language_names = languages.values()
        else:
            language_names = languages

        for language in set(language_names):
            counts[language] = counts.get(language, 0) + 1

    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:n]


def most_populated_countries(countries=None, n=10, limit=None):
    """Return the most populated countries as (country name, population)."""
    if isinstance(countries, int):
        countries, n = None, countries
    if limit is not None:
        n = limit

    if n not in (10, 20):
        raise ValueError("n must be 10 or 20")

    countries = _load_countries(countries)
    population_data = [
        (country["name"], country["population"])
        for country in countries
    ]
    return sorted(population_data, key=lambda item: item[1], reverse=True)[:n]


print("Most spoken languages:")
for language, country_count in most_spoken_languages(n=10):
    print(language, country_count)

print("\nMost populated countries:")
for country, population in most_populated_countries(n=10):
    print(country, population)