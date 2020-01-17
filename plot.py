import json
import math
import os
import argparse

import matplotlib.pyplot as plt


def main(categories):
    files = os.listdir("data/")
    for f in files:
        if f == ".DS_Store" or f[-5:] != ".json":
            continue
        with open("data/" + f, "r") as file:
            data = json.loads(file.read())
        mydata = {}
        for i in categories:
            mydata[i] = []
        for c in mydata:
            for timestamp in data.get("list"):
                if c != "temp" and c != "feels_like":
                    value = timestamp.get("main").get(c)
                else:
                    value = timestamp.get("main").get(c) - 273.15
                mydata[c].append(value)
        plt.subplot(len(files) * 100 + 11 + files.index(f))
        for c in mydata:
            plt.plot(mydata.get(c), label=c)
        plt.legend()
    plt.show()


if __name__ == "__main__":
    categories = ["temp", "feels_like"]
    p = argparse.ArgumentParser()
    p.add_argument("--no-pressure", "-np", dest="pressure", action="store_false",
                   help="do not plot pressure data")
    p.add_argument("--no-humidity", "-nh", dest="humidity",
                   action="store_false", help="do not plot humidity data")
    args = p.parse_args()
    if args.pressure:
        categories.append("pressure")
    if args.humidity:
        categories.append("humidity")
    main(categories)
