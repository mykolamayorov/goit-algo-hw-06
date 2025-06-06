import networkx as nx
import matplotlib.pyplot as plt

# Функція створення простого незваженого графа
def create_graph():
    G = nx.Graph()

    # Вершини (станції метро)
    stations = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    G.add_nodes_from(stations)

    # Ребра (сполучення між станціями)
    edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('C', 'F'), ('F', 'G')]
    G.add_edges_from(edges)

    return G

# Візуалізація та базовий аналіз графа
def analyze_and_visualize(G):
    pos = nx.spring_layout(G)  # Розташування вузлів
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=800, font_size=14)
    plt.title("Транспортна мережа (метро)")
    plt.show()

    print("Кількість вершин:", G.number_of_nodes())
    print("Кількість ребер:", G.number_of_edges())
    print("Ступінь кожної вершини:")
    for node in G.nodes():
        print(f"{node}: {G.degree[node]}")

# Точка входу при запуску напряму
if __name__ == "__main__":
    graph = create_graph()
    analyze_and_visualize(graph)