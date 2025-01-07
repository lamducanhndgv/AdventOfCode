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
    
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_idx = 0
    
    steps = 0
    while True:
        dr, dc = direction[direction_idx]
        new_row = guard_pos[0] + dr
        new_col = guard_pos[1] + dc
        
        if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
            break
        
        if lab_map[new_row][new_col] == '#':
            direction_idx = (direction_idx + 1) % 4
            continue
    
if __name__ == "__main__":
    solution()