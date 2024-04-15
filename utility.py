import requests
from typing import Dict

API_KEY = "2wubG+f3rTK+ElC0Nwmb4w==YK0iGR3pcTfZx5Jd"

QuoteType = Dict[str, str]


def get_random_quote(category="") -> QuoteType:
    api_url = "https://api.api-ninjas.com/v1/quotes?category={}".format(category)
    response = requests.get(api_url, headers={"X-Api-Key": API_KEY})  # type: ignore
    if response.status_code == requests.codes.ok:
        return response.json()[0]
    else:
        raise Exception("Error:", response.status_code, response.text)


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
