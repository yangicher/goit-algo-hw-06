import metro_graph
import graph_fs
import dijkstras_algorithm as da
import networkx as nx
import matplotlib.pyplot as plt
import timeit
from collections import deque

def main():
    metro_graph.create_metro()

    graph = metro_graph.get_graph()

    start = "Лук'янівська"
    target = "Олімпійська"

    #adj_list = {node: list(graph.neighbors(node)) for node in graph.nodes}

    dfs_paths = list(graph_fs.dfs_path(graph, start, target))
    bfs_paths = list(graph_fs.bfs_path(graph, start, target))

    dfs_time = timeit.timeit(lambda: graph_fs.dfs_path(graph, start, target), number=1)
    bfs_time = timeit.timeit(lambda: graph_fs.bfs_path(graph, start, target), number=1)

    write_conclusion(dfs_paths, dfs_time, bfs_paths, bfs_time)

    visualize_path(graph, dfs_paths, "DFS")
    visualize_path(graph, bfs_paths, "BFS")

    dijkstra_res = list(da.dijkstra(graph, start))
    print(dijkstra_res)

def visualize_path(graph, path, title):
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(12, 8))
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='r', width=2)
    nx.draw_networkx_nodes(graph, pos, nodelist=path, node_color='r')
    plt.title(title)
    plt.show()

def write_conclusion(dfs_paths, dfs_time, bfs_paths, bfs_time):
    with open("README.md", "w", encoding="utf-8") as file:
        file.write("# Comparison DFS and BFS \n\n")
        file.write(f"|Dfs |{dfs_paths}|{dfs_time}|\n")
        file.write(f"|Bfs |{bfs_paths}|{bfs_time}|\n")
        if(dfs_time < bfs_time):
            file.write("# DFS faster than BFS \n")
        else:
            file.write("# BFS faster than DFS \n")

        file.write("\n## Conclusions\n")
        file.write("#DFS - досліджує глибокі гілки графа, перш ніж переходити до інших, \n#BFS - вивчає рівні графа, спершу обробляючи всіх сусідів поточного вузла.")

if __name__ == "__main__":
    main()