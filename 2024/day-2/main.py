import os
import re

import requests

from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

def get_input():
    data_link = "https://adventofcode.com/2024/day/2/input"
    response = requests.get(
        data_link,
        cookies={"session": os.environ.get("COOKIE_SESSION")}
    )
    response.raise_for_status()
    
    data = response.content.decode("utf-8").strip()
    data = data.split("\n")
    data = [list(map(int, re.split(r"\s+", row))) for row in data]
    return data

def is_safe_report(levels: list[int]):
    direction = 0
    for index, level in enumerate(levels):
        if index == len(levels) - 1:
            return True
        difference = levels[index + 1] - level
        if direction * difference < 0:
            return False
        if not (1 <= abs(difference) <= 3):
            return False
        direction = 1 if levels[index + 1] - level > 0 else -1
    return True

def solution():
    print([
        is_safe_report(report)
        for report in [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9]
        ]
    ])
    
    result = 0
    for report in get_input():
        if is_safe_report(report):
            result += 1
    print(result)
    
if __name__ == "__main__":
    solution()