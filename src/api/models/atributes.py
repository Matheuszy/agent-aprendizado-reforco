from pydantic import BaseModel, Field
from typing import Type

class atributes (BaseModel):

    alpha: float = Field(0.1, ge=0.0, le=1.0, description="Taxa de aprendizado")
    gamma: float = Field(0.99, ge=0.0, le=1.0, description="Fator de desconto. Recompensas futuras X imediatas") 
    epsilon: float = Field(0.1, ge=0.0, le=1.0, description="Probabilidades exploratorias")
    epsilon_decay: float = Field(0.9995, ge=0.0, le=1.0, description="Reduz gradualmente a exploração conforme o agente aprende")
    epsilon_min: float = Field(0.1, ge=0.0, le=1.0, description="Limite mínimo de exploração para garantir que o agente ainda explore um pouco")   
    num_episodes: int = Field(2000, ge=1000, le=5000, description="Número de tentativas de aprendizado")


class SimulationResponse(BaseModel):
    scenario: str
    train_episodes: int
    test_episodes: int
    success_rate: float
    successes: int