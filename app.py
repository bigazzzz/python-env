#!/usr/bin/env python3

import os
import sys
import uvicorn

from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/", response_class=JSONResponse)
async def index(request: Request):
    return JSONResponse(sys.argv[1:])


@app.get("/all", response_class=JSONResponse)
async def index(request: Request):
    envs = []
    for env in os.environ:
        envs.append({"name": str(env), "value": str(os.environ[env])})

    return JSONResponse(envs)


@app.get("/env/{env}", response_class=JSONResponse)
async def get_env(request: Request, env:str):
    envs = { str(env): str(os.environ[env])}
    return JSONResponse(envs)

if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, log_level="info", reload=True)
