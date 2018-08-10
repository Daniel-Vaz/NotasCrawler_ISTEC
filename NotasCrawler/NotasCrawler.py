#!python3
##############################################################################
#               Saberes as tuas notas nunca foi tão Fácil !                  #
#                    Copyright (C) <2018>  <Daniel Vaz>                      #
#                                                                            #
#    This program is free software: you can redistribute it and/or modify    #
#    it under the terms of the GNU General Public License as published by    #
#    the Free Software Foundation, either version 3 of the License, or       #
#    (at your option) any later version.                                     #
#                                                                            #
#    This program is distributed in the hope that it will be useful,         #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#    GNU General Public License for more details.                            #
#                                                                            #
#    You should have received a copy of the GNU General Public License       #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.  #
##############################################################################
# O objectivo deste script é facilitar a obtenção das notas dos Alunos nos CTeSP do ISTEC.
# Todo este código foi feito com uma mentalidade "OpenSource", tentando documentar todo o seu funcionamento, para quem quiser melhorar ou prosseguir com o seu desenvolvimento.
# Na sua totalidade o Script toma recurso dos seguintes Módulos \ Programas:
#
# Requests \ BeautifulSoup4-> Obter páginas Web e "navegar" os conteudos das mesma;
# Wand \ Pillow-> Conversão dos PDF's para JPG's, e manipulação das imagens para reterem apenas a informação Necessária;
# PyTesseract-> OCR responsável pelas tentativas de obtenção de texto dos JPG's modificados.
#
# Script em v.2.0 - Ter em conta que o código pode e deverá ser melhorado.


import bs4
import os
import requests
import sys
from Sup_CadeirasBD import Cadeira
from Sup_TesseractOCR import Loop_ComReconhecimento
import time


# Função Clear Screen
def cls():
    # Windows\Linux Compatible
    os.system("cls" if os.name == "nt" else "clear")


# Ecrã de Entrada
cls()
print(" |====================================================================================================================|\n |                                       .hmmdho`                                                                     |\n |                                       `smmdho                                                `----`                |\n |                           -syy-       /mmdhh.            `oyyyyyyyyyh.    -syyyyyhy-      -oymmmmm:                |\n |                           :dmN+      `smmhhy.            `/++omNN++++`    :dmNy++++.     :hmNo:...`                |\n |                           :dNN+      .hmmhh+                 .mNN         :dmNo         `hmNs                      |\n |                           :dNN+      `ymmhho`                .mNN         -hmNo         -dmN+                      |\n |                           :dNN+       +mmdhh.                .mNN         -hmNo         -dmN+                      |\n |                           :dNN+       `smmdhs`               .mNN         -hmNo         -dmN+                      |\n |                           :dNN+        `smmdhs-              .mNN         -hmNo         -dmN+                      |\n |                           :dNN+          /dmdhh+.            .mNN         -hmNdssso.    -dmM+                      |\n |                           :dNN+           .ymdhhy.           .mNN         -hdNdhhhs.    -dmM+                      |\n |                           :dNN+             ymmhhy:          .mNN         -hdNo         -dmM+                      |\n |                           :dNN+             `hmmhhs.         .mNN         -hdNo         -dmM+                      |\n |                           :dNN+              .dmdhh:         .mNN         -hdNo         -dmM+                      |\n |                           :dNN+              `ymmhh/         .mNN         -hdNo         -dmM+                      |\n |                           :dNN+              -dmdhh:         .mNN         -hdNo         .dmM+                      |\n |                           :dNN+              ymmhhs.         .mNN         -hdNo          ymNd.                     |\n |                           :dNN+             +mmdhh/          .mNN         -hdNmhyyy-     -ymNms/::`                |\n |                           -syy:            `hmdhho`          `/++         .///++++/.      `:+syhhh-                |\n |                                           .smdhho`                                                                 |\n |                                          -ymdhho`                                                                  |\n |====================================================================================================================|\n !                               !! Saberes as tuas notas nunca foi tão fácil !!                                v.2.0 !\n !                              <NotasCrawler>  Copyright (C) <2018>  <Daniel Vaz>                                    !\n |--------------------------------------------------------------------------------------------------------------------|")


# Função responssável pela seleção do Ctesp
def CtespSelector():
    nome_de_curso = input(
        '\n                         Pretende ver as notas de que CTeSPs? ( Escrever: "RSI,DDM,IG,DPM")  \n<<CTeSP>> ')
    if nome_de_curso == ("RSI") or nome_de_curso == ("rsi"):
        nome_de_curso = "Redes e Sistemas Informáticos"
    elif nome_de_curso == ("DDM") or nome_de_curso == ("ddm"):
        nome_de_curso = "Desenvolvimento para Dispositivos Móveis"
    elif nome_de_curso == ("IG") or nome_de_curso == ("ig"):
        nome_de_curso = "Informática de Gestão"
    elif nome_de_curso == ("DPM") or nome_de_curso == ("dpm"):
        nome_de_curso = "Desenvolvimento de Produtos Multimédia"
    else:
        print("Os dados indicados não são os solicitados!")
        sys.exit()
    return nome_de_curso


# Função responssável pela seleção de Turma
def TurmaSelector():
    nome_de_turma = input(
        '                         Qual é a Turma que pretende ver as notas? ( Escrever: "A","B","Pos") \n<<Turma>> ')
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


# Função responssável pela seleção do Ano
def Ano():
    ano = input(
        '                         Qual dos Anos é que pretende ver as notas? ( Escrever: "1" ou "2") \n<<Ano>> ')
    if ano == "1":
        ano = "1ºAno"
    elif ano == "2":
        ano = "2ºAno"
    else:
        print("Os dados indicados não são os solicitados!")
        sys.exit()
    return ano


# Função responssável pela seleção do Número do Aluno
def NumSelector():
    numero_de_aluno = input(
        '          Pretende ver as notas de toda a Turma, ou de apenas um Aluno? ( "*"= Turma | "(nºAluno)"= Aluno )  \n<<AlunoNº>> ')
    return numero_de_aluno


# Função de escolha de link pendente as opções indicadas pelo utilizador
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


# Obtenção dos dados através das anteriores funções
if __name__ == "__main__":
    nome_de_curso = str(CtespSelector())
    nome_de_turma = str(TurmaSelector())
    ano = str(Ano())
    numero_de_aluno = str(NumSelector())
    url = str(SelectorDeLink())

cls()


# Criação de Directório de armazenamento de PDF's e JPG's
try:
    os.mkdir("Cadeiras")
except BaseException:
    pass


# Criação de Directório de armazenamento de Ficheiros escritos
try:
    os.mkdir("Textos_Tesseract")
except BaseException:
    pass


# Obtenção do Site através do módulo Request
res = requests.get(url)
res.raise_for_status()
res = res.text
soup = bs4.BeautifulSoup(res, "lxml")  # Formatação

# Agrupamento da secçao das notas das cadeiras
container = soup.find("div", class_="content")
# Links Searcher
links = container.find_all_next(href=True, string=nome_de_turma)

# Decorator para contablização do tempo demorado para obter as notas
def Cronometro(f):
    def wraper():
        inicio = time.time()
        f()
        fim = time.time()
        tempo = (fim - inicio) * 1000.0
        tempo = "{0:.4}".format(tempo)
        Frase = f"| Demorou {tempo} ms a obter as suas Notas |"
        print("\n" + Frase.center(120, " "))
    return wraper


# Loop de Apresentação dos Links das notas disponiveis.
@Cronometro
def Loop_SemReconhecimento():
    for link in links:
        link = link["href"]
        url_texto = (link)  # Garantir uma cópia do URL em formato str()
        link = link.split("/")[7]
        link = link.split("-")[0]
        # Tradução da Sigla no URl para nome completo da cadeira
        nome_texto = Cadeira(link)
        print("|====================================================================================================================|")
        print(f"| {nome_texto}:  \n| ")
        print(f"| LINK:  {url_texto}")


# Apresentação final na CLI
print("|====================================================================================================================|")
print(
    f" \n                          Notas Referentes ao Ctesp: {nome_de_curso}  do {ano} \n")

if numero_de_aluno == "*":
    Loop_SemReconhecimento()
else:
    print("                                        Por Favor seja Paciente.")
    print("              Neste momento estão a ser alocados vários recursos para tentar obter as suas Notas")
    Loop_ComReconhecimento(nome_de_curso, ano, numero_de_aluno, links)

print("|====================================================================================================================|")
print("!                                     Espero que esteja tudo OK. Devolva Feedback                                    !")
print("!                                      https://github.com/Daniel-Vaz/NotasCrawler                                    !")
print("!                           --------- NotasCrawler  Copyright (C) 2018  Daniel Vaz ---------                         !")
print("|--------------------------------------------------------------------------------------------------------------------|")
