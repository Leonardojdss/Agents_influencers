from fastapi import APIRouter
from main import start_flow
from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

router = APIRouter()

# Rota para iniciar os agentes
@router.post("/influencers")
async def start_agents(topic: TextRequest, platform: TextRequest):
    try:
        start_flow(topic.text, platform.text)
        print(topic.text, platform.text) 
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}