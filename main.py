#!/usr/bin/env python3

import sys
import requests
import os
from icecream import ic

def check_env_variables():
    ic()
    if not all(elem in os.environ for elem in ["EMAIL", "ROOT_URL"]):
        print("Please setup environment variable EMAIL and ROOT_URL.")
        sys.exit(1)


EMAIL = os.getenv("EMAIL")
ROOT_URL = os.getenv("ROOT_URL")

def http_error_decorator(function):
    def wrapper(*args, **kwargs):
        try:
            func = function(*args, **kwargs)
            return func
        except requests.exceptions.HTTPError as errh:
            print("Http Error: ", errh)
            raise Exception("Http Error: ", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting: ", errc)
            raise Exception("Error Connecting: ", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error: ", errt)
            raise("Timeout Error: ", errt)
        except requests.exceptions.RequestException as e:
            print("An error has occurred ", e)
            raise("An error has occurred ", e)
    return wrapper

@http_error_decorator
def make_get_request(url: str, get: str):
    ic()
    response = requests.get(url=url)
    response.raise_for_status()
    return response.json()[get]

@http_error_decorator
def make_post_request(url: str, data: dict, get: str):
    ic()
    response = requests.post(url=url, data=data)
    response.raise_for_status()
    return response.json()[get]

def get_token(url: str) -> str:
    ic()
    return make_get_request(url=url, get="token")

def get_blocks(url: str) -> str:
    ic()
    return make_get_request(url=url, get="data")

def is_continuous(url: str, _from: str, to: str) -> bool:
    ic()
    return make_post_request(
        url=url, 
        data={
        "blocks": [_from, to]
        }, 
        get="message"
    )

def validate_result(url: str, encoded: str) -> bool:
    ic()
    return make_post_request(
        url=url,
        data={
        "encoded": encoded
        },
        get="message"
    )

def generate_full_string_encoded(url: str, blocks: list[str], new_blocks: list[str], first: str, index: int) -> list[str]:
    ic(index, blocks, len(blocks), new_blocks, len(new_blocks), first)
    while(len(blocks) != 0):
        ic(index, url, first, blocks, blocks[index])
        if is_continuous(url=url, _from= first, to=blocks[index]):
            new_blocks.append(blocks[index])
            first = blocks[index]
            blocks.pop(index)
            index = 0
            return generate_full_string_encoded(url=url, blocks=blocks, new_blocks=new_blocks, first=first, index=index)
        else:
            index = index + 1
    return new_blocks

def check(blocks: list[str], token: str) -> list[str]:
    ic()
    if len(blocks) != 0:
        first: str = blocks[0]
        index: int = 0
        blocks: list[str] = blocks[1:]
        new_blocks: list[str] = [first]
        url = f"{ROOT_URL}/check?token={token}"
        return(generate_full_string_encoded(url=url, blocks=blocks, new_blocks=new_blocks, first=first, index=index)) 
    else:
        return blocks

def run() -> bool:
    ic()
    ### Get Token
    token = get_token(url=f"{ROOT_URL}/token?email={EMAIL}")

    ### Get blocks
    blocks = get_blocks(f"{ROOT_URL}/blocks?token={token}")

    ### Get sorted blocks
    sorted_blocks = check(blocks=blocks, token=token)
    ic(sorted_blocks)
    return sorted_blocks

if __name__ == "__main__":
    ic()
    check_env_variables()
    sorted_blocks = run()
    token = get_token(url=f"{ROOT_URL}/token?email={EMAIL}")
    ### Verify if all the strings are sorted
    is_valid = validate_result(url=f"{ROOT_URL}/check?token={token}", encoded="".join(sorted_blocks))
    ic(is_valid)
    if is_valid: ic("The blocks were sorted properly.")
    else: ic("The blocks weren't sorted properly.")