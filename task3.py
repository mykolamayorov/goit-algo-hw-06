import networkx as nx
import matplotlib.pyplot as plt
from task1 import create_graph

# Визначення ваг для кожного ребра (наприклад, час у хвилинах між станціями)
edge_weights = {
    ('A', 'B'): 4,
    ('B', 'C'): 3,
    ('C', 'D'): 2,
    ('D', 'E'): 5,
    ('C', 'F'): 6,
    ('F', 'G'): 1
}

# Додавання ваг до існуючого графа
def add_weights_to_graph(G, weights):
    for u, v in G.edges():
        if (u, v) in weights:
            G[u][v]['weight'] = weights[(u, v)]
        elif (v, u) in weights:
            G[u][v]['weight'] = weights[(v, u)]
        else:
            G[u][v]['weight'] = 1  # Стандартна вага, якщо не вказано явно

# Візуалізація зваженого графа
def visualize_weighted_graph(G):
    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=800, font_size=14)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Зважена транспортна мережа")
    plt.show()

# Алгоритм Дейкстри — пошук найкоротшого шляху
def find_shortest_path(G, source, target):
    path = nx.dijkstra_path(G, source=source, target=target)
    distance = nx.dijkstra_path_length(G, source=source, target=target)
    return path, distance

# Точка входу
if __name__ == "__main__":
    G = create_graph()                     # Отримання графа з task1.py
    add_weights_to_graph(G, edge_weights)  # Додавання ваг

    visualize_weighted_graph(G)            # Візуалізація графа з вагами

    source, target = 'A', 'G'
    path, distance = find_shortest_path(G, source, target)

    print(f"Найкоротший шлях з {source} до {target}: {path}")
    print(f"Загальна вага шляху: {distance}")