from sqlalchemy import Integer, String, Column, create_engine, DateTime, ForeignKey
from sqlalchemy.orm import Session, declarative_base
from datetime import datetime
from fastapi import HTTPException

DB_PATH = "election.db"
engine = create_engine(f"sqlite:///{DB_PATH}")
Base = declarative_base()

POSITIONS = ["class_rep","sports_secretary","cultural_secretary","tech_secretary"]


# E1
def get_candidates(position=None, approved_only=False):
    session = Session(engine)

    candidates = session.query(Candidates)

    if position is not None:
        candidates = candidates.filter(Candidates.position == position)

    if approved_only:
        candidates = candidates.filter(Candidates.status == "approved")

    result = candidates.all()

    session.close()
    return result


# E2
def get_candidate(id):
    session = Session(engine)

    candidate = session.get(Candidates, id)

    session.close()
    return candidate


# E3
def add_candidate(roll_no, name, position, manifesto):
    session = Session(engine)

    election = session.query(Election).first()

    if election is None or election.phase != "nominations":
        session.close()
        return "phase_closed"

    candidate = Candidates( 
        roll_no=roll_no,
        name=name,
        position=position,
        manifesto=manifesto,
        status="nominated"
    )

    session.add(candidate)
    session.commit()

    session.close()
    return "nominated"
