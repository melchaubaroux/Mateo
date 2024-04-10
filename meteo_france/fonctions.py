from meteofrance_api import MeteoFranceClient , model
import requests

client = MeteoFranceClient()

def position_forecast(long,lat):

    location_forecast = client.get_forecast(long, lat)
    location_forecast.daily_forecast
    return location_forecast.daily_forecast


def city_forecast(city):

    list_places = client.search_places(city)
    my_place = list_places[0]
    my_place_weather_forecast = client.get_forecast_for_place(my_place)
    return (my_place_weather_forecast.daily_forecast)



def get_france_city():

    response=requests.get("https://www.data.gouv.fr/fr/datasets/r/521fe6f9-0f7f-4684-bb3f-7d3d88c581bb")
    return response.json()["cities"]


def get_france_fc(cities): 

    for city in cities : 
        yield city["city_code"],position_forecast(city["longitude"],city["latitude"])
        

