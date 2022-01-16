import requests
import smtplib
import wikipedia

import pywhatkit as kit

from decouple import config

def get_ip() -> str:
    """
    Returns the current IP address
    """
    return requests.get("https://api.ipify.org").text

print(get_ip())