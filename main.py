from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 許可するオリジンを設定 
origins = [ "http://localhost:3000" ]

# CORSミドルウェアを追加
app.add_middleware( 
    CORSMiddleware, 
    allow_origins=origins, # 許可するオリジンを設定（例：すべてのオリジンを許可） 
)

class Team(BaseModel):
    name: str
    members: List[str]


@app.get("/teams",response_model=List[Team])
def get_teams():
    return [Team(name="A", members=["apple", "banana", "lemon"]), Team(name="B", members=["cabbage", "tomato", "corn"])]

@app.get("/topics",response_model=str)
def get_topics():
    return "Which do you prefer, vegetables or fruits?"