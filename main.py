from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Team(BaseModel):
    name: str
    members: List[str]


@app.get("/teams",response_model=List[Team])
def get_teams():
    return [Team(name="A", members=["apple", "banana", "lemon"]), Team(name="B", members=["cabbage", "tomato", "corn"])]

@app.get("/topics",response_model=str)
def get_topics():
    return "Which do you prefer, vegetables or fruits?"