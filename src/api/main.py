from fastapi import FastAPI
from app.routes.agent import router as agent_router

app = FastAPI(title="RL Multi-Agent API", version="1.0.0")

app.include_router(agent_router)