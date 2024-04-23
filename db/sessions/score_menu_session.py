from db.create_db import create_session
from db.models.menuModels import ScoreMenu

session = create_session()

def add_score(user_id: int, name_dish: str, score: int) -> None:
    session.add(ScoreMenu(
        user_id=user_id,
        name_dish=name_dish,
        score_dish=score
    ))
    session.commit()

def check_user_score(user_id: int, name_dish: str):
    return session.query(ScoreMenu.score_dish).filter(ScoreMenu.user_id == user_id, ScoreMenu.name_dish == name_dish).all()

def check_dish_score(name_dish: str):
    return session.query(ScoreMenu.score_dish).filter(ScoreMenu.name_dish == name_dish).all()