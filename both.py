import argparse
import os

import load
import plot

p = argparse.ArgumentParser()
p.add_argument("cities", nargs="*", help="list of cities to plot")
p.add_argument("--destructive", "--delete", "-d",
               action="store_true", dest="destructive", help="delete files after plotting them")
p.add_argument("--no-pressure", "-np", dest="pressure", action="store_false",
               help="do not plot pressure data")
p.add_argument("--no-humidity", "-nh", dest="humidity",
               action="store_false", help="do not plot humidity data")
args = p.parse_args()

categories = ["temp", "feels_like"]

if args.pressure:
    categories.append("pressure")
if args.humidity:
    categories.append("humidity")
load.get_weather(args.cities)
plot.main(categories)
if args.destructive:
    for f in os.listdir("data/"):
        os.remove("data/" + f)
