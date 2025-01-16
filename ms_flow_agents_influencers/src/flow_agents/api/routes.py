from fastapi import APIRouter
from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

router = APIRouter()

# Rota para iniciar os agentes
@router.post("/influencers")
async def start_agents(topic: TextRequest, platform: TextRequest, command: TextRequest):
    try:
        from flow_agents.main import start_flow
        start_flow(topic.text, platform.text, command.text)
        print(topic.text, platform.text) 
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}