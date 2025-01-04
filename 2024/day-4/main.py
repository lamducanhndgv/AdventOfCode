import os
import re

import requests

from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

def get_input():
    data_link = "https://adventofcode.com/2024/day/4/input"
    response = requests.get(
        data_link,
        cookies={"session": os.environ.get("COOKIE_SESSION")}
    )
    response.raise_for_status()

    # Parse data    
    data = response.content.decode("utf-8").strip()
    data = data.split("\n")
    
    return data

def count_xmas_string(input_data, r, c, m, n):
    """
    Find the number of Xmas strings in 8 directions
    """
    pattern = "MAS"
    directions = [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
    
    count = 0
    for dr, dc in directions:
        c_index = 0 
        new_r, new_c = r, c
        while c_index < len(pattern):
            new_r = new_r + dr
            new_c = new_c + dc
            if 0 <= new_r < m and 0 <= new_c < n:
                if input_data[new_r][new_c] == pattern[c_index]:
                    c_index += 1
                else:
                    break
            else:
                break
        if c_index == len(pattern):
            count += 1
    
    return count

def solution():
    input_data = get_input()
    m, n = len(input_data), len(input_data[0])
    
    total = 0
    for r in range(m):
        for c in range(n):
            if input_data[r][c] == 'X':
                total += count_xmas_string(input_data, r, c, m, n)
    print(total)
    
    
if __name__ == "__main__":
    solution()