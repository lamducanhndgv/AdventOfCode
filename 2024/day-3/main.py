import os
import re

import requests

from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

def get_input():
    data_link = "https://adventofcode.com/2024/day/3/input"
    response = requests.get(
        data_link,
        cookies={"session": os.environ.get("COOKIE_SESSION")}
    )
    response.raise_for_status()

    # Parse data    
    data = response.content.decode("utf-8").strip()
    
    return data

def solution():
    input_data = get_input()
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    
    total = 0
    for match in pattern.finditer(input_data):
        left, right = list(map(int, match.groups()))
        total += left * right
    print(total)
    
    
if __name__ == "__main__":
    solution()