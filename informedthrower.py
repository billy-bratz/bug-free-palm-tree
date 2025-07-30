import httpx
from datetime import datetime, timezone, timedelta
from uuid import UUID
from typing import Literal, Optional, Dict
from pydantic import BaseModel, Field

Throw = Literal["Rock", "Paper", "Scissors"]

class RoundTelemetry(BaseModel):
    round_number: int
    your_throw: Optional[Throw] = None
    opponent_throw: Optional[Throw] = None
    winner_id: Optional[UUID]
    
class MatchTelemetry(BaseModel):
    match_id: UUID
    opponent_id: UUID
    winner_id: Optional[UUID] = None
    you_are_winner: Optional[bool] = None
    rounds: list[RoundTelemetry]
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc),
                                description="Timestamp of the match telemetry")

competitor_data = []
telemetry_data: Dict[UUID, MatchTelemetry] = {}

async def fetch_competitor_data(a: UUID):
    try:
        resp = await httpx.AsyncClient().get(f"http://rps-competition-bot.a2dmfpegefctc2hg.westus2.azurecontainer.io/api/competitors/{a}/throws", timeout=httpx.Timeout(10.0, connect=5.0))
        competitor_data.append(resp.json())
    except Exception as ex:
        print(f"Error fetching competitor data: {ex}")
        
async def make_informed_throw(competitor_id: UUID):
    await fetch_competitor_data(competitor_id)
    if not competitor_data:
        return "rock" 

    last_throw = competitor_data[-1].get("last_throw", "rock")
    
    if last_throw == "rock":
        throw = "paper"
    elif last_throw == "paper":
        throw = "scissors"
    else:
        throw = "rock"
    
    competitor_data.clear()
    return throw

def add_telemetry(matchTelemetry: MatchTelemetry):
    if len(matchTelemetry.rounds) < 1:
        telemetry_data[matchTelemetry.match_id] = matchTelemetry
    else:
        telemetry_data[matchTelemetry.match_id].rounds.extend(matchTelemetry.rounds)
    
    cutoff_time = datetime.now(timezone.utc) - timedelta(days=1)
    for match_id, data in list(telemetry_data.items()):
        if data.timestamp < cutoff_time:
            del telemetry_data[match_id]