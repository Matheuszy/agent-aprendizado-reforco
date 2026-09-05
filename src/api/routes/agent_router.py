from fastapi import APIRouter
from app.schemas.agent import HyperparametersRequest, SimulationResponse
from app.services.rl_service import run_q_learning

router = APIRouter(prefix="/simulations", tags=["Simulações RL"])

@router.post("/taxi", response_model=SimulationResponse)
def train_and_eval_taxi(params: HyperparametersRequest):
    return run_q_learning("Taxi-v3", params)

@router.post("/frozen-lake", response_model=SimulationResponse)
def train_and_eval_frozen(params: HyperparametersRequest):
    return run_q_learning("FrozenLake-v1", params)