# NotasCrawler - Saberes as tuas notas nunca foi tão fácil!
<p align="center">
    <a href="#">
        <img src="https://forthebadge.com/images/badges/made-with-python.svg"/> </a>
</p>

Um Script escrito em Pyhton, que facilita a obtenção das notas dos alunos nos CTESP's do [ISTEC](http://www.istec.pt/ctesp/). 

Este projecto começou por iniciativa prória, nunca estando este diretamente associado ao Instituo Superior de Tecnologias Avançadas.


**Made By:** Daniel Vaz 
<a href="https://aimeos.org/">
    <img src="http://www.ocupacional.pt/cursos/istec.png" title="ISTEC" align="right" width="300" height="85" />
</a>

**Version:** 2.0

## História \ Sobre

Certo dia fartei de ter de fazer sempre o mesmo processo:

>Abrir browser > Ir ao Site do my.istec > Navegar no site até os Ctesp's RSI > Finalmente andar a fazer scroll para ver se alguma nova nota tinha sido publicada.

Então decidi simplificar a minha vida fazendo um simples Webcrawler capaz de detetar se tinham sido colocadas novas notas no Site e se sim devolver-me o respetivo Link\Nota. Dado o aumento do interesse neste script pelos respetivo colegas de cursso, este Crawler foi evoluindo até aquilo que é hoje.

**Qualquer pessoa que tenha alguma recomendação para o projecto é livre de se pronunciar! Todo o feedback é Bem Vindo!**


<img src="https://media.giphy.com/media/8PvAjFc4OVR79lQBoJ/giphy.gif" title="Apresentação GIF" align="middle"/>


## Requirements
Para poder executar este script vai ter de garantir os seguintes Requisitos: 

 * [Python 3.6 (ou Sup.)](https://www.python.org/downloads/)
 * Os seguintes Módulos:
    - BeautifullSoup4   - ``pip install beautifullsoup4``
    - Requests          - ``pip install requests``
    - Lxml              - ``pip install lxml``
    - Pillow            - ``pip install Pillow-PIL``
    - Pytesseract       - ``pip install pytesseract``
    - Wand              - ``pip install Wand``
* [ImageMagick](https://www.imagemagick.org/script/download.php)
* [GhostScript](https://www.ghostscript.com/download/gsdnld.html)
* [Google Tesseract OCR](https://github.com/tesseract-ocr/tesseract/wiki)


### Getting started

Antes de mais para garantirmos o bom funcionamento do script devemos garantir que todos os requisitos indicados acima estão garantidos.

De seguida é apenas efectuar o download do [NotasCrawler_ISTEC](https://github.com/Daniel-Vaz/NotasCrawler_ISTEC.git), e executar o ficheiro NotasCrawler.py .

Ao executarmos o Ficheiro devemos responder sempre a 4 questões:

- Qual o CTeSP que queremos ver;
- Qual a Turma;
- Qual o Ano;
- E finalmente se é pretendido ver as Notas de toda a turma ou de apenas 1 aluno;

Nesta ultima questão é que o programa se "Subdivide", ou seja, caso seja escolhido a opção de ver as notas de toda a turma, o script apenas irá obter os Módulos disponiveis com notas finais e os respectivos links para serem vizualisados os PDF's com as notas. Contudo caso seja introduzido um numero de aluno, o script irá fazer o Download dos PDF's, converte-los para JPG's e tomar recurso do Tesseract para **tentar**  recuperar a respetiva nota do aluno em questão.

 >Reforço o **tentar** isto porque dado as condições com que os pdf's são submetidos no site nem sempre é possivel obter a nota pretendida.


## Obstáculos do Projecto
Quando falamos de um Webcrawler realmente associamos a um script fácil de montar e por a funcionar em pouco tempo e realmente, graças a alguns módulos existentes este processo pode ser automatizado muito facilmente. Contudo estas ferramentas e módulos de forma a tentarem funcionar no maior tipo de cenários possiveis acabam muitas vezes por generalizar o funcionamento do seu código sendo que em alguns casos práticos, ao aplicarmos estas ferramentas deparamos-nos sempre com uma vasta variedade de osbtáculos que pendente cada situação podemos abordar a resolução através de diferentes prespetivas.

Ao longo deste projecto deparei-me com esses mesmos obstáculos, sendo que acho essencial documentar os mesmo e a maneira que usei para os ultrapassar:

  * O Site my.istec.pt foi construido sobre WordPress, e ao analisarmos o código fonte html das páginas onde são postadas as notas dos alunos, deparamos-nos que dentro do div responssável por armazenar todos os Módulos, cada linha na source tem o seu próprio TAG:


```html
(exemplo)
<h2></h2>
<h4>Módulo01</h4>
<p><a href="http:\\link.exemplo.pt\ano\turmaA\modulo01.pdf" target="_blank">Turma A</a><br />
<a href="http:\\link.exemplo.pt\ano\turmaB\modulo01.pdf" target="_blank">Turma B</a></p>
<h4>Modulo02</h4>
<p><a href="http:\\link.exemplo.pt\ano\turmaA\modulo02.pdf" target="_blank">Turma A</a><br />
<a href="http:\\link.exemplo.pt\ano\turmaB\modulo02.pdf" target="_blank">Turma B</a></p>
etc...
```


  Porque é que isto é chato ?
  Caso o site tivesse cada módulo desenhado deste modo:


```html
  <div>
        <h1>Nome do Módulo</h1>
        <a href=link>Link do Módulo</a>
  </div>
```


Seria muito mais facil criar um loop para obter os diferentes div's responssáveis por armazenar cada módulo e de uma só vez consseguiamos extrair o Nome da cadeira e o link do pdf das notas. Note-se que isto não é nenhum bicho de seta cabeças mas caso seja verificado no código deste script, pode-se ver que tive de utilizar alguns truques de edição do string do url para consseguir decifrar o nome da cadeira por cada url que o crawler obtia. 

  * **NÃO EXISTE NENHUM(ou quase nenhum) PADRÃO NOS PDF's!**

Esta foi a minha maior dificuldade. O que poderia ter sido apenas uma fácil extração de texto dos pdf's que conteem as notas acabou por mostrar-se uma das maiores dificuldades deste projecto dado que os pdf's não são nada mais do que imagens de folhas scanerizadas. 
 
 Sem grandes complicações o processo acaba por se desenrrolar do seguinte modo:

- Com o módulo request fasso download dos pdf's para um directório novo;

- Tomo recurso do módulo Wand.Image para converter os PDF's em JPG's e usar a funcionalidade ("liquid_rescale") que ajuda a remover o aleatório espaço branco nas diferentes imagens;

- O Módulo Pillow trata da edição da imagem, aplicando filtros e balanciamento de cores;

- Finalmente o OCR Tesseract pega nas imagens e tenta reconhecer o máximo texto possível.
No final este texo todo é armazenado de forma a tentar-se obter o valor final da nota do Utilizador.

## License
Copyright (C) 2018  Daniel Vaz   

[gpl-3.0](https://choosealicense.com/licenses/gpl-3.0/)
