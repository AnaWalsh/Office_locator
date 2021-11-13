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









