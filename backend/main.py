from sqlalchemy import Integer, String, Column, create_engine, DateTime, ForeignKey
from sqlalchemy.orm import Session, declarative_base
from datetime import datetime
from fastapi import FastAPI, HTTPException
import functions
app = FastAPI()

# E4
@app.patch("/candidates/{candidate_id}/approve")
def approve_candidate(candidate_id: int):
    response = functions.approve_candidate(candidate_id)
    if response is None:
        raise HTTPException(status_code=404, detail="Candidate not found")
    if response is "phase_closed":
        raise HTTPException(status_code=400, detail="Nominations are closed")
    if response is "invalid_status":
        raise HTTPException(status_code=400, detail="Candidate cannot be approved")
    return {"message": "Candidate approved successfully"}

# E5
@app.patch("/candidates/{roll_no}/withdraw")
def withdraw_candidate(roll_no: str):
    response = functions.withdraw_candidate(roll_no)
    if response is None:
        raise HTTPException(status_code=404, detail="Candidate not found")
    if response is "phase_closed":
        raise HTTPException(status_code=400, detail="Nominations are closed")
    if response is "invalid_status":
        raise HTTPException(status_code=400, detail="Candidate cannot be withdrawn")
    return {"message": "Nomination withdrawn successfully"}

# E6
@app.get("/election/phase")
def get_election_phase():
    response = functions.get_election_phase()
    if response is None:
        raise HTTPException(status_code=404, detail="Election not found")
    return {"phase": response}