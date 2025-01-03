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
    
    data = response.content.decode("utf-8").strip()
    
    # Parse data
    
    return data

def solution():
    ...
    
if __name__ == "__main__":
    solution()