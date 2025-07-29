import httpx
from uuid import UUID

competitor_data = []

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