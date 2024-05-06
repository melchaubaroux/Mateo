from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi import FastAPI, Request 
import json
import requests
import uvicorn

from config_local import * 
from fonctions import * 


connection_db()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


########################################### endpoints #############################################


# check connection
@app.get("/available_connection", response_class=HTMLResponse)
def test_connection():
    conn,cur=connection_db()

    return "True" if conn else "False"


# check existence of a table 
@app.get("/exist/{table}", response_class=HTMLResponse)
def request_table(table):
    return table_existance(table)


#pull all  data of a table 
@app.get("/pull_all/{table}", response_class=JSONResponse)
def request_table(table):
    conn,cur=connection_db()
    return get_table(table)


#pull data of a table 
@app.get("/pull/{location}/{date}", response_class=JSONResponse)
def request_table(location,date):
    conn,cur=connection_db()
    # newdate=calibrage(date)
    # newdate=date.replace("_","/")
    newdate=date
    
    return search(cur,location,newdate)


if __name__ == '__main__':
    uvicorn.run(app,host="0.0.0.0" , port=8001)


