import { useState, useEffect } from "react";
import Vote from "./components/Vote";
import Nominate from "./components/Nominate";
import Officer from "./components/Officer";

const API_URL = "http://127.0.0.1:8001";

function App() {
const [phase, setPhase] = useState("");
const [candidates, setCandidates] = useState([]);
const [results, setResults] = useState(null);
const [message, setMessage] = useState("");

function loadAll() {
fetch(API_URL + "/election/phase")
.then((res) => res.json())
.then((data) => {
if (data.detail) {
setMessage(data.detail);
} else {
setPhase(data.phase);

      if (data.phase === "closed") {
        fetch(API_URL + "/results")
          .then((res) => res.json())
          .then((data) => setResults(data));
      } else {
        setResults(null);
      }
    }
  })

fetch(API_URL + "/candidates")
  .then((res) => res.json())
  .then((data) => {
    if (data.detail) {
      setMessage(data.detail);
    } else {
      setCandidates(data);
    }
  })

}

useEffect(() => {
loadAll();
}, []);

return (
<> <h2>Phase: {phase}</h2>
{message !== "" && <p>{message}</p>}
  <Vote
    apiUrl={API_URL}
    candidates={candidates}
    setMessage={setMessage}
    loadAll={loadAll}
  />
  <hr />
  <Nominate
    apiUrl={API_URL}
    candidates={candidates}
    setMessage={setMessage}
    loadAll={loadAll}
  />
  <hr />
  <Officer
    apiUrl={API_URL}
    phase={phase}
    candidates={candidates}
    results={results}
    setMessage={setMessage}
    loadAll={loadAll}
  />
</>
);
}

export default App;
