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
    kit.search(query, option="web")

