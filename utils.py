import pandas as pd
import networkx as nx

def calculate_critical_path(df):
    G = nx.DiGraph()
    task_dict = {row['Görev']: row for _, row in df.iterrows()}

    for _, row in df.iterrows():
        task = row['Görev']
        duration = row['Süre']
        dependencies = [d.strip() for d in row['Bağımlılık'].split(',') if d.strip()]
        if not dependencies:
            G.add_node(task, duration=duration)
        else:
            for dep in dependencies:
                if dep in task_dict:
                    G.add_edge(dep, task)
        G.nodes[task]["duration"] = duration

    # Ağırlıkları ekleyerek kritik yol analizi
    for u, v in G.edges():
        G[u][v]['weight'] = G.nodes[u]['duration']

    path = nx.dag_longest_path(G, weight='weight')
    total_duration = sum([G.nodes[node]['duration'] for node in path])
    return path, total_duration
