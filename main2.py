from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic model for request/response
class Calculator(BaseModel):
    Operation: str
    result: int

@app.get("/")
def index():
    return {"hello world"}

@app.get("/addition", response_model=Calculator, status_code=201, tags=["addition"])
def add(num1: int , num2:int ):
    return{'Operation':'Addition','result':num1+num2}
        

@app.get("/multiplication", response_model=Calculator, status_code=201, tags=["addition"])
def multi(num1: int , num2:int ):
    return{'Operation':'multiplication','result':num1*num2}


@app.get("/Substraction", response_model=Calculator, status_code=201, tags=["addition"])
def sub(num1: int , num2:int ):
    return{'Operation':'Substraction','result':num1-num2}