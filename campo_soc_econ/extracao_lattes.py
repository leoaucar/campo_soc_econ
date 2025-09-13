from bs4 import BeautifulSoup
import os
import re
import pandas as pd

def lista_arquivos():
    paths = []
    path_dados = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'Data','raw'))
    arquivos = os.listdir(path_dados)
    for arquivo in arquivos:
        path_arquivo = os.path.abspath(os.path.join(path_dados,arquivo))
        paths.append(path_arquivo)
    return paths

def obtem_html(path_arquivo):
    with open(path_arquivo, "r") as file:
        # Read the file content
        html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    return soup

def extrai_colaboradores(soup):
    h1_tag = soup.find("h1", string='Projetos de pesquisa')
    colaboradores = []
    next_element = h1_tag.find_all_next(string=re.compile("^Integrantes.*"))
    for i in next_element:
        i = i.replace('Integrantes:', '')
        i = i.replace('- Coordenador', '')
        i = i.replace('- Integrante','')
        i = i.replace('.','')
        i = i.split('/')
        i = [item.strip() for item in i]
        colaboradores.extend(i[1:])
    pessoa = i[0]
    return colaboradores, pessoa

def adiciona_ao_csv(colaboradores,pessoa):
    rede = pd.DataFrame(columns=['Pessoa1','Pessoa2'])
    rede['Pessoa2'] = colaboradores
    rede['Pessoa1'] = pessoa
    rede.to_csv('rede_'+pessoa+'.csv')

paths = lista_arquivos()
for path in paths:
    soup = obtem_html(path)
    colaboradores, pessoa = extrai_colaboradores(soup)
    adiciona_ao_csv(colaboradores, pessoa)


'''#extrai resumo
paragraphs = soup.find_all('p', class_='resumo')
for p in paragraphs:
    pass
    #print(p.text)

#extrai projetos
projetos = soup.find_all('div', class_='layout-cell-pad-5')
for p in projetos:
    pass
    #print(p.text)
'''
