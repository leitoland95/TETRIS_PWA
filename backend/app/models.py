from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TetrisGame(Base):
    __tablename__ = 'tetris_games'

    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    level = Column(Integer)

    def __repr__(self):
        return f'TetrisGame(id={self.id}, score={self.score}, level={self.level})'