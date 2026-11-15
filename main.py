import requests


def fetch_pokemon(name):
    try:
        response = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{name}/", timeout=15
        )
        if response.status_code == 404:
            print("Pokemon not found. Please check the English name.")
            return None
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("The request timed out. Please try again.")
        return None
    except requests.exceptions.RequestException:
        print("Could not get data. Check your internet connection and try again.")
        return None
    except ValueError:
        print("The API did not return valid JSON data.")
        return None


def process_pokemon(data):
    types = []
    for item in data.get("types", []):
         types.append(item.get("type", {}).get("name", "unknown"))

    hp = None
    for item in data.get("stats", []):
        if item.get("stat", {}).get("name") == "hp":
            hp = item.get("base_stat")

    pokemon = {"name": data.get("name", "unknown"), "types": types, "hp": hp}
    return [pokemon]


def display_pokemon(pokemon_list):
    for pokemon in pokemon_list:
        print("\nName:", pokemon["name"])
        print("Types:", ", ".join(pokemon["types"]))
        print("HP:", pokemon["hp"])


def main():
    name = input("Enter a Pokemon's English name (for example, pikachu): ").strip().lower()
    if not name:
        print("Please enter a Pokemon name.")
        return

    data = fetch_pokemon(name)
    if data is not None:
        pokemon_list = process_pokemon(data)
        display_pokemon(pokemon_list)


if __name__ == "__main__":
    main()
