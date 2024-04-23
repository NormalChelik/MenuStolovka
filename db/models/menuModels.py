from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Menu(Base):
    __tablename__ = 'menu_dish'
    name_dish = Column(Text, primary_key=True, nullable=False)
    description_dish = Column(Text, nullable=False)
    photo_id_dish = Column(Text, nullable=False)

class ScoreMenu(Base):
    __tablename__ = 'score_dish'
    user_id = Column(Integer, primary_key=True, nullable=False)
    name_dish = Column(Text, nullable=False)
    score_dish = Column(Integer, nullable=False)