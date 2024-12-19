import logging
from sqlalchemy.exc import IntegrityError
from app.database.engine import engine, SessionLocal
from app.database import models

def init() -> None:
    models.create_tables(engine)
    
    def users() -> None:
        with SessionLocal() as session:
            users = [
                models.User(id=123, name="Alex"),
                models.User(id=456, name="Bob"),
                models.User(id=789, name="Jhon"),
            ]
            
            try:
                for user in users:
                    session.add(user)
                
                session.commit()
            except IntegrityError:
                print('ERR: база не обновлена, юзер(ы) уже содержиться')
                logging.info('ERR: база не обновлена, юзер(ы) уже содержиться')
                
    def products() -> None:
        with SessionLocal() as session:
            products = [
                models.Product(name="thing 1", description = "super", price=11.0, image=f"Egg.png"),
                models.Product(name="thing 2", description = "super", price=22.0, image=f"EggRaw.png"),
                models.Product(name="thing 3", description = "super", price=33.0, image=f"EggsFried.png"),
                models.Product(name="thing 4", description = "super", price=44.0, image=f"Fish.png"),
                models.Product(name="thing 5", description = "super", price=55.0, image=f"FishCut.png"),
                models.Product(name="thing 6", description = "super", price=66.0, image=f"FishFried.png"),
                models.Product(name="thing 7", description = "super", price=77.0, image=f"FishSkeleton.png"),
                models.Product(name="thing 8", description = "super", price=88.0, image=f"FriedMeat.png"),
                models.Product(name="thing 9", description = "super", price=99.0, image=f"GarbageBag.png"),
                models.Product(name="thing 10", description = "super", price=100.0, image=f"Meat.png"),
                models.Product(name="thing 11", description = "super", price=111.0, image=f"MeatCut.png"),
                models.Product(name="thing 12", description = "super", price=122.0, image=f"PiecesOfMeat.png"),
            ]
            
            try:
                for product in products:
                    session.add(product)
                
                session.commit()
            except IntegrityError:
                print('ERR: база не обновлена, товар(ы) уже содержиться')
                logging.info('ERR: база не обновлена, товар(ы) уже содержиться')
   
    users()
    products()
    
    logging.info('инициализация базы завершена')