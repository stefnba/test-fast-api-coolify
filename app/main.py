from typing import Union

import os
from fastapi import FastAPI

app = FastAPI()


test = os.getenv("TEST", "World")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/env")
def read_env():
    return {"env": test}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
