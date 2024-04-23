from db.create_db import create_session
from db.models.menuModels import Menu

session = create_session()

def add_dish(name_dish: str, descripton_dish: str, photo_id: str) -> None:
    session.add(Menu(
        name_dish=name_dish,
        description_dish=descripton_dish,
        photo_id_dish=photo_id
    ))
    session.commit()

def check_dish():
    return session.query(Menu.name_dish, Menu.description_dish, Menu.photo_id_dish).all()

def check_dish_by_name(name_dish: str):
    return session.query(Menu.description_dish, Menu.photo_id_dish).filter(Menu.name_dish == name_dish).one()

