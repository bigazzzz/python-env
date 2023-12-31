#!/usr/bin/env python3

import os
import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, JSONResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
current_directory = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(current_directory + "/templates")
prefix = os.environ.get('PYTHONENV_ROOT_PATH')
if prefix is None:
    prefix = ""

@app.get(prefix + "/", response_class=PlainTextResponse)
async def index(request: Request):
    return templates.TemplateResponse("array.html.j2", {"request": request, "envs": get_env_array()})

@app.get(prefix + "/all", response_class=JSONResponse)
async def get_all_env(request: Request):
    return JSONResponse(get_env_array())

@app.get(prefix + "/hostname", response_class=PlainTextResponse)
async def get_hostname(request: Request):
    return PlainTextResponse(os.uname().nodename)

@app.get(prefix + "/env/{env}", response_class=PlainTextResponse)
async def get_env(request: Request, env:str):
    return PlainTextResponse(str(os.environ[env]))

def get_env_array():
    envs = dict()
    for env in os.environ:
        envs[str(env)] = str(os.environ[env])
    return envs

if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, log_level="info", reload=True)
