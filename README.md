#NotasCrawler - Saberes as tuas notas nunca foi tão fácil!
===============================================
:Info: Um Script escrito em pyhton, que facilita a obtenção das notas dos alunos nos CTESP's do ISTEC. http://www.istec.pt/ctesp/
:Author: Daniel Vaz <dafivaz@hotmail.com>
:Date: 2018-07-28
:Version: 1.5

.. contents::

História \ Sobre
============

Certo dia fartei de ter de fazer sempre o mesmo processo: Abrir browser > Ir ao Site do my.istec > Navegar no site até os Ctesp's RSI > Finalmente andar a fazer scroll para ver se alguma nova nota tinha sido publicada.

Então decidi simplificar a minha vida fazendo um simples Webcrawler capaz de detetar se tinham sido colocadas novas notas no Site e se sim devolver-me o respetivo Link\Nota. Dado o aumento do interesse neste script pelos respetivo colegas de cursso, este Crawler foi evoluindo até aquilo que é hoje.


Requirements
=============================

Para poder executar este script vai ter de garantir os seguintes Requisitos: 

 * Python 3.6 (ou Sup.)
 * Os seguintes Módulos:
    - BeautifullSoup4   - ``pip install beautifullsoup4``
    - Requests          - ``pip install requests``
    - Lxml              - ``pip install lxml``
    - Pillow            - ``pip install Pillow-PIL``
    - Pytesseract       - ``pip install pytesseract``
    - Wand              - ``pip install Wand``
* ImageMagick (https://www.imagemagick.org/script/download.php)
* Google Tesseract OCR (https://github.com/tesseract-ocr/tesseract/wiki)


Getting started
===============



Obstáculos
=================

Quando falamos de um Webcrawler realmente associamos a um script fácil de montar e por a funcionar em pouco tempo e realmente, graças a alguns módulos existentes este processo pode ser automatizado muito facilmente. Contudo estas ferramentas e módulos de forma a tentarem funcionar no maior tipo de cenários possiveis acabam muitas vezes por generalizar o funcionamento do seu código sendo que alguns casos práticos, ao aplicarmos estas ferramentas deparamos-nos sempre com uma vasta variedade de osbtáculos que pendente cada situação podemos abordar a resolução de diferentes prespetivas.

Ao longo deste projecto deparei-me com esses mesmos obstáculos, sendo que acho essencial documentar os mesmo e a maneira que usei para os ultrapassar:

  * O Site do my.istec.pt foi construido com WordPress, e ao analisarmos o código fonte html das páginas onde são postadas as notas dos alunos, deparamos-nos que dentro do <div> responssável por armazenar todos os Módulos, cada linha no ecrã do utilizador tem o seu próprio <TAG>. 
  Porque é que isto é chato ?
  Caso o site tivesse cada módulo desenhado deste modo::
´´´
  <div>
        <h1>Nome do Módulo</h1>
        <a href=link>Link do Módulo</a>
  </div>
´´´
Seria muito mais facil criar um loop para obter os diferentes div's responssáveis por armazenar cada módulo e de uma só vez consseguiamos extrair o Nome da cadeira e o link do pdf das notas. Note-se que isto não é nenhum bicho de seta cabeças mas caso seja verificado no código pode-se ver que tive de utilizar alguns truques de edição do string do url para consseguir decifrar o nome da cadeira por cada url que o crawler obtia. 

  * NÃO EXISTE NENHUM(ou quase nenhum) PADRÃO NOS PDF'S!
  Esta foi a minha maior dificuldade. O que poderia ter sido apenas uma fácil extração de texto dos pdf's que conteem as notas acabou por mostrar-se uma das maiores dificuldades deste projecto dado que os pdf's não são nada mais do que imagens de folhas scanerizadas. 
  Sem grandes complicações  processo acaba por se desenrrolar do seguinte modo:
        - Com o módulo request fasso download dos pdf's para um directório novo;
        - Tomo recurso do módulo Wand.Image para converter os PDF's em JPG's e usar a funcionalidade ("liquid_rescale") que ajuda a remover o aleatório espaço branco nas diferentes imagens;
        - O Módulo Pillow trta da edição da imagem, aplicando filtros e balanciamento de cores;
        - Finalmente o OCR Tesseract pega nas imagens e tenta reconhecer o máximo texto possível.

## Authors
Made By: Daniel Vaz 

License
=======

####################################################################################### 
                Saberes as tuas notas nunca foi tão Fácil !                             
                     Copyright (C) <2018>  <Daniel Vaz>                               
                                                                                       
     This program is free software: you can redistribute it and/or modify             
     it under the terms of the GNU General Public License as published by             
     the Free Software Foundation, either version 3 of the License, or                
     (at your option) any later version.                                              
                                                                                      
     This program is distributed in the hope that it will be useful,                  
     but WITHOUT ANY WARRANTY; without even the implied warranty of                   
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                    
     GNU General Public License for more details.                                     
                                                                                      
     You should have received a copy of the GNU General Public License                
     along with this program.  If not, see <https://www.gnu.org/licenses/>.           
#######################################################################################
