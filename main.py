from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.put("/product/")
async def create_product(item_id:int, item: Product):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def get_file(file_path: str):
    return {"file_path": file_path}


@app.get(
    "/information/{type}"
)  # Ex: http://localhost/information/balance?size=10&qty=2&model=other
async def get_information(
    type: str, size: int, qty: int = 1, model: str | None = "default"
):
    return {"type": type, "size": size, "qty": qty, "model": model}
