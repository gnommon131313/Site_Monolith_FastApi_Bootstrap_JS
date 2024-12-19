from fastapi import APIRouter, HTTPException
from app.fast_api import schemes
from app.database.engine import SessionLocal
from app.database import models
from pydantic import ValidationError
import random
from datetime import datetime
from starlette.requests import Request
from app.fast_api import main

router = APIRouter()
    
@router.get("/orders", tags=['orders'])
async def read_html(request: Request):
    return main.templates.TemplateResponse("orders.html", {"request": request,})
    
@router.get("/api/orders", tags=['orders'])
async def read_orders():
    with SessionLocal() as session: 
        orders = session.query(models.Order).all()
        
    return {"orders": orders, "msg": "response is success"}
    
@router.post("/api/orders/create", tags=['orders'])
async def create_order(order: schemes.Order):
    with SessionLocal() as session: 
        new_order = models.Order(
            **vars(order),
            date=str(datetime.now().date()),
            total=random.randint(1, 999999))
        
        session.add(new_order)
        session.commit()
    
    return {"msg": "response is success"}