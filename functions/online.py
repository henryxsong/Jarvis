import json
import requests
import smtplib
import wikipedia

import pywhatkit as kit

from decouple import config

def get_ip():
    """
    Returns the current IP address
    """
    return requests.get("https://api.ipify.org").json()["ip"]

def wiki_lookup(query:str) -> str:
    """
    Looks up a query on Wikipedia and returns the first paragraph
    """
    return wikipedia.summary(query, sentences=3)

def google_it(query:str):
    """
    Searches Google for a query and returns the first result
    """
    kit.search(query)

def youtube_it(query:str):
    """
    Searches YouTube for a query and returns the first result
    """
    kit.playonyt(query)

def get_weather(query:str) -> str:
    """
    Returns the weather for a given location
    """
    WEATHER_API_KEY = config('WEATHER_API_KEY')
    result = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={query}&appid={WEATHER_API_KEY}&units=imperial").json()
    condition = result["weather"][0]["description"]
    temp = result["main"]["temp"]
    return f"The weather in {query} is {condition} with a temperature of {temp} degrees Ferenheit."

def get_joke() -> str:
    """
    Returns a random joke from the Chuck Norris API
    """
    result = requests.get("https://icanhazdadjoke.com/", headers={'Accept': 'application/json'}).json()
    return result["joke"]


google_it("google")
print(get_joke())
youtube_it("rick roll")
print(get_ip())