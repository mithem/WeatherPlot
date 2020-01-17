import argparse

import requests

API_KEY = "3a1fcf20bd2c469656a9ab0e1c686428"


def get_weather(cities):
    for c in cities:
        r = requests.get(
            "https://api.openweathermap.org/data/2.5/forecast?q=" + c + "&APPID=" + API_KEY)
        with open("data/" + c + ".json", "w") as f:
            f.write(str(r.content, "utf-8"))


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Get the forecast for a city and save it")
    p.add_argument("cities", nargs="*",
                   help="The city 'code' as passed to openweathermap.org")
    args = p.parse_args()
    get_weather(args.cities)
