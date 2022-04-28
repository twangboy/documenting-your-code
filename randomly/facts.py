import requests
from requests.exceptions import RequestException


def generate_random_fact(output_format: str, language: str) -> str:
    """
    Generates a random fact from uselessfacts.jsph.pl

    Args:
        output_format (str): The output format of the fact. Must be one of [html, json, txt, md]
        language (str): The language for the random fact. Must be one of [en, de]

    Returns:
        str: json or text containing the random fact
    """
    # Validate the language
    if language not in {"en", "de"}:
        raise ValueError(f"{language} is not supported.")

    # Validate the output format
    if output_format not in {"html", "json", "txt", "md"}:
        raise ValueError(f"{output_format} is not supported.")

    # Get the random fact from the web
    response = requests.get(
        f"https://uselessfacts.jsph.pl/random.{output_format}?language={language}"
    )

    # If successful, get the output
    if response.status_code == 200:
        if output_format == "json":
            fact = response.json()
        else:
            fact = response.text
    else:
        raise RequestException(
            f"Something went wrong. Request returned status {response.status_code}."
        )

    return fact
