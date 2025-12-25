import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import collections

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title="Binary Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.show()

def build_heap_tree(heap, index=0):
    if index < len(heap):
        node = Node(heap[index])
        node.left = build_heap_tree(heap, 2 * index + 1)
        node.right = build_heap_tree(heap, 2 * index + 2)
        return node
    return None

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def generate_colors(n):
    start_color = "#003366"
    end_color = "#ADD8E6"
    
    cmap = mcolors.LinearSegmentedColormap.from_list("custom_blue", [start_color, end_color])
    return [mcolors.to_hex(cmap(i / (n - 1 if n > 1 else 1))) for i in range(n)]

def dfs_visualize(root):
    if not root:
        return
    
    total_nodes = count_nodes(root)
    colors = generate_colors(total_nodes)
    
    stack = [root]
    visited_count = 0
    
    while stack:
        node = stack.pop()
        node.color = colors[visited_count]
        visited_count += 1
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def bfs_visualize(root):
    if not root:
        return
    
    total_nodes = count_nodes(root)
    colors = generate_colors(total_nodes)
    
    queue = collections.deque([root])
    visited_count = 0
    
    while queue:
        node = queue.popleft()
        node.color = colors[visited_count]
        visited_count += 1
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)




#-----------------------------------------------------------------------------
# Checking time

heap_list = [1, 3, 5, 7, 9, 10, 11, 15, 17, 18, 21, 24]

# DFS
root_dfs = build_heap_tree(heap_list)
dfs_visualize(root_dfs)
draw_tree(root_dfs, title="DFS Traversal (Dark to Light)")

# BFS
root_bfs = build_heap_tree(heap_list)
bfs_visualize(root_bfs)
draw_tree(root_bfs, title="BFS Traversal (Dark to Light)")