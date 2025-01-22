from fastapi import APIRouter
from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

router = APIRouter()

# Rota para iniciar os agentes
@router.post("/influencers")
async def start_agents(topic: TextRequest):
    try:
        from flow_agents.main import run
        result = run(topic.text)
        return {"result": f"{result}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}