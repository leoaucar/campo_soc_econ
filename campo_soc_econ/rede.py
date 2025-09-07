import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

rede_1 = pd.read_csv('rede_rodrigo.csv')
rede_1 = rede_1.groupby(['Pessoa1','Pessoa2'], as_index=False).size()
rede_1.columns = ['Pessoa1','Pessoa2','weight']
print(rede_1.sort_values(by='weight',ascending=False).head())


# Create the NetworkX graph
G = nx.from_pandas_edgelist(rede_1, source='Pessoa1', target='Pessoa2', edge_attr='weight')

ego_G = nx.ego_graph(G, 'Rodrigo Salles Pereira dos Santos', radius=1)

# Print basic graph information
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")

pos = nx.spring_layout(ego_G)


# Basic drawing
nx.draw(ego_G, pos, with_labels=True)

plt.show()