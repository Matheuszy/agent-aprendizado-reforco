import pytest
from agent_aprendizado_reforco.Taxi_v4 import train_and_eval_taxi
from agent_aprendizado_reforco.FrozenLake_v1 import train_and_eval_frozen

def test_taxi_training_returns_correct_structure():
    result = train_and_eval_taxi(
        alpha=0.1,
        gamma=0.9,
        epsilon=1.0,
        epsilon_decay=0.99,
        epsilon_min=0.01,
        num_episodes=10
    )
    
    assert isinstance(result, dict)
    assert "successes" in result
    assert "total_tests" in result
    assert "success_rate" in result
    assert "path" in result
    assert isinstance(result["path"], list)

def test_frozen_lake_training_returns_correct_structure():
    result = train_and_eval_frozen(
        alpha=0.8,
        gamma=0.95,
        epsilon=1.0,
        epsilon_decay=0.99,
        epsilon_min=0.01,
        num_episodes=10
    )
    
    assert isinstance(result, dict)
    assert "success_rate" in result
    assert "path" in result