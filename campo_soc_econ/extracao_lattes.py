from bs4 import BeautifulSoup
import os
import re
import pandas as pd

path_dados = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','Data','raw'))

#define arquivos para busca
arquivo = 'Currículo do Sistema de Currículos Lattes (Rodrigo Salles Pereira dos Santos).html'
path_arquivo = os.path.abspath(os.path.join(path_dados,arquivo))
path_arquivo = r'C:\Users\leoau\Documents\campo_soc_econ\campo_soc_econ\Data\raw\Currículo do Sistema de Currículos Lattes (Rodrigo Salles Pereira dos Santos).html'

#parseia o HTML
with open(path_arquivo, "r") as file:
    # Read the file content
    html_content = file.read()
soup = BeautifulSoup(html_content, "html.parser")


#extrai resumo
paragraphs = soup.find_all('p', class_='resumo')
for p in paragraphs:
    pass
    #print(p.text)


#extrai projetos
projetos = soup.find_all('div', class_='layout-cell-pad-5')
for p in projetos:
    pass
    #print(p.text)

h1_tag = soup.find("h1", string='Projetos de pesquisa')
#print(h1_tag)

colaboradores = []
next_element = h1_tag.find_all_next(text=re.compile("^Integrantes.*"))
for i in next_element:
    i = i.replace('Integrantes:', '')
    i = i.replace('- Coordenador', '')
    i = i.replace('- Integrante','')
    i = i.replace('.','')
    i = i.split('/')
    i = [item.strip() for item in i]
    colaboradores.extend(i[1:])
    #colaborou_com = re.findall(r'([A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-záéíóúâêôãõç]+(?:\s+[A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-záéíóúâêôãõç]+)+)\s+-\s+(?:Integrante|Coordenador)', i)[1:]
    #if len(colaborou_com) > 0:
    #    print("PROJETO:\n")
    #    colaboradores.extend(colaborou_com)
    #    print(colaborou_com)
    #    print('PROXIMO PROJETO:')

rede = pd.DataFrame(columns=['Pessoa1','Pessoa2'])
rede['Pessoa2'] = colaboradores
rede['Pessoa1'] = i[0]
rede.to_csv('rede_rodrigo.csv')
