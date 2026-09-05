import numpy as np
import gymnasium as gym

def train_and_eval_frozen(alpha: float, gamma: float, epsilon: float, 
                      epsilon_decay: float, epsilon_min: float, num_episodes: int):
    
    env = gym.make("FrozenLake-v1", is_slippery=True)
    q_table = np.zeros((env.observation_space.n, env.action_space.n))

    # Treinamento
    current_epsilon = epsilon
    for episode in range(num_episodes):
        state, _ = env.reset()
        done = False
        truncated = False

        while not (done or truncated):
            if np.random.rand() < current_epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(q_table[state])

            next_state, reward, done, truncated, _ = env.step(action)
            best_next_action = np.max(q_table[next_state])
            
            q_table[state, action] += alpha * (
                reward + gamma * best_next_action - q_table[state, action]
            )
            state = next_state

        if current_epsilon > epsilon_min:
            current_epsilon *= epsilon_decay


    last_path = []

    # Avaliação
    test_episodes = 1000
    successes = 0
    for episode in range(test_episodes):
        state, _ = env.reset()
        done = False
        truncated = False
        while not (done or truncated):
            action = np.argmax(q_table[state])
            state, reward, done, truncated, _ = env.step(action)
            if done and reward == 1.0:
                successes += 1

    env.close()
    
    return {
        "successes": successes,
        "total_tests": test_episodes,
        "success_rate": (successes / test_episodes) * 100,
        "path": last_path
    }