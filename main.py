from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

app = FastAPI()

# Order Management
class Order(BaseModel):
    customer_name: str = Field(..., description="Enter Customer Name")
    order_type: str = Field(..., description="Dine-In, Take-Out, or Delivery")

@app.post("/order/")
async def submit_order(order: Order):
    return {"message": "Order submitted successfully", "data": order}


# Table Reservations
class Reservation(BaseModel):
    customer_name: str = Field(..., description="Enter Customer Name")
    reservation_date: date = Field(..., description="Enter Reservation Date (mm/dd/yyyy)")
    number_of_guests: int = Field(..., description="Enter Number of Guests")

@app.post("/reservation/")
async def reserve_table(reservation: Reservation):
    return {"message": "Table reserved successfully", "data": reservation}


# Inventory Management
class Inventory(BaseModel):
    item_name: str = Field(..., description="Enter Item Name")
    quantity: int = Field(..., description="Enter Quantity")

@app.post("/inventory/")
async def add_inventory(item: Inventory):
    return {"message": "Item added to inventory", "data": item}


# Menu Management
class MenuItem(BaseModel):
    menu_item_name: str = Field(..., description="Enter Menu Item Name")
    price: float = Field(..., description="Enter Price")

@app.post("/menu/")
async def add_menu_item(item: MenuItem):
    return {"message": "Menu item added successfully", "data": item}


# Customer Feedback
class Feedback(BaseModel):
    customer_name: str = Field(..., description="Enter Customer Name")
    comments: Optional[str] = Field(None, description="Enter Comments")
    rating: int = Field(..., ge=1, le=5, description="Enter Rating (1-5)")

@app.post("/feedback/")
async def submit_feedback(feedback: Feedback):
    return {"message": "Feedback submitted successfully", "data": feedback}


# Reports and Analytics (optional)
class Report(BaseModel):
    report_type: str = Field(..., description="Enter the type of report (e.g., Sales, Inventory, Feedback)")

@app.post("/reports/")
async def generate_report(report: Report):
    return {"message": f"Generating {report.report_type} report"}