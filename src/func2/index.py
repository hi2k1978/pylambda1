#!/usr/bin/python3

from modules.token import Token

def handler(event, context):
    print("func2: handler is called")
    print(f"func2: {event=}, {context=}")
    return Token.encode()

