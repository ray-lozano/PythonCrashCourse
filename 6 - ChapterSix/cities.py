cities = {
    'tokyo': {'country': 'japan', 'population': 9_733_000}, 
    'new york city': {'country': 'usa', 'population': 8_258_000}, 
    'seoul': {'country': 'south korea', 'population': 9_411_000}}


for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    country = f"{city_info['country']}"
    population = f"{city_info['population']}"

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")