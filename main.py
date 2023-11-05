import json
from typing import List

def findPokemon(list: List[str], firstLetter: str) -> str | None:
  for pokemon in list:
    if pokemon[0] == firstLetter:
      return pokemon
  return None

def getPokedex() -> List[str]:
  with open('./pokedex-data/pokedex.json', 'r') as json_file:
    pokedex: List[str] = json.load(json_file)
  pokedex.sort()
  return pokedex

def buildChain(pokedex: List[str]):
  currentPokemon: str | None = pokedex[0]
  pokechain = []
  while currentPokemon != None:
    pokechain.append(currentPokemon)
    pokedex.remove(currentPokemon)
    currentPokemon = findPokemon(pokedex, currentPokemon[-1])
  return pokechain

def printOutput(pokechain: list):
  print('complete - total chain length is {} '.format(len(pokechain)))
  should_show_list:str = input('Would you like to see the chain?: ')
  if should_show_list.lower() == 'y' or should_show_list.lower() == 'yes':
    print('list is {}'.format(pokechain))

def main():
  pokedex = getPokedex()
  pokechain = buildChain(pokedex)
  printOutput(pokechain)

main()

