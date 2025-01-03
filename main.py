from fastapi import FastAPI
from typing import List

app = FastAPI()

@app.get("/",response_model=List[str])
def read_root():
    return ["apple", "banana", "lemon"]