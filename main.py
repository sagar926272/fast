from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import string
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://fast-fe.onrender.com/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the request schema
class InputData(BaseModel):
    data: List[str]

# Hardcoded user details
USER_ID = "Sagar kumar"
EMAIL = "sagarsaxena514@gmail.com"
ROLL_NUMBER = "2"
DOB = "17/03/2003"

@app.get("/bfhl")
def get_operation_code():
    return {"operation_code": 1}

@app.post("/bfhl")
def process_data(input_data: InputData):
    numbers = []
    alphabets = []
    
    for item in input_data.data:
        if item.isdigit():
            numbers.append(item)
        elif len(item) == 1 and item.isalpha():
            alphabets.append(item)
    
    highest_alphabet = max(alphabets, key=lambda x: string.ascii_lowercase.index(x.lower()), default=None)
    
    return {
        "is_success": True,
        "user_id": USER_ID,
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "dob": DOB,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": [highest_alphabet] if highest_alphabet else []
    }
