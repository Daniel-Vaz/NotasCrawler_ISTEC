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
# Este ficheiro tem a Função responsável pela Tradução da Sigla no URL para o nome completo do Módulo.
# Existe num ficheiro diferente do inicial para simplificar o código do mesmo.
# Script em v.2.0 - Ter em conta que o código pode e deverá ser melhorado.


# É a nossa "Base de Dados" caso seja necessário mudar alguma disciplina e\ou adicionar uma nova é aqui que fazemos as alterações.
# Note-se que se trata de um Dicionário apenas. Caso seja necessário adicionar uma nova cadeira\módulo devemos adicionar aqui respeitando o formato:
# "(Sigla)": "(Nome Completo)"

Cadeiras_Nomes = {
    "MAT": "Matemática",
    "HI": "História de Informática",
    "RC": "Redes de Computadores",
    "RCA": "Redes de Computadores Avançadas",
    "ANRO": "Avaliação das Necessidades de Rede numa Organização",
    "ACS": "Arquitetura Cliente – Servidor",
    "SR": "Serviços de Rede",
    "ISO": "Introdução aos Sistemas Operativos",
    "CLP": "Comunicar em Língua Portuguesa",
    "IT": "Inglês Técnico",
    "EMP": "Empreendedorismo",
    "AH": "Arquitetura de Hardware",
    "MH": "Montagem de Hardware",
    "DA": "Detecção de Avarias",
    "HRC": "Hardware e Redes de Computadores",
    "IRL": "Instalação de Redes Locais",
    "SD": "Servidor de Dados",
    "CASOS": "Configuração Avançada de Sistemas Operativos Servidores",
    "PS": "Políticas de Segurança",
    "SCE": "Servidor de Correio Eletrónico",
    "CSSL": "Configuração de Serviços num Servidor Linux",
    "SOC": "Sistema Operativo Cliente",
    "SOS": "Sistema Operativo Servidor",
    "SOOS": "Sistemas Operativos Open Source",
    "SOSOS": "Sistema Operativo Servidor Open Source",
    "PT": "Gestão e Manipulação Avançada de Aplicações Informáticas de Processamento de Texto",
    "PC": "Primeiros Conceitos de Programação e Algoritmia e Estruturas de Controlo num Programa Informático",
    "PETD": "Programação Estruturada e Tipos de Dados",
    "POO": "Programação Orientada a Objetos – Introdução",
    "EDECD": "Estrutura de Dados Estática, Composta e Dinâmica",
    "ASEBD": "Análise de Sistemas e Estruturação de Bases de Dados",
    "CEBDSQL": "Criação de Estrutura de Base de Dados em SQL",
    "PSQL": "Programação em SQL",
    "MP": "Metodologia de Projecto",
    "RI": "Redes Informáticas",
    "PDM": "Programação para Dispositivos Móveis I",
    "A3D": "Animação 3D",
    "AED": "Algoritmos e Estruturas de Dados",
    "BD": "Bases de Dados",
    "ADM": "Arquitetura de Dispositivos Móveis",
    "IDM": "Interação com Dispositivos Móveis",
    "FG": "Ferramentas Gráficas",
    "UXUI": "UX/UI Design",
    "PW": "Programação Web",
    "MD": "Marketing Digital",
    "GAMING": "Gaming",
    "Projeto": "Projeto",
    "SO": "Sociologia das Organizações",
    "AG": "Aplicações de Gestão",
    "CF": "Cálculo Financeiro",
    "FC": "Aplicações Informáticas de Folha de Cálculo",
    "MKT": "Marketing",
    "AR": "Administração de Redes",
    "HST": "Higiene e Segurança no Trabalho",
    "DFE": "Direito e Fiscalidade das Empresas",
    "ICC": "Introdução à Ciência dos Computadores",
    "RCD": "Redes e Comunicação de Dados",
    "ASI": "Auditoria e Segurança Informática",
    "GP": "Gestão de Projetos",
    "CVFG": "Comunicação, Visualização e Ferramentas Gráficas",
    "PCAI": "Programação Criativa e Artes Interativas",
    "AMV": "Animação Multimédia e Videojogos",
    "PMDM": "Programação Multimédia e de Dispositivos Móveis",
    "3D": "Computação Gráfica e Animação 3D",
    "TDWD": "Técnicas de Design e Web Design",
    "CTDFSV": "Criação e Tratamento Digital de Fotografia, Som e Vídeo",
    "SIMD": "Sistemas de Informação e Marketing Digital",
    "FAM": "Ferramentas de Autor Multimédia",
}


# Função Tradutora
def Cadeira(link):
    nome_de_cadeira = str(link)
    if nome_de_cadeira in Cadeiras_Nomes:
        nome_de_cadeira = Cadeiras_Nomes[nome_de_cadeira]
    else:
        nome_de_cadeira = "<Módulo não Identificado>"
    return nome_de_cadeira
