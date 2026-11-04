from sqlalchemy import Integer, String, Column, create_engine, DateTime, ForeignKey
from sqlalchemy.orm import Session, declarative_base
from datetime import datetime
from fastapi import FastAPI, HTTPException
import functions

app = FastAPI()
functions.sample_data()

# E1
@app.get("/candidates")
def candidates(position=None, approved_only=False):
    return functions.get_candidates(position, approved_only)

# E2
@app.get("/candidates/{id}")
def candidate(id: int):
    result = functions.get_candidate(id)
    if result is None:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return result

# E3
@app.post("/candidates")
def nominate(roll_no: str, name: str, position: str, manifesto: str):
    if position not in functions.POSITIONS:
        raise HTTPException(status_code=422, detail="Invalid position")
    if len(manifesto) < 30:
        raise HTTPException(status_code=422, detail="Manifesto must contain at least 30 characters")
    result = functions.add_candidate(roll_no, name, position, manifesto)
    return result

# E4
@app.patch("/candidates/{candidate_id}/approve")
def approve_candidate(candidate_id: int):
    response = functions.approve_candidate(candidate_id)
    if response is None:
        raise HTTPException(status_code=404, detail="Candidate not found")
    if response == "phase_closed":
        raise HTTPException(status_code=400, detail="Nominations are closed")
    if response == "invalid_status":
        raise HTTPException(status_code=400, detail="Candidate cannot be approved")
    return {"message": "Candidate approved successfully"}

# E5
@app.patch("/candidates/{roll_no}/withdraw")
def withdraw_candidate(roll_no: str):
    response = functions.withdraw_candidate(roll_no)
    if response is None:
        raise HTTPException(status_code=404, detail="Candidate not found")
    if response == "phase_closed":
        raise HTTPException(status_code=400, detail="Nominations are closed")
    if response == "invalid_status":
        raise HTTPException(status_code=400, detail="Candidate cannot be withdrawn")
    return {"message": "Nomination withdrawn successfully"}

# E6
@app.get("/election/phase")
def get_election_phase():
    response = functions.get_election_phase()
    if response is None:
        raise HTTPException(status_code=404, detail="Election not found")
    return {"phase": response}

# E7
@app.patch("/election/phase/next")
def change_phase():
    result = functions.next_phase()
    if result == "closed":
        raise HTTPException(status_code=400, detail="Election already closed")
    if result == "no_candidate":
        raise HTTPException(status_code=400, detail="No approved candidate")
    return result

# E8
@app.post("/votes", status_code=201)
def vote(voter_roll: str, candidate_id: int):
    if voter_roll == "":
        raise HTTPException(status_code=422, detail="Empty roll number")
    result = functions.cast_vote(voter_roll, candidate_id)
    if result == "voting_closed":
        raise HTTPException(status_code=400, detail="Voting is not open")
    if result == "not_found":
        raise HTTPException(status_code=404, detail="Candidate not found")
    if result == "not_approved":
        raise HTTPException(status_code=400, detail="Candidate not approved")
    if result == "already_voted":
        raise HTTPException(status_code=400, detail="Already voted for this position")
    return result

# E9
@app.get("/votes/{voter_roll}/positions")
def voted_positions(voter_roll: str):
    if voter_roll == "":
        raise HTTPException(status_code=422, detail="Empty roll number")
    return functions.get_voted_positions(voter_roll)

# E10
@app.get("/results")
def results():
    result = functions.get_results()
    if result == "not_closed":
        raise HTTPException(status_code=403, detail="Election is not closed")
    return result