# 🤖 RL Hyperparameter Playground API

Uma API interativa e modular desenvolvida em Python para simulação, treinamento e avaliação de algoritmos de **Aprendizado por Reforço (Reinforcement Learning)** utilizando o ecossistema **Gymnasium**. 

O objetivo principal deste projeto é servir como um **laboratório visual e prático (playground)** para estudantes e desenvolvedores testarem como diferentes combinações de hiperparâmetros (como `alpha`, `gamma` e `epsilon`) afetam o comportamento e a taxa de convergência de agentes inteligentes em tempo real.

---

## 📌 Status do Projeto

* 🟢 **Core Backend & API:** Concluídos e totalmente funcionais.
* 🟢 **Cenários Suportados:** `Taxi-v3` e `FrozenLake-v1`.
* 🟡 **Cenários Em Desenvolvimento:** `CliffWalking-v1` e `CartPole-v1`.
* 🚀 **Deploy Cloud:** Em planejamento (Infraestrutura Serverless / Cloudflare / Render).

---

## 🎯 Propósito do Projeto

Em vez de apenas rodar scripts isolados no terminal, esta aplicação foi desenhada para expor a lógica do Q-Learning através de uma API REST limpa e desacoplada. Qualquer pessoa pode consumir a API ou utilizar a interface gráfica para ajustar hiperparâmetros e visualizar instantaneamente a tomada de decisão do agente e sua taxa de sucesso após milhares de episódios de treino.

---

## 🛠️ Tecnologias e Ferramentas

### **Backend (Foco Principal)**
* **Python 3.12+**
* **[uv](https://github.com/astral-sh/uv):** Gerenciador de pacotes e ambientes virtuais ultrarrápido (substituindo `pip`/`venv` tradicional).
* **[FastAPI](https://fastapi.tiangolo.com/):** Framework web assíncrono para construção dos endpoints de simulação.
* **[Pydantic](https://docs.pydantic.dev/):** Validação estrita de dados e tipos para os hiperparâmetros de entrada.
* **[Gymnasium](https://gymnasium.farama.org/):** Ambiente padrão para algoritmos de Aprendizado por Reforço.
* **NumPy:** Manipulação da Q-Table e processamento vetorial de recompensas.

### **Frontend (Visualizador)**
* **React + Vite:** Interface reativa para renderização da grade de estados.
* **Tailwind CSS (v4):** Estilização moderna e responsiva.
* **Howler.js:** Efeitos sonoros e áudio imersivo estilo retro game.

---

## 🧱 Arquitetura e Organização do Projeto

A aplicação adota uma estrutura em camadas para manter a lógica matemática/algorítmica desacoplada das rotas HTTP:

```text
agent-aprendizado-reforco/
├── src/
│   ├── agent_aprendizado_reforco/   # Core: Lógica pura do Gymnasium e Q-Learning
│   │   ├── FrozenLake_v1.py
│   │   └── Taxi_v4.py
│   └── api/                         # Camada Web (FastAPI)
│       ├── models/                  # Schemas de validação Pydantic
│       ├── routes/                  # Endpoints da API REST
│       └── main.py                  # Ponto de entrada da aplicação e CORS
├── frontend/                        # Interface visual em React
├── pyproject.toml                   # Dependências do projeto (uv)
└── uv.lock                          # Lockfile de dependências exatas

## ⚙️ Hiperparâmetros Configuráveis

Através dos endpoints da API, é possível ajustar os seguintes parâmetros por requisição:

| Parâmetro       | Tipo               | Descrição                                              |
|-----------------|--------------------|--------------------------------------------------------|
| alpha           | float (0.0 a 1.0) | Taxa de Aprendizado (Learning Rate)                   |
| gamma           | float (0.0 a 1.0) | Fator de Desconto para recompensas futuras            |
| epsilon         | float (0.0 a 1.0) | Taxa inicial de exploração aleatória (Epsilon-Greedy) |
| epsilon_decay   | float              | Fator de decaimento do epsilon a cada episódio        |
| epsilon_min     | float              | Taxa mínima aceitável de exploração                   |
| num_episodes    | int                | Quantidade de episódios na fase de treinamento        |

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos

- Python 3.12+ instalado.
- [uv](https://github.com/astral-sh/uv) instalado (ou pip).
- Node.js (opcional, para rodar o frontend).

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd agent-aprendizado-reforco
```

### 2. Instalar dependências e rodar o Backend (FastAPI)

```bash
# O uv cria o ambiente virtual e instala tudo automaticamente
uv sync

# Subir o servidor da API
uv run uvicorn api.main:app --reload --port 8000
```

Acesse a documentação interativa da API via Swagger em: http://localhost:8000/docs

### 3. Rodar o Frontend

```bash
cd frontend
npm install
npm run dev
```