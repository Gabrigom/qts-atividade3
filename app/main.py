from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="API TDD VGMG")


class Item(BaseModel):
    item_id: int
    name: str
    description: Optional[str] = None
    price: float


mock_db = {
    1: {"item_id": 1, "name": "Item 1"},
    2: {"item_id": 2, "name": "Item 2"},
    3: {"item_id": 3, "name": "Item 3"},
}


@app.get("/")
def ler_root():
    return {"message": "API TDD VGMG funcionando!"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in mock_db:
        raise HTTPException(status_code=404, detail="Cartão Inválido")

    return mock_db[item_id]
