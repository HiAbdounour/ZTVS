from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

## BaseModel from Pydantic also :: @ : response_model=this class and transform into this class like a function

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/api/hello")
async def hello():
    return {
        "message": "Bonjour depuis Python !"
    }

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)