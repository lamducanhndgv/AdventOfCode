import os
import re

from collections import defaultdict

import requests

from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

def get_input():
    data_link = "https://adventofcode.com/2024/day/6/input"
    response = requests.get(
        data_link,
        cookies={"session": os.environ.get("COOKIE_SESSION")}
    )
    response.raise_for_status()

    # Parse data    
    data = response.content.decode("utf-8").strip()
    
    data = data.split('\n')
    
    return data


def solution():
    lab_map = get_input()
    m, n = len(lab_map), len(lab_map[0])
    
    obstructions = {
        "row": defaultdict(set),
        "col": defaultdict(set)
    }
    guard_pos = None
    
    for i in range(m):
        for j in range(n):
            if lab_map[i][j] == '#':
                obstructions["row"][i].add(j)
                obstructions["col"][j].add(i)
            if lab_map[i][j] == '^':
                guard_pos = (i, j)
    
    print(obstructions)
    print(guard_pos)
                       
    
if __name__ == "__main__":
    solution()