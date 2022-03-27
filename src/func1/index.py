#!/usr/bin/python3

from modules.token import Token

def handler(event, context):
    print("func1: handler is called")
    print(f"func1: {event=}, {context=}")
    return Token.encode()

