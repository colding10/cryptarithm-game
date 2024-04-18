"""This module defines utility functions for generating the cryptarithms"""

import random
from string import ascii_uppercase

import requests

# don't steal my api key please its free anyways :)
API_KEY = "2wubG+f3rTK+ElC0Nwmb4w==YK0iGR3pcTfZx5Jd"

QuoteType = dict[str, str]


def get_random_quote(category="") -> QuoteType:
    """Uses the api-ninjas api to get a random quote"""
    api_url = f"https://api.api-ninjas.com/v1/quotes?category={category}"
    response = requests.get(api_url, headers={"X-Api-Key": API_KEY}, timeout=200)

    if response.status_code == 200:
        return response.json()[0]
    raise requests.HTTPError("Error:", response.status_code, response.text)


def get_quote_max_length(max_length=1000) -> QuoteType:
    """get a quote with an maximum length using Api-Ninjas"""
    while True:
        quote = get_random_quote()
        if len(quote["quote"]) <= max_length:
            return quote


def create_alphabet_mapping() -> dict[str, str]:
    """Creates an alphabet-mapping where no character can map to itself"""
    letters = list(ascii_uppercase)
    random.shuffle(letters)
    mapping = {}
    for i, _ in enumerate(letters):
        next_index = (i + 1) % 26
        if letters[next_index] == chr(65 + i):
            letters[next_index], letters[(i + 2) % 26] = (
                letters[(i + 2) % 26],
                letters[next_index],
            )
        mapping[chr(65 + i)] = letters[next_index]
    return mapping
