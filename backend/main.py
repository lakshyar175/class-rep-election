from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import functions

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"])

functions.initialize_database()

# E1
@app.get("/candidates")
def get_candidates(position = None,approved_only = False):
    if position and position not in functions.POSITIONS:
        raise HTTPException(status_code=422,detail="Invalid position")
    return functions.get_all_candidates(position, approved_only)

# E2
@app.get("/candidates/{candidate_id}")
def candidate(candidate_id: int|None=None):
    result = functions.get_candidate(candidate_id)
    if result == "not_found":
        raise HTTPException(status_code=404, detail="Candidate not found")
    return result

# E3
@app.post("/candidates")
def nominate(roll_no: str, name: str, position: str, manifesto:str):
    if position not in functions.POSITIONS:
        raise HTTPException(status_code=422, detail="Invalid position")
    if len(manifesto) < 30:
        raise HTTPException(status_code=422, detail="Manifesto must contain at least 30 characters")
    result = functions.add_candidate(roll_no, name, position, manifesto)
    if result == "duplicate_roll":
        raise HTTPException(status_code=400, detail="This roll number already has an active nomination")
    if result == "invalid_position":
        raise HTTPException(status_code=422, detail="Invalid position")
    return {"message": "Candidate nominated successfully"}

# E4
@app.patch("/candidates/{candidate_id}/approve")
def approve_candidate(candidate_id: int):
    response = functions.approve_candidate(candidate_id)
    if response == "phase_closed":
        raise HTTPException(status_code=400, detail="Nominations are closed")
    if response == "not_found":
        raise HTTPException(status_code=404, detail="Candidate not found")
    if response == "not_nominated":
        raise HTTPException(status_code=400, detail="Only nominated candidates can be approved")
    return {"message": "Candidate approved successfully"}

# E5
@app.patch("/candidates/{candidate_id}/withdraw")
def withdraw_candidate(candidate_id: int, roll_no: str):
    response = functions.withdraw_candidate(candidate_id, roll_no)
    if response == "phase_closed":
        raise HTTPException(status_code=400, detail="Nominations are closed")
    if response == "not_found":
        raise HTTPException(status_code=404, detail="Candidate not found")
    if response == "roll_mismatch":
        raise HTTPException(status_code=403, detail="Roll number does not match the candidate")
    if response == "already_withdrawn":
        raise HTTPException(status_code=400, detail="Candidate is already withdrawn")
    return {"message": "Nomination withdrawn successfully"}

# E6
@app.get("/election/phase")
def get_election_phase():
    response = functions.get_election_phase()
    if response == "no_election":
        raise HTTPException(status_code=404, detail="Election not found")
    return {"phase": response}

# E7
@app.patch("/election/phase")
def change_phase(phase: str):
    result = functions.change_phase(phase)
    if result == "no_election":
        raise HTTPException(status_code=404, detail="Election not found")
    if result == "invalid_phase":
        raise HTTPException(status_code=400, detail="Invalid election phase")
    if result == "no_candidate":
        raise HTTPException(status_code=400, detail="Every position must have at least one approved candidate")
    return result

# E8
@app.post("/votes")
def vote(voter_roll: str, candidate_id: int):
    if voter_roll == "":
        raise HTTPException(status_code=422,detail="Empty roll number")
    result = functions.cast_vote(voter_roll, candidate_id)
    if result == "voting_closed":
        raise HTTPException(status_code=400,detail="Voting is not open")
    if result == "not_found":
        raise HTTPException(status_code=404,detail="Candidate not found")
    if result == "not_approved":
        raise HTTPException(status_code=400,detail="Candidate not approved")
    if result == "already_voted":
        raise HTTPException(status_code=400,detail="Already voted for this position")

    return result

# E9
@app.get("/votes/{voter_roll}/positions")
def voted_positions(voter_roll: str):
    return functions.get_voted_positions(voter_roll)

# E10
@app.get("/results")
def get_final_results():
    result = functions.get_results()
    if result == "not_closed":
        raise HTTPException(status_code=403, detail="Election is not closed")
    return result