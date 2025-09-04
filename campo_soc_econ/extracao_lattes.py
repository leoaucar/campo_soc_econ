from bs4 import BeautifulSoup
import os
import re

path_dados = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','Data','raw'))

#define arquivos para busca
arquivo = 'Currículo do Sistema de Currículos Lattes (Rodrigo Salles Pereira dos Santos).html'
path_arquivo = os.path.abspath(os.path.join(path_dados,arquivo))


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
next_element = h1_tag.find_all_next(text=re.compile("^Integrantes.*"))
for i in next_element:
    print(i)