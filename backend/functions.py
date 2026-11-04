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
    id = Column(Integer, primary_key=True)
    roll_no = Column(String)
    name = Column(String)
    position = Column(String)
    manifesto = Column(String)
    status = Column(String, default="nominated")

class votes(Base):
    __tablename__ = "votes"
    id = Column(Integer, primary_key=True)
    position = Column(String)
    candidate_id = Column(Integer)
    voter_roll = Column(String)
    voded_on = Column(DateTime, default=datetime.now)

class Election(Base):
    __tablename__ = "election"
    id = Column(Integer, primary_key=True)
    phase = Column(String, default="nominations")

Base.metadata.create_all(engine)


def sample_data():
    session = Session(engine)

        if session.query(Candidates).count() == 0:
            sample_candidates = [
                Candidates(roll_no="AU01", name="Toshimah",
                           position="class_rep",
                           manifesto="I will represent students and improve communication.",
                           status="approved"),

                Candidates(roll_no="AU02", name="Harsita",
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

# E7
def next_phase():
    session = Session(engine)
    election = session.get(Election, 1)
    if election.phase == "nominations":
        for position in POSITIONS:
            candidate = session.query(Candidates).filter(
                Candidates.position == position,
                Candidates.status == "approved"
            ).first()
            if candidate is None:
                session.close()
                return "no_candidate"
        election.phase = "voting"
    elif election.phase == "voting":
        election.phase = "closed"
    else:
        session.close()
        return "closed"
    session.commit()
    phase = election.phase
    session.close()
    return {"phase": phase}

# E8
def cast_vote(voter_roll, candidate_id):
    session = Session(engine)
    election = session.get(Election, 1)
    if election.phase != "voting":
        session.close()
        return "voting_closed"
    candidate = session.get(Candidates, candidate_id)
    if candidate is None:
        session.close()
        return "not_found"
    if candidate.status != "approved":
        session.close()
        return "not_approved"
    existing = session.query(votes).filter(
        votes.voter_roll == voter_roll,
        votes.position == candidate.position
    ).first()
    if existing is not None:
        session.close()
        return "already_voted"
    vote = votes(
        voter_roll=voter_roll,
        candidate_id=candidate_id,
        position=candidate.position
    )
    session.add(vote)
    session.commit()
    session.close()
    return {"message": "Vote recorded successfully"}

# E9
def get_voted_positions(voter_roll):
    session = Session(engine)
    votes = session.query(votes).filter(
        votes.voter_roll == voter_roll).all()
    positions = []
    for vote in votes:
        positions.append(vote.position)
    session.close()
    return {"voted_positions": positions}

# E10 
def get_results():
    session = Session(engine)
    election = session.get(Election, 1)
    if election.phase != "closed":
        session.close()
        return "not_closed"
    results = {}
    for position in POSITIONS:
        candidates = session.query(Candidates).filter(
            Candidates.position == position,
            Candidates.status == "approved").all()
        position_results = []
        for candidate in candidates:
            count = session.query(votes).filter(
                votes.candidate_id == candidate.id).count()
            position_results.append({
                "candidate_id": candidate.id,
                "name": candidate.name,
                "votes": count
            })
        results[position] = position_results
    session.close()
    return results

# E11
def add_sample_data():
    session = Session(engine)
    if session.query(Candidates).count() == 0:
        sample_candidates = [
            ("AU01", "Toshima", "class_rep",
             "I will represent students and improve communication.", "approved"),

            ("AU02", "Harshitha", "class_rep",
             "I will work towards better student coordination.", "approved"),

            ("AU03", "Adib", "sports_secretary",
             "I will encourage sports activities and teamwork.", "approved"),

            ("AU04", "Hemanth", "sports_secretary",
             "I will organize sports events for everyone.", "nominated"),

            ("AU05", "Samhitha", "cultural_secretary",
             "I will organize cultural programs and celebrations.", "approved"),

            ("AU06", "Darsh", "cultural_secretary",
             "I will encourage creativity and student participation.", "approved"),

            ("AU07", "Shafi", "tech_secretary",
             "I will promote technology and technical events.", "approved"),

            ("AU08", "Sarang", "tech_secretary",
             "I will bring innovative technical activities.", "withdrawn")
        ]

        candidate_list = []

        for candidate in sample_candidates:
            candidate_list.append(candidate)

        for candidate in candidate_list:
            add_candidate(
                roll_no=candidate[0],
                name=candidate[1],
                position=candidate[2],
                manifesto=candidate[3],
                status=candidate[4]
            )

    session.close()
    return "nominated"
