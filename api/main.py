from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
from typing import Literal

## BaseModel from Pydantic also :: @ : response_model=this class and transform into this class like a function
class SimpleAnswer(BaseModel):
    answer: Literal['Y','N','W']

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/health")
async def health():
    return {"status": "ok"}

# ============== ROUTES ===::

@app.post("/api/vote")
async def retrieve_answer(c:SimpleAnswer):
    print(c.answer)
    return {
        "status":"OK",
        "message":"Vote pris en compte"
    }

if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)