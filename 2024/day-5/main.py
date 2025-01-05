import os
import re

import requests

from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

def get_input():
    data_link = "https://adventofcode.com/2024/day/5/input"
    response = requests.get(
        data_link,
        cookies={"session": os.environ.get("COOKIE_SESSION")}
    )
    response.raise_for_status()

    # Parse data    
    data = response.content.decode("utf-8").strip()
    data = data.split("\n\n")
    
    data[0] = data[0].split("\n")
    data[1] = data[1].split("\n")
    
    return data

def is_valid(update, orders):
    number = len(update)
    for i in range(number):
        for j in range(0, i):
            if update[j] in orders and update[j] in orders[update[i]]:
                return False
    return True

def solution():
    rules, updates = get_input()
    
    result = 0
    
    orders = {}
    for rule in rules:
        before, after = list(map(int, rule.split('|')))
        if before not in orders:
            orders[before] = set()
        orders[before].add(after)
        
    for update in updates:
        update = list(map(int, update.split(',')))
        if is_valid(update, orders):
            result += update[len(update) // 2]
    
    print(result)
        
    
if __name__ == "__main__":
    solution()