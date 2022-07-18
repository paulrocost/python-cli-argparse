import requests
import json


BASE_URL = "https://date.nager.at/api/v3/"


def get_available_countries():
    resp = requests.get(f"{BASE_URL}AvailableCountries")
    if resp.status_code is 200:
        return json.loads(resp.content, encoding="utf-8")
    else:
        raise Exception(f"{resp.status_code} - Something happen to reach out the api")


def get_country_following_holidays(country_code):
    resp = requests.get(f"{BASE_URL}NextPublicHolidays/{country_code}")
    if resp.status_code is 200:
        return json.loads(resp.content, encoding="utf-8")[:5]
    else:
        raise Exception(f"{resp.status_code} - Something happen to reach out the api")
