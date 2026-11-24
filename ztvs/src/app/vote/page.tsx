'use client';

import "./vote.css";
import votedata from "../../votedata.json";
import { saveAnswer } from "../services/saveAnswer";

export default function VotePage() {

  return (
    <main className="vote">
      <h1 className="mainquestion">{votedata.question}</h1>

      <div className="votebuttons">
        <button
          className="votebutton yesbtn"
          type="button"
          onClick={() => saveAnswer("Y")}
        >
          Oui
        </button>

        <button
          className="votebutton nobtn"
          type="button"
          onClick={() => saveAnswer("N")}
        >
          Non
        </button>

        <button
          className="votebutton passbtn"
          type="button"
          onClick={() => saveAnswer("W")}
        >
          Passer
          <span>(vote blanc)</span>
        </button>
      </div>
    </main>
  );
}