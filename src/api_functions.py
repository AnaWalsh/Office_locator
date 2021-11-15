from pymongo import MongoClient
import requests
from dotenv import load_dotenv
import os
import pandas as pd
import geopandas as gpd
from cartoframes.viz import Map, Layer, popup_element
from functools import reduce
import operator
import json
import re

def geocode(direccion):
    """
    This function returns the coordinates of a given address by making a request to the geocode API.
    Args: 
        direccion
    Returns:
        coordinates
    """
    data = requests.get(f"https://geocode.xyz/{direccion}?json=1").json()
    try:
        return {"type": "Point", "coordinates": [data["latt"], data["longt"]]}
    except:
        return data

def getFromDict(diccionario,mapa):
    return reduce(operator.getitem,mapa,diccionario)



def extraetodo(json):
    """
    This function extracts from a given json the specified data. 
    Args:
        json
    Returns:
        list of dictionaries
    """
    todo = {"nombre": ["name"], "latitud": ["location", "lat"], "longitud": ["location", "lng"]} 
    total = []
    for elemento in json:
        place = {key: getFromDict(elemento, value) for key,value in todo.items()}
        place["location"] = type_point([place["latitud"], place["longitud"]])
        total.append(place)
    return total

def type_point(lista):
    """

    """
    return {"type":"Point", "coordinates": lista}

def find_places(place,city):
    """
    This function stores a dictionary the data of places in a city obtained trough the foursquare API.
    Args:
        place, city
    Returns:
        dictionary
    """
    url_query = 'https://api.foursquare.com/v2/venues/search'
    url_recomendados = 'https://api.foursquare.com/v2/venues/explore'
    client_id = os.getenv("tok1") # Variables para getenv token
    client_secret = os.getenv("tok2")
    parametros = {
        "client_id": client_id,
        "client_secret": client_secret,
        "v": "20180323",
        "ll": f"{city['coordinates'][0]}, {city['coordinates'][1]}", #aquí pongo la ciudad que quiero
        "query": f"{place}" #aquí pongo lo que quiero buscar en la ciudad.
    }
    resp = requests.get(url_query, params = parametros).json()
    map_ = ["location", "lat"]
    getFromDict(resp["response"]["venues"][0], map_)
    resp["response"]["venues"][0]["location"]["address"]
    loquebusco = resp["response"]["venues"]
    return extraetodo(loquebusco)

def build_df(lovemosclaro:dict):
    """
    This function builds a DataFrame from a given dictionary.
    Args:
        dictionary
    Returns:
        DataFrame
    """
    return pd.DataFrame(lovemosclaro)

def build_json(place,city,lovemosclaro:dict):
    """
    This function exports a given json and it names it with its corresponding place and city.
    Args:
        place, city, dictionary
    """
    json_name = f'{place}_{city}.json'    
    with open (json_name,"w") as f: # creamos un archivo vacío en el que vamos a escribir
        json.dump(lovemosclaro,f) # cargamos nuestra lista de diccionarios en ese archivo

def build_final_dictionary(city_dictionary, city_name:str, coordinates, database, distance):
    """
    This function adds elements to a dictionary from queries made for specified cities.
    The dictionary contains the total number of stations, starbucks and pet hairdressers for
    each city and the quality of the city based on a score defined by myself. OLÉ YO!!

    Args:
    city_diccionary, city_name, coordinates, database, distance

    Return:
    citi_dictionary
    """
    if city_name == "Madrid":
        city_dictionary[city_name] = build_madrid_dictionary_list(coordinates, database, distance)
    if city_name == "Sevilla":
        city_dictionary[city_name] = build_sevilla_dictionary_list(coordinates, database, distance)
    if city_name == "Barcelona":
        city_dictionary[city_name] = build_barcelona_dictionary_list(coordinates, database, distance)
   
    return city_dictionary


def build_madrid_dictionary_list(coordinate, database, distance):
    """
    This function makes queries for stations, starbucks and pet hairdressers in a city and it stores
    the results in a list. 
    (There is a function for each city because the query that have been made to look for the same type 
    of place had to be different)

    Args:
    coordinate, database, distance

    Return:
    list
    """
    
    places_count = []

    query_station = {"location": {"$near": {"$geometry": coordinate, "$maxDistance": distance}},
        'nombre': re.compile("cerc", re.IGNORECASE)}
    query_starbucks = {"location": {"$near": {"$geometry": coordinate, "$maxDistance": distance}},
        'nombre': re.compile("Starbu", re.IGNORECASE)}
    query_doggy = {"location": {"$near": {"$geometry": coordinate, "$maxDistance": distance}},
        'nombre': re.compile("canin", re.IGNORECASE)}
    query_vegan = {"location": {"$near": {"$geometry": coordinate, "$maxDistance": distance}},
        'nombre': re.compile("vegan", re.IGNORECASE)}

    station_lenght = len(list(database.find(query_station)))
    places_count.append(station_lenght)
    
    starbucks_lenght = len(list(database.find(query_starbucks)))
    places_count.append(starbucks_lenght)

    pets_lenght = len(list(database.find(query_doggy)))
    places_count.append(pets_lenght)

    vegan_length = len(list(database.find(query_vegan)))
    places_count.append(vegan_length)

    #Añadimos como ultimo elemento de la lista la suma de la cantidad de elementos por su valor
    places_count.append(station_lenght*3 + starbucks_lenght*2 + pets_lenght*1 + vegan_length*3)

    return places_count



def build_sevilla_dictionary_list(coordinate, database, distance):
    """
    This function makes queries for stations, starbucks and pet hairdressers in a city and it stores
    the results in a list. 
    (There is a function for each city because the queries that have been made to look for the same type 
    of place needed to be different)

    Args:
    coordinate, database, distance

    Return:
    list
    """
    
    places_count = []

    query_station = {"location": {"$near": {"$geometry": coordinate, "$maxDistance": distance}},
        'nombre': re.compile("renfe", re.IGNORECASE)}
    query_starbucks = {"location": {"$near": {"$geometry": coordinate, "$maxDistance": distance}},
        'nombre': re.compile("Starbu", re.IGNORECASE)}
    query_doggy = {"location": {"$near": {"$geometry": coordinate, "$maxDistance": distance}},
        'nombre': re.compile("Pet", re.IGNORECASE)}
    query_vegan = {"location": {"$near": {"$geometry": coordinate, "$maxDistance": distance}},
        'nombre': re.compile("vegan", re.IGNORECASE)}

    station_lenght = len(list(database.find(query_station)))
    places_count.append(station_lenght)
    
    starbucks_lenght = len(list(database.find(query_starbucks)))
    places_count.append(starbucks_lenght)

    pets_lenght = len(list(database.find(query_doggy)))
    places_count.append(pets_lenght)

    vegan_length = len(list(database.find(query_vegan)))
    places_count.append(vegan_length)

    #Añadimos como ultimo elemento de la lista la suma de la cantidad de elementos por su valor
    places_count.append(station_lenght*3 + starbucks_lenght*2 + pets_lenght*1 + vegan_length*3)

    return places_count



def build_barcelona_dictionary_list(coordinate, database, distance):
    """
    This function makes queries for stations, starbucks and pet hairdressers in a city and it stores
    the results in a list. 
    (There is a function for each city because the query that have been made to look for the same type 
    of place had to be different)

    Args:
    coordinate, database, distance

    Return:
    list
    """

    places_count = []

    query_station = {"location": {"$near": {"$geometry": coordinate, "$maxDistance": distance}},
        'nombre': re.compile("renfe", re.IGNORECASE)}
    query_starbucks = {"location": {"$near": {"$geometry": coordinate, "$maxDistance": distance}},
        'nombre': re.compile("Starbu", re.IGNORECASE)}
    query_doggy = {"location": {"$near": {"$geometry": coordinate, "$maxDistance": distance}},
        'nombre': re.compile("canin", re.IGNORECASE)}
    query_vegan = {"location": {"$near": {"$geometry": coordinate, "$maxDistance": distance}},
        'nombre': re.compile("vegan", re.IGNORECASE)}

    station_lenght = len(list(database.find(query_station)))
    places_count.append(station_lenght)
    
    starbucks_lenght = len(list(database.find(query_starbucks)))
    places_count.append(starbucks_lenght)

    pets_lenght = len(list(database.find(query_doggy)))
    places_count.append(pets_lenght)

    vegan_length = len(list(database.find(query_vegan)))
    places_count.append(vegan_length)

    #Añadimos como ultimo elemento de la lista la suma de la cantidad de elementos por su valor
    places_count.append(station_lenght*3 + starbucks_lenght*2 + pets_lenght*1 + vegan_length*3)

    return places_count





