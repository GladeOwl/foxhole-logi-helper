""" Glade's Foxhole Logistic Helper Script """

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import json
import orders

# NOTE: Make it able to do the orders in Phases.

with open("./data/data.json", "r", encoding="utf-8") as dataFile:
    data = json.load(dataFile)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('index.html', context={ "request" : request, "data" : data })

@app.get("/getData",)
async def root():
    return data