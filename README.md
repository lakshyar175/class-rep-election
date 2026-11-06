# class-rep-election

## Problem Statement

The Class Rep Election Management System is a web-based application designed to simplify and manage student council elections digitally. The system allows students to nominate themselves for different student council positions, enables the election officer to review and approve nominations, and provides a platform for students to cast their votes securely.

The election process consists of three phases: Nominations, Voting, and Closed. Students can nominate themselves for positions such as Class Representative, Sports Secretary, Cultural Secretary, and Technical Secretary by providing their roll number, name, and manifesto. The election officer manages candidate approvals and controls the transition between election phases.

Student council elections in many colleges are still run with paper forms, spreadsheets or group chats. This causes several recurring problems:

* No structure
* Duplicate and invalid entries
* Double voting
* Lack of transparency
* Manual effort

## Tech Stack

| Layer    | Technology                  |
| -------- | --------------------------- |
| Backend  | FastAPI (Python), port 8001 |
| Database | SQLite (`election.db`)      |
| Frontend | React                       |

## Who is doing what?

| Day   | Partner  | What will you do?                                     | Completed? | What are you going to work on next? | Stuck on? |
| ----- | -------- | ----------------------------------------------------- | ---------- | ----------------------------------- | --------- |
| Day 1 | Thanmayee | Database setup and table creation                    | Yes        | testing and making my swagger work better |  No   |
| Day 1 | lakshya | Working on functions.py along with main.py             | Yes        | testing and working on frontend           |  No   |
| Day 1 | poojitha | Working on functions.py along with main.py            | Yes        | testing and working on frontend           |  No   |
| Day 2 | Thanmayee | working on errors in the backend code                | No         | Debugging                                 |  Yes  |
| Day 2 | lakshya | working on errors in the backend code                  | No         | Debugging                                 |  Yes  |
| Day 2 | poojitha | working on errors in the backend code                 | No         | Debugging                                 |  Yes  |
| Day 3 | Thanmayee | worked on officer.jsx file                 |  yes        | testing front end                  |   no        |
| Day 3 | lakshya  |  worked on nominate and app.jsx file                         |  yes         |   testing frontend                  |   no        |
| Day 3 | poojitha  |  worked on vote.jsx                |   yes       |     testing frontend                |   no       |


## Endpoint tracker

|#	Method | path	Built	Rules checked in /docs |	Connected to React	| Who |
| -------- | --------------------------------- |  ------------------- | --- |
|E1	get    |✅	|✅ |	✅|Poojitha |
|E2	post   |✅ |✅ |	✅|Poojitha |
|E3	get	   |✅	|✅ |	✅|Poojitha |
|E4	patch	 |✅ |✅ |	✅|Lakshya  |
|E5	patch	 |✅ |✅ |	✅|Lakshya  |
|E6	get  	 |✅ |✅	| ✅|Lakshya  |
|E7	patch  |✅ |✅	| ✅|Thanmayee|
|E8  post  |✅ |✅ | ✅|Thanmayee|
|E9  get   |✅ |✅ | ✅|Thanmayee|
|E10 get   |✅ |✅ | ✅|Thanmayee|

## Frontend tracker

| components files |	Shows the data |	Buttons work|	Shows API errors|	Who |
| ---------------  | -------------- |  ----------------------------- | --- |
| Nominate         |✅|	✅|	✅| Lakshya |
| Vote	           | ✅|	✅|✅|	Poojitha |
| Officer	         | ✅|	✅|✅|	Thanmayee |

## How to run our app

Backend:

cd backend
uvicorn main:app --reload --port 8001
open http://127.0.0.1:8001/docs in the browser

Frontend:

cd frontend
npm run dev
