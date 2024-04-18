from typing import Dict
from string import ascii_uppercase

import random
import requests

API_KEY = "2wubG+f3rTK+ElC0Nwmb4w==YK0iGR3pcTfZx5Jd"

QuoteType = Dict[str, str]


def get_random_quote(category="") -> QuoteType:
    api_url = f"https://api.api-ninjas.com/v1/quotes?category={category}"
    response = requests.get(api_url, headers={"X-Api-Key": API_KEY})  # type: ignore
    if response.status_code == requests.codes.ok:
        return response.json()[0]
    raise requests.HTTPError("Error:", response.status_code, response.text)


def get_quote_max_length(max_length=1000) -> QuoteType:
    """
    get a quote with an maximum length using Api-Ninjas

    Args:
        max_length (int, optional): the maximum length. Defaults to 1000.

    Returns:
        QuoteType: a dictionary with information about the quotes
    """
    while True:
        quote = get_random_quote()
        if len(quote["quote"]) <= max_length:
            return quote


def create_alphabet_mapping() -> Dict[str, str]:
    available = list(ascii_uppercase)
    mapping = {}

    for char in ascii_uppercase:
        add_back = False
        if char in available:
            available.remove(char)
            add_back = True

        chosen = random.choice(available)
        available.remove(chosen)
        mapping[char] = chosen

        if add_back:
            available.append(char)

    return mapping
