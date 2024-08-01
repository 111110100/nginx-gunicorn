#!/usr/bin/env python3

import os
from bottle import Bottle
from dotenv import load_dotenv

app = Bottle()

@app.get("/ping")
def ping() -> dict:
    return {
        "message": "pong"
    }

if __name__ == "__main__":
    load_dotenv()
    BJOERN_ENABLED: bool = os.getenv("BJOERN", "F")[0].upper() in ["T", "Y", "1"]
    if BJOERN_ENABLED:
        app.run(
                server = "bjoern",
                host = "0.0.0.0",
                port = 8080,
                debug = True
        )
    else:
        app.run(
                host = "0.0.0.0",
                port = 8080,
                debug = True,
                reloader = True
        )
