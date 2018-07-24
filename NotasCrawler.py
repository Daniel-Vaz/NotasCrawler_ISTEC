#!python3
# O objectivo deste script é tomar recursso das funcionalidades do módulo "Request" para obter o código fonte do site my.istec.pt 
# E usar o módulo "BeautifulSoup4" para navegar na página e obter os links dos diferentes pdf's onde constam as notas dos alunos.
# Script em v.1.2 - Ter em conta que o código pode e deverá ser melhorado.

import bs4
import requests
import sys
import os
from Cadeiras import Cadeira

#URL in plain text
url_texto = []
#Função Clear Screen
def cls():
    os.system("cls" if os.name=="nt" else "clear") #Windows\Linux Compatible


#Ecrã de entrada
print("|====================================================================================================================|\n|                                   .&&&%%%#                                                                         |\n|                                  ,%&&%%%(                                                                          |\n|                                  &&&&%%,                                                                           |\n|                   .(((.        ,&&&%%*               *@@@@@@@@@@&*      #@@@@@@@@*        *%&&&&@@#                |\n|                    .@&@,        /&&%%%                .***(&&@****.      #@&%*****.       %&&(                     |\n|                    .@&@,        (&&%%/                    *&&@           #@            /@@#                        |\n|                    .@&@,        (&&%%(                    *&&@           #@            (&@(                        |\n|                    .@&@,        ,&&&%%,                   *&&@           #@            (&@(                        |\n|                    .@&@,         %&&&%%/.                 *&&@           #@            (&@(                        |\n|                    .@&@,          /&&&%%%,                *&&@           #@            (&@(                        |\n|                    .@&@,           ,&&&%%%/.              *&&@           #@&&((((/     (&@(                        |\n|                    .@&@,             (&&&%%%(             *&&@           #@&&%%%%#.    (&@(                        |\n|                    .@&@,              *&&&%%%#            *&&@           #@            (&@(                        |\n|                    .@&@,                /&&&%%#           *&&@           #@            (&@(                        |\n|                    .@&@,                 %&&&%%           *&&@           #@            (&@(                        |\n|                    .@&@,                 %&&&%%           *&&@           #@            (&@(                        |\n|                    .@&@,                .&&&&%#           *&&@           #@            (&@(                        |\n|                    .@&@,                /&&&%%/           *&&@           #@            ,@&&                        |\n|                    .@@@,               #&&&%%#            *&&@           #@&&&&&&@*        &&&&%###/               |\n|                    ***               %&&&%%#                                                 (#%%%/                |\n|                                     .#&&&%%%.                                                                      |\n|                                    .&&&%%%,                                                                        |\n|                                   (&&&%%%.                                                                         |\n|====================================================================================================================|\n!                               !! Saberes as tuas notas nunca foi tão fácil !!                                v.1.0 !\n!                        *Script de Conssulta de Notas*     *Focado para os Alunos dos Ctesp's*                      !\n|--------------------------------------------------------------------------------------------------------------------|")


#Ctesp Selector
def CtespSelector():
    nome_de_curso = input(r'                         Pretende ver as notas de que CTeSPs? ( Escrever: "RSI,DDM,IG,DPM")' + '\n')
    if nome_de_curso == ("RSI") or nome_de_curso ==("rsi"):
        nome_de_curso = "Redes e Sistemas Informáticos"
    elif nome_de_curso == ("DDM") or nome_de_curso ==("ddm"):
        nome_de_curso = "Desenvolvimento para Dispositivos Móveis"
    elif nome_de_curso == ("IG") or nome_de_curso ==("ig"):
        nome_de_curso = "Informática de Gestão"    
    elif nome_de_curso == ("DPM") or nome_de_curso ==("dpm"):
        nome_de_curso = "Desenvolvimento de Produtos Multimédia"    
    else:
        print("Os dados indicados não são os solicitados!")
        sys.exit()
    return nome_de_curso
nome_de_curso = str(CtespSelector())

#Turma Selector
def TurmaSelector():
    nome_de_turma = input(r'                         Qual é a Turma que pretende ver as notas? ( Escrever: "A\B\Pos")' + '\n')
    if nome_de_turma == ("A") or nome_de_turma == ("a"):
        nome_de_turma = "Turma A"
    elif nome_de_turma == ("B") or nome_de_turma == ("b"):
        nome_de_turma = "Turma B"
    elif nome_de_turma == ("Pos") or nome_de_turma == ("pos"):
        nome_de_turma = "Turma Pós-Laboral"
    else:
        print("Os dados indicados não são os solicitados!")
        sys.exit()
    return nome_de_turma
nome_de_turma = str(TurmaSelector())

#Selector de Ano
def Ano ():
    ano = input('                         Qual dos Anos é que pretende ver as notas? ( Escrever: "1" ou "2")' + '\n')
    if ano == "1":
        ano = "1ºAno"
    elif ano == "2":
        ano = "2ºAno"
    else:
        print("Os dados indicados não são os solicitados!")
        sys.exit()
    return ano
ano = str(Ano())

cls()

#Função de escolha de link pendente opção indicada pelo utilizador
def SelectorDeLink():
    if nome_de_curso == "Redes e Sistemas Informáticos" and ano == "1ºAno":
        url = "http://my.istec.pt/avaliacoes-rsi/"
    elif nome_de_curso == "Redes e Sistemas Informáticos" and ano == "2ºAno":
        url = "http://my.istec.pt/redes-e-sistemas-informaticos-1617/"
    elif nome_de_curso == "Desenvolvimento para Dispositivos Móveis" and ano == "1ºAno":
        url = "http://my.istec.pt/avaliacoes-ddm/"
    elif nome_de_curso == "Desenvolvimento para Dispositivos Móveis" and ano == "2ºAno":
        url = "http://my.istec.pt/avaliacoes-ddm-1617/"
    elif nome_de_curso == "Informática de Gestão" and ano == "1ºAno":
        url = "http://my.istec.pt/avaliacoes-ig/"
    elif nome_de_curso == "Informática de Gestão" and ano == "2ºAno":
        url = "http://my.istec.pt/avaliacoes-informatica-de-gestao-1617/"
    elif nome_de_curso == "Desenvolvimento de Produtos Multimédia" and ano == "1ºAno":
        url = "http://my.istec.pt/avaliacoes-dpm/"
    elif nome_de_curso == "Desenvolvimento de Produtos Multimédia" and ano == "2ºAno":
        url = "http://my.istec.pt/avaliacoes-desenvolvimento-de-produtos-multimedia-20162017/"
    else: 
        url = "http://my.istec.pt/ctesp/"
    return url
url = str(SelectorDeLink())


#Obtenção do Site através do módulo Request
res = requests.get(url)
res.raise_for_status()
res = res.text
soup = bs4.BeautifulSoup(res, "lxml") # Formatação

#Agrupamento da secçao das notas das cadeiras
container = soup.find("div", class_="content")
#Links Searcher
links = container.find_all_next(href=True, string=nome_de_turma)

#Loop MultiFunções. 
def loop():
    for link in links:
        link = link["href"]
        url_texto = (link)  # Garantir uma cópia do URL em formato str()
        link = link.split("/")[7]
        link = link.split("-")[0]
        nome_texto = Cadeira(link)  # Tradução da Sigla no URl para nome completo da cadeira
        print("===============================================================================")
        print("| " + nome_texto + ":  \n ")
        print("| LINK:  " + url_texto )


#Apresentação final na CLI
print("|=============================================================================|")
print(" \n       Notas Referentes ao Ctesp: " + nome_de_curso + " do " + ano + "\n")
loop()
print("|=============================================================================|")
print("!                    Espero que esteja tudo OK. Devolva Feedback              !")
print("!                    https://github.com/Daniel-Vaz/NotasCrawler               !")
print("|-----------------------------------------------------------------------------|")
input() #Retem a consola aberta até ser pressionado Enter
