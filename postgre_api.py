from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request 
import json
import requests
import uvicorn

from config_global import * 
from db.fonctions import * 


# connection_db()
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

 
#pull data of a table 
@app.get("/pull/{table}", response_class=HTMLResponse)
def request_table(table):
    referral=table_existance(table)
    print(referral)
    return referral


# @app.post("/{table}")
# def insert_table(table,requete):
#     # insert_many(table,col_name,data)
#     pass
#     # return insert_many((table,col_name,data)    

   

    

if __name__ == '__main__':
    uvicorn.run(app,host="0.0.0.0" , port=8001)


