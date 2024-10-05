from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Order(BaseModel):
    customer_name: str
    ordertype: Optional[str] = None  # ordertype is optional, can be made required by removing Optional

@app.get("/order/")
async def get_order(customer_name: str, ordertype: Optional[str] = None):
    return {"customer_name": customer_name, "ordertype": ordertype}