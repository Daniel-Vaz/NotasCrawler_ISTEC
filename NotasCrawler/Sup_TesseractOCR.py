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
# Este ficheiro tem a Função responsável por armazenar as funções de conversão dos PDF's em JPG's, e consequente manipulação dessas imagens para ficarem legiveis para o Tesseract.
# Estas Funções existe num ficheiro diferente do inicial para simplificar o código do mesmo.
# Script em v.2.0 - Ter em conta que o código pode e deverá ser melhorado.


import bs4
import os
from PIL import Image as PI
from PIL import ImageEnhance, ImageFilter
import pytesseract
import requests
import re
import time
from wand.image import Image
from Sup_CadeirasBD import Cadeira


def Loop_ComReconhecimento(nome_de_curso, ano, numero_de_aluno, links):
    for link in links:
        link = link["href"]
        url_texto = (link)  # Garantir uma cópia do URL em formato str()
        link = link.split("/")[7]
        link = link.split("-")[0]
        # Tradução da Sigla no URl para nome completo da cadeira
        nome_de_cadeira = Cadeira(link)

        # Preparação dos PDF's e diretorios a serem usados temporáriamente
        pdf_download = requests.get(url_texto, allow_redirects=True)
        open(
            f".\\Cadeiras\\{nome_de_cadeira}.pdf",
            "wb").write(
            pdf_download.content)
        pdf_directory = f".\\Cadeiras\\{nome_de_cadeira}.pdf"
        jpg_directory = f".\\Cadeiras\\{nome_de_cadeira}.jpg"

        # Funções de Edição\Reconhecimento respetivamente
        EdiçãoDeImagem(nome_de_cadeira, pdf_directory, jpg_directory)
        TesseractOCR(jpg_directory, numero_de_aluno)

        # Tentativa de Obter nota
        if numero_de_aluno in open(
                r".\Textos_Tesseract\Tesseract_Texto_Editado.txt").read():
            with open(r".\Textos_Tesseract\Tesseract_Texto_Editado.txt") as Texto:
                for linha in Texto:
                    if numero_de_aluno in linha:
                        linhaObtida = linha.strip()
                        try:
                            linhaObtida.split("|")[1]
                        except BaseException:
                            nota_final = "<Não Identificavel>"
                        else:
                            nota_final = linhaObtida.split("|")[1]
                        if nota_final is None or nota_final == "":
                            nota_final = "<Não Identificavel>"
        else:
            nota_final = "<Não Identificavel>"

        os.remove(r".\Textos_Tesseract\Tesseract_Texto.txt")
        os.remove(r".\Textos_Tesseract\Tesseract_Texto_Editado.txt")
        os.remove(pdf_directory)
        print("|====================================================================================================================|")
        print(f"| {nome_de_cadeira}:  \n| ")
        print(f"| NOTA FINAL: {nota_final}")
        print(f"| LINK: {url_texto}")


# Função de Edição de Imagem:
# Converte os PDF's em JPG's com recursso ao modulo Wand.Image;
# Usa o Pillow para editar a Imagem, ficando mais percetivel para o OCR.
def EdiçãoDeImagem(nome_de_cadeira, pdf_directory, jpg_directory):
    with Image(filename=pdf_directory, resolution=400) as img:
        img.format = "jpg"
        img.compression_quality = 99
        img.liquid_rescale(1400, 940)
        img.crop(50, 100, width=1200, height=750)
        img.save(filename=jpg_directory)
    pil_editor = PI.open(jpg_directory)
    enhancer = pil_editor.convert("L")
    enhancer.filter(ImageFilter.SHARPEN)
    enhancer.filter(ImageFilter.EDGE_ENHANCE_MORE)
    enhancer.save(jpg_directory, quality=99)


# Google Tesseract OCR:
# Tentar manipular as configurações de reconhecimento do Tesseract de
# forma a este reconhecer a maior quantidade de texto possivel.
def TesseractOCR(jpg_directory, numero_de_aluno):
    plain_text = pytesseract.image_to_string(
        jpg_directory, lang="por", config="--psm 3")
    EditaTextos(plain_text)


# Função de Manipulação do texto Obtido pelo TesseractOCR
# Esta Função faz várias manipulações do texto obtido.
# Após várias tentativas e analises cheguei a esta formula.
# Caso seja pretendido efectuar testes lembrem-se de inativar as linhas
# responssáveis por eliminar os ficheiros txt
def EditaTextos(plain_text):
    open(r".\Textos_Tesseract\Tesseract_Texto.txt", "w").write(plain_text)
    with open(r".\Textos_Tesseract\Tesseract_Texto.txt") as Texto:
        for linha in Texto:
            SemEspassos = re.sub(r"^\s+", "|", linha.strip())
            SemEspassos = re.sub(r"\D", "|", SemEspassos)
            SemEspassos = re.sub(r"\|", " ", SemEspassos)
            SemEspassos = re.sub(r"\s+", "|", SemEspassos)
            SemEspassos.strip()
            open(
                r".\Textos_Tesseract\Tesseract_Texto_Editado.txt",
                "a").write(
                SemEspassos + "\n")
    open(r".\Textos_Tesseract\Tesseract_Texto_Editado.txt",
         "a").write("\n==================================\n")
