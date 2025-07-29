from fastapi import FastAPI, APIRouter
from informedthrower import make_informed_throw
from uuid import UUID
import random 

app = FastAPI()
router = APIRouter(prefix="/api")

@router.get("/throw")
def throw_rps():
    return {"throw": get_throw()}
    
def get_throw():
    return random.choice(["rock", "paper", "scissors"])

@router.get("/informed-throw/{competitor_id}")
async def informed_throw(competitor_id: str):
    throw = await make_informed_throw(UUID(competitor_id))
    return {"throw": throw}

app.include_router(router)