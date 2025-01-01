import os
import re

import requests

from functools import reduce

from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

def get_input():
    data_link = "https://adventofcode.com/2024/day/1/input"
    response = requests.get(
        data_link,
        cookies={"session": os.environ.get("COOKIE_SESSION")}
    )
    response.raise_for_status()
    
    data = response.content.decode("utf-8").strip()
    data = data.split("\n")
    data = [list(map(int, re.split(r"\s+", row))) for row in data]
    return data

def main():
    input_data = get_input()
    left_data, right_data = zip(*input_data)
    result = reduce(lambda res, x: res + abs(x[0] - x[1]), zip(sorted(left_data), sorted(right_data)), 0)
    print(result)
    
if __name__ == "__main__":
    main()