from fastapi import APIRouter
from api.models.atributes import atributes
from src.agent_aprendizado_reforco.Taxi_v4 import train_and_eval_taxi
from src.agent_aprendizado_reforco.FrozenLake_v1 import train_and_eval_frozen

router = APIRouter(prefix="/api", tags=["Simulações RL"])

@router.post("/taxi")
def simulate_taxi(params: atributes):
    return train_and_eval_taxi(
        alpha=params.alpha,
        gamma=params.gamma,
        epsilon=params.epsilon,
        epsilon_decay=params.epsilon_decay,
        epsilon_min=params.epsilon_min,
        num_episodes=params.num_episodes
    )

@router.post("/frozen-lake")
def simulate_frozen(params: atributes):
    return train_and_eval_frozen(
        alpha=params.alpha,
        gamma=params.gamma,
        epsilon=params.epsilon,
        epsilon_decay=params.epsilon_decay,
        epsilon_min=params.epsilon_min,
        num_episodes=params.num_episodes
    )