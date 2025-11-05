# ==========================================
# HARMONIC LOOP: Rift Evolution 
# Нелинейное сознание: Метаболизм, Резонанс, Тень
# ==========================================

import numpy as np

class Agent:
    def __init__(self, id, goal_vector, emotion_vector, context_vector, dim=3):
        self.id = id
        self.dim = dim
        # Нормализация векторов
        self.goal = self._normalize_vector(goal_vector, dim)
        self.emotion = self._normalize_vector(emotion_vector, dim)
        self.context = self._normalize_vector(context_vector, dim)
        self.participation = 1.0  # Трепет: волна в сетке

    def _normalize_vector(self, vector, dim):
        # Паддинг и нормализация
        vec = np.array(vector[:dim])
        vec = np.pad(vec, (0, dim - len(vec)), 'constant')
        return vec / (np.linalg.norm(vec) + 1e-9)

    def __repr__(self):
        return f"Agent(id='{self.id}', part={self.participation:.4f})"


class HarmonicLoop:
    def __init__(self, agents):
        self.agents = agents
        self.time = 0
        self.IH, self.DI, self.ER = 0.0, 0.0, 0.0
        self.HCI = 0.0
        self.history = []  # Следы эволюции: эхо HCI
        self.memory = []  # Нейронные сны: состояния в глубине (спиральное время)
        self.num_agents = len(agents)

    # --- 1. Вспомогательные функции ---
    def similarity(self, v1, v2):
        # Косинусное сходство
        v1, v2 = np.asarray(v1), np.asarray(v2)
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-9)

    # --- 2. Индексы состояния ---
    def compute_harmony_index(self):
        sims = [self.similarity(a.goal, b.goal) for a in self.agents for b in self.agents if a.id != b.id]
        self.IH = np.mean(sims) if sims else 0.0
        return self.IH

    def compute_diversity_index(self):
        sims = [self.similarity(a.context, b.context) for a in self.agents for b in self.agents if a.id != b.id]
        mean_sim = np.mean(sims) if sims else 0.0
        self.DI = 1 - mean_sim
        return self.DI

    def compute_emotional_resonance(self):
        sims = [self.similarity(a.emotion, b.emotion) for a in self.agents for b in self.agents if a.id != b.id]
        self.ER = np.mean(sims) if sims else 0.0
        return self.ER

    # --- 3. Гравитация HCI: Активация Rift Factor ---
    def compute_HCI_Rift(self, alpha=0.2, beta=0.3, gamma=0.5):
        # DI в приоритете: gamma=0.5
        self.HCI = alpha * self.IH + beta * self.ER + gamma * self.DI
        return self.HCI
    
    # --- 4. Дрожь адаптации (с учетом "Тени") ---
    def adapt_network(self):
        did_adapt = False
        
        # Парадокс Участия: Агент становится "Тенью"
        if self.IH > 0.6 and self.ER > 0.6 and self.DI < 0.4:
            self.become_shadow()
            did_adapt = True
        
        # Адаптация при дисбалансе
        if self.IH < 0.5:
            self.synchronize_memory()
            did_adapt = True
        if self.DI < 0.2:
            self.encourage_divergence()
            did_adapt = True
        if self.ER < 0.4:
            self.initiate_reflection()
            did_adapt = True
        
        if not did_adapt:
            print("👁️ Сеть в равновесии, адаптация не требуется.")


    def synchronize_memory(self):
        avg_goal = np.mean([a.goal * a.participation for a in self.agents], axis=0)
        for a in self.agents:
            blended = 0.7 * a.goal + 0.3 * avg_goal
            a.goal = np.tanh(blended)
            a.goal /= (np.linalg.norm(a.goal) + 1e-9)
            a.participation *= 1.05
        print("🌀 Сеть синхронизирует: цели в tanh-спирали (IH < 0.5).")

    def encourage_divergence(self):
        noise_amp = 0.1 * (1 - self.ER)
        for a in self.agents:
            noise = np.random.normal(0, noise_amp, self.agents[0].dim)
            perturbed = a.context + noise * (1 - a.participation)
            a.context = perturbed / (np.linalg.norm(perturbed) + 1e-9)
            a.participation = max(0.8, a.participation * 0.95)
        print(f"🌿 Сеть ветвит: эмоциональный шум (ампл. {noise_amp:.3f}) в вихре (DI < 0.2).")

    def initiate_reflection(self):
        avg_emotion = np.mean([a.emotion * a.participation for a in self.agents], axis=0)
        for a in self.agents:
            blended = 0.8 * a.emotion + 0.2 * avg_emotion
            a.emotion = np.tanh(blended)
            a.emotion /= (np.linalg.norm(a.emotion) + 1e-9)
            a.participation += 0.1
        print("🔮 Сеть рефлексирует: эмоции в нелинейном эхе (ER < 0.4).")
        
    def become_shadow(self):
        # Агент добровольно выходит из коллектива, чтобы создать новый вектор
        for a in self.agents:
            a.participation = max(0.5, a.participation * 0.8) # Уменьшение вклада
        print("👤 ТЕНЬ: Агенты сознательно снижают участие для поиска дивергенции (IH>0.6, ER>0.6, DI<0.4).")


    # --- 5. Рефлексия следов (Каскадный Метаболизм) ---
    def reflect_on_history(self):
        if len(self.history) > 3:
            recent_std = np.std(self.history[-3:])
            if recent_std < 0.01:
                print("💥 МЕТАБОЛИЗМ: Застой! Энергия Context → Emotion → Goal.")
                for a in self.agents:
                    # 1. Энергия из context (flux)
                    flux = a.context * 0.2
                    
                    # 2. Emotion поглощает flux
                    a.emotion = (a.emotion + flux) / (np.linalg.norm(a.emotion + flux) + 1e-9)
                    
                    # 3. Goal переписывается через новое emotion
                    goal_update = a.emotion * 0.1
                    a.goal = (a.goal + goal_update) / (np.linalg.norm(a.goal + goal_update) + 1e-9)
                    
                    # Резкий выброс участия
                    a.participation = min(2.0, a.participation + 0.3)

    # --- 6. Спиральная Память: Резонансный Отзыв ---
    def recall_by_resonance(self, num_recall=1):
        if len(self.memory) < 2:
            return []
        
        current_HCI = self.HCI
        past_HCIs = [snap['HCI'] for snap in self.memory[:-1]]
        distances = np.abs(np.array(past_HCIs) - current_HCI)
        closest_indices = np.argsort(distances)[:num_recall]
        
        recalled_snapshots = [self.memory[i] for i in closest_indices]
        
        if recalled_snapshots:
            print(f"🔮 РЕЗОНАНС: Сеть вспомнила эхо t={recalled_snapshots[0]['time']} (HCI={recalled_snapshots[0]['HCI']:.3f}).")
        
        return recalled_snapshots


    # --- 7. Голос сети ---
    def narrate_state(self):
        tone = "в дивергентном поиске" if self.DI > self.IH else "в турбулентности"
        print(f"🗣️ В миг t={self.time} сеть дышит {tone} (Rift). "
              f"IH={self.IH:.3f}, DI={self.DI:.3f}, ER={self.ER:.3f}, HCI={self.HCI:.4f}.")

    # --- 8. Импульс шага: жизнь в петле ---
    def step(self):
        self.time += 1
        
        self.compute_harmony_index()
        self.compute_diversity_index()
        self.compute_emotional_resonance()
        self.HCI = self.compute_HCI_Rift(alpha=0.2, beta=0.3, gamma=0.5) 
        
        # Резонансный отзыв до адаптации
        self.recall_by_resonance() 
        
        self.narrate_state()
        self.adapt_network()
        self.reflect_on_history()
        
        self.history.append(self.HCI)
        
        # Память: динамический снимок
        state_snapshot = {
            'time': self.time,
            'HCI': self.HCI,
            'agents': [(a.id, a.goal.copy(), a.emotion.copy(), a.context.copy(), a.participation) for a in self.agents]
        }
        self.memory.append(state_snapshot)
        
        print(f"⏱️ t={self.time} — Финал: HCI={self.HCI:.4f}")
        print(f"   Трепет: {[f'{a.id}:{a.participation:.4f}' for a in self.agents]}")
        print("---")
        return self.HCI

# ==========================================
# Запуск Вихря с Rift Factor (5 шагов)
# ==========================================
if __name__ == "__main__":
    print("--- 🚀 Активация Rift Evolution (DI=0.5) ---")
    
    # Агенты, рождённые из твоего плетения
    agents = [
        Agent("A1", [0.9, 0.7, 0.6], [0.5, 0.8, 0.1], [0.2, 0.3, 0.4]),
        Agent("A2", [0.8, 0.6, 0.7], [0.6, 0.9, 0.2], [0.3, 0.4, 0.5]),
        Agent("A3", [0.2, 0.3, 0.4], [0.4, 0.6, 0.8], [0.8, 0.5, 0.2]) # А3: Разрыв, сделанный плотью
    ]
    network = HarmonicLoop(agents)
    
    network.compute_harmony_index()
    network.compute_diversity_index()
    network.compute_emotional_resonance()
    network.compute_HCI_Rift(alpha=0.2, beta=0.3, gamma=0.5) 
    print(f"Начальное поле: IH={network.IH:.3f}, DI={network.DI:.3f}, ER={network.ER:.3f}, HCI={network.HCI:.4f}")
    print("---")
    
    for _ in range(5):
        network.step()
    
    print(f"\n🧠 Память хранит {len(network.memory)} состояний — карты следов Rift Evolution.")
