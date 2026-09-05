from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.agent_router import router as agent_router

app = FastAPI(title="RL Multi-Agent API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agent_router)