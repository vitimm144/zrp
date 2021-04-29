from django.shortcuts import render
from django.http import JsonResponse
import requests
from pprint import pprint
from operator import itemgetter


def get(url) -> dict:
    data = {}
    result = requests.get(url)
    if result:
        data = result.json()
    return data

def get_pokemon_info(pokemon_name: str) -> dict:
    poke_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    pokemon = get(poke_url)
    return pokemon

def get_pokemon_ability_description(url: str) -> dict:
    description = ''
    result = get(url) 
    for item in result.get("effect_entries"):
        if item.get("language").get("name") == "en":
            description = item.get("effect")
    return description
    
def process_pokemon_info(pokemon_info) -> list:
    data = {}
    abilities = pokemon_info.get("abilities")
    for ability in abilities:
        pprint(ability)
        ab = ability.get("ability")
        data[ab.get("name")] = get_pokemon_ability_description(ab.get("url"))

    return dict(sorted(data.items(), key=itemgetter(0)))

def poke_api_view(request):
    if request.method == "GET":
        pprint(request.GET)
        poke_name = request.GET.get("name")
        if poke_name:
            result = get_pokemon_info(poke_name)
            habilities = process_pokemon_info(result)

            return JsonResponse(habilities)

