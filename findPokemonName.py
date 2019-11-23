from difflib import get_close_matches
import json

# pokemonNamesListJSON = json.load('pokemonNames.json')
# print(pokemonNamesListJSON)
pokemonNameJSONconvertedToList = []
with open('pokemonNames.json','r') as pokemonNamesList:
	pokemonData = json.load(pokemonNamesList)
	# print(pokemonData['pokemon'])
for name in pokemonData['pokemon']:
	pokemonNameJSONconvertedToList.append(name)
print(pokemonNameJSONconvertedToList)
# for name in pokemonNameJSONconvertedToList:
# 	print(name)
def findClosestPokemon(listOfPokemonNames,wordToFindClosestPokemonName):
	print(get_close_matches(wordToFindClosestPokemonName,listOfPokemonNames,cutoff=0))

# if __name__ == "__main__":
# 	nameGivenByUser = input("Enter any word and we'll try to find the closest pokemon name to that word\n")
# 	findClosestPokemon(nameGivenByUser,pokemonNameJSONconvertedToList)