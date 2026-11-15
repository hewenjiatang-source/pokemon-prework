# Pokemon Lookup

Enter a Pokemon's English name to see its name, types, and HP. The data comes from [PokeAPI](https://pokeapi.co/docs/v2).

## API notes

Example request: [pikachu](https://pokeapi.co/api/v2/pokemon/pikachu/)

**Is the response a list or a dictionary?**

One Pokemon comes back as a dictionary. The code puts the processed dictionary into a list.

**What fields are there?**

There are fields like `name`, `id`, `height`, `weight`, `types`, `abilities`, and `stats`. This project uses `name`, `types`, and the HP entry in `stats`.

**Is anything nested?**

Yes. `types` is a list, and each item has a `type` dictionary with the type's name. `stats` is another list. To get HP, the program looks for the item where `stat.name` is `hp` and takes its `base_stat` value.

**Can data be missing or null?**

If a field is missing, .get() returns a default value instead of crashing. Some sprite image fields can be null if that image isn't available. This project doesn't use the images. 

## Project plan

The idea is a single Pokemon lookup. The user enters a name, and the program gets the data and prints the name, types, and HP on separate lines. It shows a message if the input is empty, the name isn't found, the request times out, or the request fails. Getting the data, picking out the fields, and printing them are handled in separate functions. The processed result is stored in a list of dictionaries.

## Run it

You need Python 3 and an internet connection. From the project folder:

```sh
python3 -m pip install -r requirements.txt
python3 main.py
```

If you're using a virtual environment, activate it first.

For example:

```text
Enter a Pokemon's English name (for example, pikachu): pikachu

Name: pikachu
Types: electric
HP: 35
```

If the name doesn't exist:

```text
Enter a Pokemon's English name (for example, pikachu): pikachuu
Pokemon not found. Please check the English name.
```

It does one lookup and then finishes. Run it again to try another name, like `bulbasaur`.
