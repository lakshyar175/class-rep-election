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

# E4
def approve_candidate(candidate_id):
    session = Session(engine)
    candidate = session.get(Candidates, candidate_id)
    if candidate is None:
        session.close()
        return None
    election = session.query(Election).first()
    if election is None or election.phase != "nominations":
        session.close()
        return "phase_closed"
    if candidate.status != "nominated":
        session.close()
        return "invalid_status"
    candidate.status = "approved"
    session.commit()
    session.close()
    return "approved"


# E5
def withdraw_candidate(roll_no):
    session = Session(engine)
    candidate = session.query(Candidates).filter(
        Candidates.roll_no == roll_no
    ).first()
    if candidate is None:
        session.close()
        return None
    election = session.query(Election).first()
    if election is None or election.phase != "nominations":
        session.close()
        return "phase_closed"
    if candidate.status != "nominated":
        session.close()
        return "invalid_status"
    candidate.status = "withdrawn"
    session.commit()
    session.close()
    return "withdrawn"

# E6
def get_election_phase():
    session = Session(engine)
    election = session.query(Election).first()
    if election is None:
        session.close()
        return None
    phase = election.phase
    session.close()
    return phase