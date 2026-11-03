
from sqlalchemy import Integer, String, Column, create_engine, DateTime, ForeignKey
from sqlalchemy.orm import Session, declarative_base
from datetime import datetime
from fastapi import HTTPException

DB_PATH = "election.db"
engine = create_engine(f"sqlite:///{DB_PATH}")
Base = declarative_base()

POSITIONS = ["class_rep","sports_secretary","cultural_secretary","tech_secretary"]

class Candidates(Base):
    __tablename__ = "candidates"
    id = Column[int](Integer, primary_key=True)
    roll_no = Column[str](String)
    name = Column[str](String)
    position = Column[str](String)
    manifesto = Column[str](String)
    status = Column[str](String, default="nominated")
    nominated_on = Column(DateTime, default=datetime.now)

class votes():
    __tablename__ = "votes"
    id = Column[int](Integer, primary_key=True)
    position = Column[str](String)
    candidate_id = column[int](Integer)
    voter_roll = Column[str](String)
    voded_on = Column(DateTime, default=datetime.now)

class Election():
    __tablename__ = "election"
    id = Column(Integer, primary_key=True)
    phase = Column(String, default="nominations")


Base.metadata.create_all(engine)

