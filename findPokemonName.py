from difflib import get_close_matches
import json

# pokemonNamesListJSON = json.load('pokemonNames.json')
# print(pokemonNamesListJSON)

with open('pokemonNames.json','r') as pokemonNamesList:
	pokemonData = json.load(pokemonNamesList)
	print(pokemonData)
# 	for name in pokemonNamesList['pokemon']:
# 		print(name)