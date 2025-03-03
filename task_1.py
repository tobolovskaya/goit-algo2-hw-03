import matplotlib.pyplot as plt
import networkx as nx

# побудова графа відповідно до логістичної мережі з 20 вершинами
G = nx.DiGraph()

# Визначення всіх зв'язків та пропускних здатностей
edges = [
    ("Термінал 1", "Склад 1", 25),
    ("Термінал 1", "Склад 2", 20),
    ("Термінал 1", "Склад 3", 15),
    ("Термінал 2", "Склад 3", 15),
    ("Термінал 2", "Склад 4", 30),
    ("Термінал 2", "Склад 2", 10),
    ("Склад 1", "Магазин 1", 15),
    ("Склад 1", "Магазин 2", 10),
    ("Склад 1", "Магазин 3", 20),
    ("Склад 2", "Магазин 4", 15),
    ("Склад 2", "Магазин 5", 10),
    ("Склад 2", "Магазин 6", 25),
    ("Склад 3", "Магазин 7", 20),
    ("Склад 3", "Магазин 8", 15),
    ("Склад 3", "Магазин 9", 10),
    ("Склад 4", "Магазин 10", 20),
    ("Склад 4", "Магазин 11", 10),
    ("Склад 4", "Магазин 12", 15),
    ("Склад 4", "Магазин 13", 5),
    ("Склад 4", "Магазин 14", 10),
]

# Додавання ребер до графа
G.add_weighted_edges_from(edges)

# Додавання джерела та стоку
G.add_node("Джерело")
G.add_node("Стік")

# З'єднання джерела з терміналами
G.add_edge("Джерело", "Термінал 1", capacity=50)
G.add_edge("Джерело", "Термінал 2", capacity=50)

# З'єднання магазинів зі стоком
for i in range(1, 15):
    G.add_edge(f"Магазин {i}", "Стік", capacity=30)

# Візуалізація графа
plt.figure(figsize=(12, 7))
pos = nx.spring_layout(G, seed=42)  # Визначення фіксованого розміщення вершин
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="black", node_size=2000, font_size=10)
labels = {(u, v): d for u, v, d in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)
plt.title("Оновлена логістична мережа")
plt.show()
