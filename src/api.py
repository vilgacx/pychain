from uvicorn import run
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pychain import pyChain

instance = pyChain()

app = FastAPI()

@app.get("/")
def home():
    return instance.chain


@app.get("/add")
def mine(nonce:int,data:str):
    instance.Mine(nonce,data)
    return RedirectResponse(url='/')

if __name__ == "__main__":
    run("api:app", host="127.0.0.1", port=8000, reload=True)
