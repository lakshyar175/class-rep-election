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
    candidate_id = Column[int](Integer)
    voter_roll = Column[str](String)
    voded_on = Column(DateTime, default=datetime.now)

class Election():
    __tablename__ = "election"
    id = Column(Integer, primary_key=True)
    phase = Column(String, default="nominations")

Base.metadata.create_all(engine)

def sample_data():
    session = Session(engine)

        if session.query(Candidates).count() == 0:
            sample_candidates = [
                Candidates(roll_no="AU01", name="Toshima",
                           position="class_rep",
                           manifesto="I will represent students and improve communication.",
                           status="approved"),

                Candidates(roll_no="AU02", name="Harshitha",
                           position="class_rep",
                           manifesto="I will work towards better student coordination.",
                           status="approved"),

                Candidates(roll_no="AU03", name="Adib",
                           position="sports_secretary",
                           manifesto="I will encourage sports activities and teamwork.",
                           status="approved"),

                Candidates(roll_no="AU04", name="Hemanth",
                           position="sports_secretary",
                           manifesto="I will organize sports events for everyone.",
                           status="nominated"),

                Candidates(roll_no="AU05", name="Samhitha",
                           position="cultural_secretary",
                           manifesto="I will organize cultural programs and celebrations.",
                           status="approved"),

                Candidates(roll_no="AU06", name="Darsh",
                           position="cultural_secretary",
                           manifesto="I will encourage creativity and student participation.",
                           status="approved"),

                Candidates(roll_no="AU07", name="Shafi",
                           position="tech_secretary",
                           manifesto="I will promote technology and technical events.",
                           status="approved"),

                Candidates(roll_no="AU08", name="Sarang",
                           position="tech_secretary",
                           manifesto="I will bring innovative technical activities.",
                           status="withdrawn")
            ]
            session.add_all(sample_candidates)
            session.commit()
               