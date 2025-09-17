import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import glob
import os

'''rede_1 = pd.read_csv('rede_rodrigo.csv')
rede_1 = rede_1.groupby(['Pessoa1','Pessoa2'], as_index=False).size()
rede_1.columns = ['Pessoa1','Pessoa2','weight']
print(rede_1.sort_values(by='weight',ascending=False).head())


# Create the NetworkX graph
G = nx.from_pandas_edgelist(rede_1, source='Pessoa1', target='Pessoa2', edge_attr='weight')

#pessoa = "Rodrigo Salles Pereira dos Santos"
pessoa = "Cristiano Fonseca Monteiro"
ego_G = nx.ego_graph(G, pessoa, radius=1)

# Print basic graph information
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")

pos = nx.spring_layout(ego_G)


# Basic drawing
nx.draw(ego_G, pos, with_labels=True)

plt.show()'''

def junta_arquivos(diretorio):
    df = pd.DataFrame(columns=['Pessoa1','Pessoa2'])
    files = os.listdir(diretorio)
    for i in files:
        df_novo = pd.read_csv(diretorio+i)
        df = pd.concat([df,df_novo], axis=0)
    return df

def cria_rede(df):
    # Create the NetworkX graph
    G = nx.from_pandas_edgelist(df, source='Pessoa1', target='Pessoa2', edge_attr='weight')
    pos = nx.spring_layout(G)

    nodes_to_label = set()
    for u, v, d in G.edges(data=True):
        if d['weight'] > 5:
            nodes_to_label.add(u)
            nodes_to_label.add(v)
    labels = {node: node for node in nodes_to_label}
    # Basic drawing
    nx.draw(G, pos, labels=labels)
    plt.show()




if __name__=="__main__":
    df = junta_arquivos("campo_soc_econ/Data/processed/")
    df = df.groupby(['Pessoa1','Pessoa2'], as_index=False).size()
    df = df.rename(columns={'size': 'weight'})
    cria_rede(df)