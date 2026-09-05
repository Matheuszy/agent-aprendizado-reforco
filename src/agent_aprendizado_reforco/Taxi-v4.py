import numpy as np
import gymnasium as gym

# Inicializar o ambiente Taxi
# O agente precisa levar seu passageiro ao destino 
env = gym.make("Taxi-v4")

while True:
    alpha = float(input("Digite o parâmetro alpha: "))
    gamma = float(input("Digite o parâmetro gamma: "))
    epsilon = float(input("Digite o parâmetro epsilon: "))
    epsilon_decay = float(input("Digite o parâmetro epsilon_decay: "))
    epsilon_min = float(input("Digite o parâmetro epsilon_min: "))
    
    num_episodes = int(input("Digite o parâmetro num_episodes: "))
    if num_episodes > 0:
        print("\nTodos os parâmetros foram preenchidos com sucesso!")
        break
    else:
        print("\nO número de episódios precisa ser maior que 0. Reiniciando o preenchimento...\n")


# Definir os hiperparâmetros do Q-Learning
alpha = alpha  # Taxa de aprendizado: o quanto o agente aprende de novas informações
gamma = gamma  # Fator de desconto: quão importante são as recompensas futuras em comparação com as imediatas
epsilon = epsilon  # Probabilidade inicial de explorar ações aleatórias
epsilon_decay = epsilon_decay  # Reduz gradualmente a exploração conforme o agente aprende
epsilon_min = epsilon_min  # Limite mínimo de exploração para garantir que o agente ainda explore um pouco
num_episodes = num_episodes  # Número total de tentativas de aprendizado (episódios)

# Criar a tabela Q (Q-table) com zeros
# As linhas representam os estados e as colunas representam as ações
q_table = np.zeros((env.observation_space.n, env.action_space.n))

# Iniciar o treinamento do agente
for episode in range(num_episodes):
    # Reiniciar o ambiente a cada episódio
    state, _ = env.reset()
    done = False

    while not done:
        # Escolher uma ação usando a estratégia epsilon-greedy
        # Com probabilidade 'epsilon', escolhemos uma ação aleatória (exploração)
        # Caso contrário, escolhemos a melhor ação conhecida até o momento (exploração)
        if np.random.rand() < epsilon:
            action = env.action_space.sample()  # Explorar uma ação aleatória
        else:
            action = np.argmax(q_table[state])  # Explorar a ação com maior valor na Q-table

        # Executar a ação escolhida no ambiente
        next_state, reward, done, truncated, _ = env.step(action)

        # Atualizar a Q-table com a fórmula de aprendizado por reforço
        # Q(s, a) = Q(s, a) + alpha * (recompensa + desconto * max(Q(s', a')) - Q(s, a))
        best_next_action = np.max(q_table[next_state])  # Melhor ação no próximo estado
        q_table[state, action] += alpha * (reward + gamma * best_next_action - q_table[state, action])

        # Avançar para o próximo estado
        state = next_state

    # Reduzir a taxa de exploração gradualmente, sem ultrapassar o mínimo definido
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

# Avaliar o desempenho do agente treinado
# Aqui, testamos 1000 episódios para verificar quantas vezes ele atravessa o lago com sucesso
successes = 0
for episode in range(1000):
    state, _ = env.reset()
    done = False
    while not done:
        # O agente agora só escolhe a melhor ação aprendida (sem exploração aleatória)
        action = np.argmax(q_table[state])
        state, reward, done, truncated, _ = env.step(action)
        if done and reward == 20:
            successes += 1  # Contabilizar os sucessos

# Exibir o resultado final
print(f"O taxista conseguiu levar o passegeiro em {successes} de 1000 episódios.")