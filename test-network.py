import networkx as nx
import pandas as pd

df = pd.read_csv('q-network-python-centrality.csv')

G = nx.from_pandas_edgelist(df, source='source', target='target', create_using=nx.Graph())
centrality = nx.betweenness_centrality(G)

max_actor = max(centrality, key=centrality.get)
max_value = centrality[max_actor]

print(f"Actor with highest betweenness centrality: {max_actor}, Value: {max_value:.4f}")

top3 = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:3]
print("Top 3 actors by betweenness centrality:")
for actor, value in top3:
    print(actor, value)
