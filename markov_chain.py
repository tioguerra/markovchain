

import random

# Definição da Cadeia de Markov
# -----------------------------
# A estrutura de dados a seguir representa a cadeia de Markov descrita no
# arquivo .tex. Ela é baseada no diagrama da Figura 4.
#
# A matriz de transição é representada como um dicionário onde cada chave é um
# estado de origem. O valor associado a cada chave é outro dicionário que
# mapeia os estados de destino às suas respectivas probabilidades de transição.
#
# Por exemplo, a partir do estado 's0', temos:
# - 70% de chance de permanecer em 's0'
# - 20% de chance de ir para 's1'
# - 10% de chance de ir para 's3'
transition_matrix = {
    's0': {'s0': 0.7, 's1': 0.2, 's3': 0.1},
    's1': {'s2': 0.9, 's3': 0.1},
    's2': {'s1': 1.0},
    's3': {'s3': 1.0}
}

# Lista de todos os estados possíveis na cadeia
states = list(transition_matrix.keys())

def simulate_chain(start_state: str, num_steps: int) -> list[str]:
    """
    Simula uma caminhada aleatória na cadeia de Markov por um número definido de passos.

    Args:
        start_state: O estado inicial da simulação.
        num_steps: O número de transições a serem simuladas.

    Returns:
        Uma lista de strings representando o caminho percorrido pela cadeia,
        incluindo o estado inicial.
    """
    if start_state not in states:
        raise ValueError(f"Estado inicial '{start_state}' não existe na cadeia.")

    path = [start_state]
    current_state = start_state

    for _ in range(num_steps):
        # Obtém as possíveis transições a partir do estado atual
        transitions = transition_matrix.get(current_state, {})
        if not transitions:
            # Se um estado não tem saídas definidas (é um estado absorvente sem loop),
            # ele permanece em si mesmo.
            next_state = current_state
        else:
            # Pega os estados de destino e suas probabilidades
            next_states = list(transitions.keys())
            probabilities = list(transitions.values())
            
            # Escolhe o próximo estado com base nas probabilidades
            next_state = random.choices(next_states, weights=probabilities, k=1)[0]
        
        path.append(next_state)
        current_state = next_state

    return path

if __name__ == "__main__":
    # Exemplo de uso da simulação
    # ---------------------------
    # Você pode alterar o 'start_state' e 'simulation_steps' para ver diferentes
    # resultados.
    
    initial_state = 's0'
    simulation_steps = 20

    print(f"Iniciando simulação da Cadeia de Markov a partir do estado '{initial_state}' por {simulation_steps} passos.")
    
    # Executa a simulação
    trajectory = simulate_chain(start_state=initial_state, num_steps=simulation_steps)

    # Imprime o resultado de forma legível
    print("\nCaminho percorrido:")
    print(" -> ".join(trajectory))

    # Verifica o estado final e se é um estado absorvente
    final_state = trajectory[-1]
    if transition_matrix.get(final_state, {}).get(final_state) == 1.0 and len(transition_matrix.get(final_state, {})) == 1:
        print(f"\nA simulação terminou no estado absorvente: '{final_state}'")


