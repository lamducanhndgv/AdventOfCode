import os
import re

from collections import defaultdict

import requests

from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

def get_input():
    data_link = "https://adventofcode.com/2024/day/8/input"
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
    ...
    
if __name__ == "__main__":
    solution()