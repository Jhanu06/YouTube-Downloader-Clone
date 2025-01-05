
from fastapi import FastAPI,Form
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin. Restrict in production.
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
# Define the POST route to receive a and b in the request body
@app.post("/add")
def addnum(data: Dict[str, int]):
    a = data['a']
    b = data['b']
    return {"sum": a + b}
