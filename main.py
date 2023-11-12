from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
import json

app = FastAPI()

# 加載 JSON 數據
with open("db.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 模型定義
class TeaType(BaseModel):
    id: int
    name: str
    description: str

class Ingredient(BaseModel):
    id: int
    name: str
    description: str

class Shop(BaseModel):
    id: int
    name: str
    Description: str
    # 其他字段...

class ShopBranch(BaseModel):
    storeId: int
    shopId: int
    branchName: str
    # 其他字段...

# 茶類型路由
@app.get("/teaTypes", response_model=List[TeaType])
def get_tea_types():
    return data["teaTypes"]

@app.get("/teaTypes/{tea_id}", response_model=TeaType)
def get_tea_type(tea_id: int):
    for tea_type in data["teaTypes"]:
        if tea_type["id"] == tea_id:
            return tea_type
    raise HTTPException(status_code=404, detail="Tea type not found")

# 成分路由
@app.get("/ingredients", response_model=List[Ingredient])
def get_ingredients():
    return data["ingredients"]

@app.get("/ingredients/{ingredient_id}", response_model=Ingredient)
def get_ingredient(ingredient_id: int):
    for ingredient in data["ingredients"]:
        if ingredient["id"] == ingredient_id:
            return ingredient
    raise HTTPException(status_code=404, detail="Ingredient not found")

# 店鋪路由
@app.get("/shops", response_model=List[Shop])
def get_shops():
    return data["shops"]

@app.get("/shops/{shop_id}", response_model=Shop)
def get_shop(shop_id: int):
    for shop in data["shops"]:
        if shop["id"] == shop_id:
            return shop
    raise HTTPException(status_code=404, detail="Shop not found")

# 分店路由
@app.get("/shopBranches", response_model=List[ShopBranch])
def get_shop_branches():
    return data["shopBranches"]

@app.get("/shopBranches/{branch_id}", response_model=ShopBranch)
def get_shop_branch(branch_id: int):
    for branch in data["shopBranches"]:
        if branch["storeId"] == branch_id:
            return branch
    raise HTTPException(status_code=404, detail="Shop branch not found")

# 其他 CRUD 操作...

