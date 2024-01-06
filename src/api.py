from uvicorn import run
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from sys import argv
from pychain import pyChain

HOST = "127.0.0.1"
PORT = int(argv[1])

peer = argv[2]

instance = pyChain(peer)
instance.NewNode(f'{HOST}:{PORT}')

app = FastAPI()

@app.get("/")
def home():
    instance.NodeUpdate()
    instance.Consensus()
    return RedirectResponse(url='/chain')

@app.get("/chain")
def chain():
    instance.Consensus()
    return instance.chain

@app.get("/current_chain")
def current_chain():
    return instance.chain

@app.get("/add")
def mine(nonce:int,data:str):
    instance.Mine(nonce,data)
    return RedirectResponse(url='/chain')

@app.get("/nodes")
def nodes():
    return instance.nodes

@app.get("/addnode")
def addnode(peer:str):
    instance.AddNode(peer)
    return { "status" : 200 }

if __name__ == "__main__":
    run("api:app", host=HOST, port=PORT, reload=True)
