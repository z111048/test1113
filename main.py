from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

# 載入 JSON 數據
with open("db.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 定義茶類型模型
class TeaType(BaseModel):
    id: int
    name: str
    description: str

@app.get("/teaTypes", response_model=List[TeaType])
def read_tea_types():
    return data["teaTypes"]

@app.get("/teaTypes/{tea_id}", response_model=TeaType)
def read_tea_type(tea_id: int):
    for tea_type in data["teaTypes"]:
        if tea_type["id"] == tea_id:
            return tea_type
    raise HTTPException(status_code=404, detail="Tea type not found")
