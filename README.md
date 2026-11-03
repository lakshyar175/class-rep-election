# class-rep-election


# Problem statement:
The Class Rep Election Management System is a web-based application designed to simplify and manage student council elections digitally. The system allows students to nominate themselves for different student council positions, enables the election officer to review and approve nominations, and provides a platform for students to cast their votes securely.

The election process consists of three phases: Nominations, Voting, and Closed. Students can nominate themselves for positions such as Class Representative, Sports Secretary, Cultural Secretary, and Technical Secretary by providing their roll number, name, and manifesto. The election officer manages candidate approvals and controls the transition between election phases.

Student council elections in many colleges are still run with paper forms, spreadsheets or group chats. This causes several recurring problems:

- No structure
- Duplicate and invalid entries 
- Double voting
- Lack of transparency
- Manual effort


# Tech Stack

| Layer    | Technology                  |
| -------- | --------------------------- |
| Backend  | FastAPI (Python), port 8001 |
| Database | SQLite (`election.db`)      |
| Frontend | React                       |


## 1. Who is doing what?

| Day   | Partner  | What will you do?                                     | Completed? | What are you going to work on next? | Stuck on? |
| ----- | -------- | ----------------------------------------------------- | ---------- | ----------------------------------- | --------- |
| Day 1 | Member 1 | Database setup and table creation                     | ⬜          |                   |           |
| Day 1 | Member 2 | Working on functions.py and election validation rules | ⬜          |                       |           |
| Day 1 | Member 3 | React setup and frontend components                   | ⬜          |                         |           |
| Day 2 | Member 1 | Working on main.py and API endpoints                  | ⬜          |                         |           |
| Day 2 | Member 2 | Testing API endpoints and handling errors             | ⬜          |                    |           |
| Day 2 | Member 3 | Connecting React frontend with FastAPI                | ⬜          |               |           |
| Day 3 | Member 1 | Backend testing and bug fixing                        | ⬜          |                   |           |
| Day 3 | Member 2 | Database and API validation                           | ⬜          |                     |           |
| Day 3 | Member 3 | Frontend testing and UI improvements                  | ⬜          |                     |           |

2. Endpoint Tracker

Status: 🟩 Done | 🟨 In progress | ⬜ Not started

#	Method + Path	Built	Rules checked in /docs	Connected to React	Who
E1	GET /candidates	⬜	⬜	⬜	Member 1
E2	GET /candidates/{id}	⬜	⬜	⬜	Member 1
E3	POST /candidates	⬜	⬜	⬜	Member 2
E4	PATCH /candidates/{id}/approve	⬜	⬜	⬜	Member 2
E5	PATCH /candidates/{id}/withdraw	⬜	⬜	⬜	Member 2
E6	GET /election/phase	⬜	⬜	⬜	Member 1
E7	PATCH /election/phase	⬜	⬜	⬜	Member 1
E8	POST /votes	⬜	⬜	⬜	Member 3
E9	GET /votes/{roll_no}	⬜	⬜	⬜	Member 3
E10	GET /results	⬜	⬜
