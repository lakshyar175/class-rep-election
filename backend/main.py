from sqlalchemy import Integer, String, Column, create_engine, DateTime, ForeignKey
from sqlalchemy.orm import Session, declarative_base
from datetime import datetime
from fastapi import FastAPI, HTTPException
import functions

app = FastAPI()


@app.get("/candidates")
def candidates(position=None, approved_only=False):
    return functions.get_candidates(position, approved_only)


@app.get("/candidates/{id}")
def candidate(id: int):
    result = functions.get_candidate(id)

    if result is None:
        raise HTTPException(status_code=404, detail="Candidate not found")

    return result



@app.post("/candidates")
def nominate(roll_no: str, name: str, position: str, manifesto: str):
    if position not in functions.POSITIONS:
        raise HTTPException(status_code=422, detail="Invalid position")

    if len(manifesto) < 30:
        raise HTTPException(status_code=422, detail="Manifesto must contain at least 30 characters")

    result = functions.nominate_candidate(roll_no, name, position, manifesto)

    return result


