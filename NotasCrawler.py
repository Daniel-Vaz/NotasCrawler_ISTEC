#!python3
# O objectivo deste script é tomar recursso das funcionalidades do módulo Request para obter o código fonte do site my.istec.pt, e usar o módulo BeautifulSoup para "navegar" na página e obter os links dos diferentes pdf's onde constam as notas dos alunos.
# Script em v.1.0 - Ter em conta que o código pode e deverá ser melhorado.

import bs4
import requests
import sys
import os


#Cadeiras disponíveis nos Ctesp's.
nome_de_cadeira = ["MAT","HI","RC","ANRO","ACS","SR","ISO","CLP","IT","EMP","AH","MH","DA","HRC","IRL","SR","SD","CASOS","PS","SCE","CSSL","SOC","SOS","SOOS","SOSOS","PT","FC","PC","CSSL","PETD","POO","EDECD","ASEBD","CEBDSQL","PSQL"]
#URL in plain text
url_texto = []
#Função Clear Screen
def cls():
    os.system("cls" if os.name=="nt" else "clear") #Windows\Linux Compatible


#Ecrã de entrada
print("|====================================================================================================================|")
print("|                                   .&&&%%%#                                                                         |")
print("|                                  ,%&&%%%(                                                                          |")
print("|                                  &&&&%%,                                                                           |")
print("|                   .(((.        ,&&&%%*               *@@@@@@@@@@&*      #@@@@@@@@*        *%&&&&@@#                |")
print("|                    .@&@,        /&&%%%                .***(&&@****.      #@&%*****.       %&&(                     |")
print("|                    .@&@,        (&&%%/                    *&&@           #@            /@@#                        |")
print("|                    .@&@,        (&&%%(                    *&&@           #@            (&@(                        |")
print("|                    .@&@,        ,&&&%%,                   *&&@           #@            (&@(                        |")
print("|                    .@&@,         %&&&%%/.                 *&&@           #@            (&@(                        |")
print("|                    .@&@,          /&&&%%%,                *&&@           #@            (&@(                        |")
print("|                    .@&@,           ,&&&%%%/.              *&&@           #@&&((((/     (&@(                        |")
print("|                    .@&@,             (&&&%%%(             *&&@           #@&&%%%%#.    (&@(                        |")
print("|                    .@&@,              *&&&%%%#            *&&@           #@            (&@(                        |")
print("|                    .@&@,                /&&&%%#           *&&@           #@            (&@(                        |")
print("|                    .@&@,                 %&&&%%           *&&@           #@            (&@(                        |")
print("|                    .@&@,                 %&&&%%           *&&@           #@            (&@(                        |")
print("|                    .@&@,                .&&&&%#           *&&@           #@            (&@(                        |")
print("|                    .@&@,                /&&&%%/           *&&@           #@            ,@&&                        |")
print("|                    .@@@,               #&&&%%#            *&&@           #@&&&&&&@*        &&&&%###/               |")
print("|                    ***               %&&&%%#                                                 (#%%%/                |")
print("|                                     .#&&&%%%.                                                                      |")
print("|                                    .&&&%%%,                                                                        |")
print("|                                   (&&&%%%.                                                                         |")
print("|====================================================================================================================|")
print("!                               !! Saberes as tuas notas nunca foi tão fácil !!                                v.1.0 !")
print("!                     *Script de Conssulta de Notas*. Focado para os Alunos dos Ctesp's RSI.                         !")
print("|--------------------------------------------------------------------------------------------------------------------|")

#Turma Selector
nome_de_turma = input('                         Qual é a Turma que pretende ver as notas? ( Escrever: "A\B\Pos") \n')
if nome_de_turma == ("A") or nome_de_turma == ("a"):
    nome_de_turma = "Turma A"
elif nome_de_turma == ("B") or nome_de_turma == ("b"):
    nome_de_turma = "Turma B"
elif nome_de_turma == ("Pos") or nome_de_turma == ("pos"):
    nome_de_turma = "Turma Pós-Laboral"
else:
    print("Os dados indicados não são os solicitados!")
    sys.exit()

#Selector de Ano
url = input('                         Qual é o Ano que pretende ver as notas? ( Escrever: "1" ou "2") \n')
if url == "1":
    url = "http://my.istec.pt/avaliacoes-rsi/"
elif url == "2":
    url = "http://my.istec.pt/redes-e-sistemas-informaticos-1617/"
else:
    print("Os dados indicados não são os solicitados!")
    sys.exit()
cls()


#Obtenção do Site
res = requests.get(url)
res.raise_for_status()
res = res.text
soup = bs4.BeautifulSoup(res, "lxml") #formatação

#Agrupamento da secçao das notas das cadeiras
container = soup.find("div", class_="content")
#Links Searcher
links = container.find_all_next(href=True, string=nome_de_turma)

#Loop MultiFunções. (To Be Improved) - Objectivos: Obter Link; Obter Nome do Módulo através desse Link; Apresentação final dos Links ao User.
def loop():
    for link in links:
        link = link["href"]
        url_texto = (link)
        link = link.split("/")[7]
        link = link.split("-")[0]
        nome_texto = link
        if nome_texto == nome_de_cadeira[0]:
            nome_texto = "Matemática"
        elif nome_texto == nome_de_cadeira[1]:
            nome_texto = "História de Informática"
        elif nome_texto == nome_de_cadeira[2]:
            nome_texto = "Redes de Computadores"
        elif nome_texto == nome_de_cadeira[3]:
            nome_texto = "Avaliação das Necessidades de Rede numa Organização"
        elif nome_texto == nome_de_cadeira[4]:
            nome_texto = "Arquitetura Cliente – Servidor"
        elif nome_texto == nome_de_cadeira[5]:
            nome_texto = "Serviços de Rede"
        elif nome_texto == nome_de_cadeira[6]:
            nome_texto = "Introdução aos Sistemas Operativos"
        elif nome_texto == nome_de_cadeira[7]:
            nome_texto = "Comunicar em Língua Portuguesa"
        elif nome_texto == nome_de_cadeira[8]:
            nome_texto = "Inglês Técnico"
        elif nome_texto == nome_de_cadeira[9]:
            nome_texto = "Empreendedorismo"
        elif nome_texto == nome_de_cadeira[10]:
            nome_texto = "Arquitetura de Hardware"
        elif nome_texto == nome_de_cadeira[11]:
            nome_texto = "Montagem de Hardware"
        elif nome_texto == nome_de_cadeira[12]:
            nome_texto = "Detecção de Avarias"
        elif nome_texto == nome_de_cadeira[13]:
            nome_texto = "Hardware e Redes de Computadores"
        elif nome_texto == nome_de_cadeira[14]:
            nome_texto = "Instalação de Redes Locais"
        elif nome_texto == nome_de_cadeira[15]:
            nome_texto = "Servidor de Dados"
        elif nome_texto == nome_de_cadeira[16]:
            nome_texto = "Configuração Avançada de Sistemas Operativos Servidores"
        elif nome_texto == nome_de_cadeira[17]:
            nome_texto = "Políticas de Segurança"
        elif nome_texto == nome_de_cadeira[18]:
            nome_texto = "Servidor de Correio Eletrónico"
        elif nome_texto == nome_de_cadeira[19]:
            nome_texto = "Configuração de Serviços num Servidor Linux"
        elif nome_texto == nome_de_cadeira[20]:
            nome_texto = "Sistema Operativo Cliente"
        elif nome_texto == nome_de_cadeira[21]:
            nome_texto = "Sistema Operativo Servidor"
        elif nome_texto == nome_de_cadeira[22]:
            nome_texto = "Sistemas Operativos Open Source"
        elif nome_texto == nome_de_cadeira[23]:
            nome_texto = "Sistema Operativo Servidor Open Source"
        elif nome_texto == nome_de_cadeira[24]:
            nome_texto = "Gestão e Manipulação Avançada de Aplicações Informáticas de Processamento de Texto"
        elif nome_texto == nome_de_cadeira[25]:
            nome_texto = "Gestão e Manipulação Avançada de Aplicações Informáticas de Folha de Cálculo"
        elif nome_texto == nome_de_cadeira[26]:
            nome_texto = "Primeiros Conceitos de Programação e Algoritmia e Estruturas de Controlo num Programa Informático"
        elif nome_texto == nome_de_cadeira[27]:
            nome_texto = "Programação Estruturada e Tipos de Dados"
        elif nome_texto == nome_de_cadeira[28]:
            nome_texto = "Programação Orientada a Objetos – Introdução"
        elif nome_texto == nome_de_cadeira[29]:
            nome_texto = "Estrutura de Dados Estática, Composta e Dinâmica"
        elif nome_texto == nome_de_cadeira[30]:
            nome_texto = "Análise de Sistemas e Estruturação de Bases de Dados"
        elif nome_texto == nome_de_cadeira[31]:
            nome_texto = "Criação de Estrutura de Base de Dados em SQL"
        elif nome_texto == nome_de_cadeira[32]:
            nome_texto = "Programação em SQL"
        else:
            nome_texto = "<Módulo não Identificado>"
        print("===============================================================================")
        print("| " + nome_texto + ":  | ")
        print("| Link:  " + url_texto )

loop()
print("|=============================================================================|")
print("!                    Espero que esteja tudo OK. Devolva Feedback              !")
print("|-----------------------------------------------------------------------------|")
input() #retem a consola aberta até ser pressionado Enter
