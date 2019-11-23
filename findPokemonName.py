import json
from fuzzywuzzy import fuzz
# pokemonNamesListJSON = json.load('pokemonNames.json')
# print(pokemonNamesListJSON)
pokemonNameJSONconvertedToList = []
with open('pokemonNames.json','r') as pokemonNamesList:
	pokemonData = json.load(pokemonNamesList)
	# print(pokemonData['pokemon'])
for name in pokemonData['pokemon']:
	pokemonNameJSONconvertedToList.append(name)
# print(pokemonNameJSONconvertedToList)

def findClosestPokemon(nameGivenByUser):
	indexWithLargestRatio = "Pikachu"
	ratioOfCurrentBestMatch = 0
	for name in pokemonNameJSONconvertedToList:
		if(fuzz.ratio(name,nameGivenByUser)>ratioOfCurrentBestMatch):
			ratioOfCurrentBestMatch = fuzz.ratio(name,nameGivenByUser)
			indexWithLargestRatio = name
	return indexWithLargestRatio

if __name__ == "__main__":
	nameGivenByUser = input("Enter any word and we'll try to find the closest pokemon name to that word\n")
	nameFoundByFuzzyMatching = findClosestPokemon(nameGivenByUser)
	print(nameFoundByFuzzyMatching)