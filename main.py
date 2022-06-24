#!/usr/bin/env python3

from re import I
import string
from urllib import response
import requests
import os

email = os.getenv("EMAIL")
root_url = os.getenv("ROOT_URL")

def make_get_request(url: str, get: str):
    try:
        response = requests.get(url=url)
        response.raise_for_status()
        return response.json()[get]
    except requests.exceptions.HTTPError as errh:
        print("Http Error: ", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting: ", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error: ", errt)
    except requests.exceptions.RequestException as e:
        print("An error has occurred ", e)


def make_post_request(url: str, data: dict, get: str):
    try:
        response = requests.post(url=url, data=data)
        response.raise_for_status()
        return response.json()[get]
    except requests.exceptions.HTTPError as errh:
        print("Http Error: ", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting: ", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error: ", errt)
    except requests.exceptions.RequestException as e:
        print("An error has occurred ", e)

def get_token(url: str) -> str:
    return make_get_request(url=url, get="token")

def get_blocks(url: str) -> str:
    return make_get_request(url=url, get="data")

def is_continuous(url: str, _from: str, to: str) -> bool:
    return make_post_request(
        url=url, 
        data={
        "blocks": [_from, to]
        }, 
        get="message"
    )

def validate_result(url: str, encoded: str) -> bool:
    return make_post_request(
        url=url,
        data={
        "encoded": encoded
        },
        get="message"
    )

def generate_full_string_encoded(url: str, blocks: list[str], encoded: str, first: str, index: int) -> str:
    print("==============================================")
    print(f"generate_full_string_encoded: - index {index}")
    print(f"blocks: {blocks}")
    print(f"encoded: {encoded}")
    print(f"first: {first}")
    print("==============================================")
    while(len(blocks) != 0):
        if is_continuous(url=url, _from= first, to=blocks[index]):
            first = blocks[index]
            blocks.pop(index)
            index = 0
            return generate_full_string_encoded(url=url, blocks=blocks, encoded=encoded+first, first=first, index=index)
        else:
            index = index + 1
    return encoded

def check(blocks: list[str], url: str) -> list[str]:
    first: str = blocks[0]
    print("check: first ", first)
    index: int = 0
    print("check: index ", index)
    new_blocks: list[str] = blocks[1:]
    print("check: new_blocks ", new_blocks)
    return(generate_full_string_encoded(url=url, blocks=new_blocks, encoded=first, first=first, index=index))

def run() -> bool:
    ### Get Token
    token = get_token(url=f"{root_url}/token?email={email}")

    ### Get blocks
    blocks = get_blocks(f"{root_url}/blocks?token={token}")

    ### Check if 2 blocks are continuos
    check_url = f"{root_url}/check?token={token}"

    result = check(blocks=blocks, url=check_url)
    print(result)

    ### Verify if all the strings are sorted
    return validate_result(url=check_url, encoded=result)

if __name__ == "__main__":
    print(run())

