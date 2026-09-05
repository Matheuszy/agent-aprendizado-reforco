import React, { useState } from 'react';
import axios from 'axios';
import { Howl } from 'howler';
import { Play, Volume2, VolumeX, Car, Snowflake, Bot, RefreshCw } from 'lucide-react';

const backgroundMusic = new Howl({
  src: ['https://cdn.pixabay.com/download/audio/2021/09/06/audio_78490a6d59.mp3?filename=game-music-7-14515.mp3'],
  loop: true,
  volume: 0.15
});

const scenarios = [
  { id: 'frozen-lake', name: 'Lago Congelado', icon: Snowflake, env: 'FrozenLake-v1', grid: 4 },
  { id: 'taxi', name: 'Motorista de Táxi', icon: Car, env: 'Taxi-v3', grid: 5 },
];

export default function App() {
  const [selectedScenario, setSelectedScenario] = useState(scenarios[0]);
  const [isPlayingAudio, setIsPlayingAudio] = useState(false);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [currentState, setCurrentState] = useState(0);
  
  const [params, setParams] = useState({
    alpha: 0.8,
    gamma: 0.95,
    epsilon: 1.0,
    epsilon_decay: 0.9995,
    epsilon_min: 0.01,
    num_episodes: 5000
  });

  const toggleAudio = () => {
    if (isPlayingAudio) {
      backgroundMusic.pause();
    } else {
      backgroundMusic.play();
    }
    setIsPlayingAudio(!isPlayingAudio);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setParams(prev => ({ ...prev, [name]: parseFloat(value) || 0 }));
  };

  const runSimulation = async () => {
    setLoading(true);
    setResult(null);
    try {
      // Ajuste o endpoint se a sua rota no FastAPI usar outro nome
      const endpoint = `http://localhost:8000/api/${selectedScenario.id}`;
      const response = await axios.post(endpoint, params);
      setResult(response.data);
      
      // Animação passo a passo do mascote na grade
      if (response.data.path && response.data.path.length > 0) {
        response.data.path.forEach((state, index) => {
          setTimeout(() => {
            setCurrentState(state);
          }, index * 350);
        });
      }
    } catch (err) {
      alert("Erro ao conectar com a API Python. Certifique-se de que o FastAPI está rodando na porta 8000!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 text-white p-6 flex flex-col items-center">
      {/* Cabeçalho */}
      <header className="w-full max-w-5xl flex justify-between items-center mb-8 border-b border-slate-800 pb-4">
        <h1 className="text-2xl font-bold flex items-center gap-3 text-cyan-400">
          <Bot className="w-8 h-8" /> Arena de Aprendizado por Reforço
        </h1>
        <button 
          onClick={toggleAudio}
          className="p-3 bg-slate-800 hover:bg-slate-700 rounded-full transition text-cyan-400"
          title="Música de Fundo"
        >
          {isPlayingAudio ? <Volume2 size={22} /> : <VolumeX size={22} />}
        </button>
      </header>

      <div className="w-full max-w-5xl grid grid-cols-1 md:grid-cols-3 gap-8">
        {/* Formulário de Configuração */}
        <div className="bg-slate-800 p-6 rounded-2xl border border-slate-700/60 flex flex-col gap-4">
          <h2 className="text-lg font-semibold text-slate-200">1. Selecione o Cenário</h2>
          <div className="grid grid-cols-2 gap-3">
            {scenarios.map((sc) => {
              const Icon = sc.icon;
              const isSelected = selectedScenario.id === sc.id;
              return (
                <button
                  key={sc.id}
                  onClick={() => { setSelectedScenario(sc); setResult(null); setCurrentState(0); }}
                  className={`p-3 rounded-xl flex flex-col items-center gap-2 font-medium border transition ${
                    isSelected ? 'bg-cyan-600 border-cyan-400 text-white' : 'bg-slate-700/50 border-transparent text-slate-400 hover:bg-slate-700'
                  }`}
                >
                  <Icon size={24} />
                  <span className="text-xs">{sc.name}</span>
                </button>
              );
            })}
          </div>

          <h2 className="text-lg font-semibold text-slate-200 mt-2">2. Hiperparâmetros</h2>
          <div className="flex flex-col gap-3 text-xs">
            <div>
              <label className="text-slate-400 block mb-1">Alpha (Taxa de Aprendizado): {params.alpha}</label>
              <input type="range" min="0" max="1" step="0.05" name="alpha" value={params.alpha} onChange={handleInputChange} className="w-full accent-cyan-400" />
            </div>
            <div>
              <label className="text-slate-400 block mb-1">Gamma (Desconto Futuro): {params.gamma}</label>
              <input type="range" min="0" max="1" step="0.05" name="gamma" value={params.gamma} onChange={handleInputChange} className="w-full accent-cyan-400" />
            </div>
            <div>
              <label className="text-slate-400 block mb-1">Epsilon Inicial: {params.epsilon}</label>
              <input type="range" min="0" max="1" step="0.05" name="epsilon" value={params.epsilon} onChange={handleInputChange} className="w-full accent-cyan-400" />
            </div>
            <div>
              <label className="text-slate-400 block mb-1">Epsilon Decay: {params.epsilon_decay}</label>
              <input type="number" step="0.0001" name="epsilon_decay" value={params.epsilon_decay} onChange={handleInputChange} className="w-full bg-slate-900 border border-slate-700 rounded p-2 text-white" />
            </div>
            <div>
              <label className="text-slate-400 block mb-1">Episódios de Treino:</label>
              <input type="number" name="num_episodes" value={params.num_episodes} onChange={handleInputChange} className="w-full bg-slate-900 border border-slate-700 rounded p-2 text-white" />
            </div>
          </div>

          <button
            onClick={runSimulation}
            disabled={loading}
            className="mt-2 w-full bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-bold py-3 rounded-xl flex items-center justify-center gap-2 transition disabled:opacity-50"
          >
            {loading ? <RefreshCw className="animate-spin" size={18} /> : <Play fill="currentColor" size={18} />}
            {loading ? 'Treinando Agente...' : 'Treinar & Simular'}
          </button>
        </div>

        {/* Visualização da Grade */}
        <div className="md:col-span-2 bg-slate-800 p-6 rounded-2xl border border-slate-700/60 flex flex-col justify-between items-center">
          <h2 className="text-lg font-semibold text-slate-200 self-start mb-4">Simulação Visual</h2>
          
          <div 
            className="grid gap-2 bg-slate-950 p-4 rounded-xl border border-slate-800"
            style={{ 
              gridTemplateColumns: `repeat(${selectedScenario.grid}, minmax(0, 1fr))` 
            }}
          >
            {Array.from({ length: selectedScenario.grid * selectedScenario.grid }).map((_, idx) => {
              const isAgentHere = currentState === idx;
              return (
                <div 
                  key={idx} 
                  className={`w-14 h-14 md:w-16 md:h-16 rounded-lg flex items-center justify-center font-bold text-lg border transition-all ${
                    isAgentHere 
                      ? 'bg-cyan-500 border-cyan-300 shadow-lg shadow-cyan-500/50 scale-105' 
                      : 'bg-slate-900/80 border-slate-800 text-slate-700'
                  }`}
                >
                  {isAgentHere ? (
                    selectedScenario.id === 'taxi' ? '🚖' : '🤖'
                  ) : (
                    <span className="text-xs">{idx}</span>
                  )}
                </div>
              );
            })}
          </div>

          {/* Resultado da Avaliação */}
          {result && (
            <div className="w-full mt-6 bg-slate-900 p-4 rounded-xl border border-slate-700 text-center">
              <h3 className="text-sm font-semibold text-emerald-400">Resultado do Teste</h3>
              <p className="text-slate-300 mt-1 text-sm">
                Taxa de Sucesso: <span className="font-bold text-white">{result.success_rate}%</span> ({result.successes} de {result.total_tests} vitórias)
              </p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}