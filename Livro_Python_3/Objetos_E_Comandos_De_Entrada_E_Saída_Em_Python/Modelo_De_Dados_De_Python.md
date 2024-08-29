<p align="center">
    <img src="https://www.svgrepo.com/show/376344/python.svg" height="170" width="195" alt="Python" />
</p>

<h1 align="center">Python 3</h1>


## Modelo de dados de Python

<p>No contexto de linguagens de programação, a expressão “modelo de
dados” diz respeito à abordagem, aos paradigmas e às técnicas adotadas no
projeto conceitual da linguagem, visando definir a maneira como os dados
serão mantidos em memória e acessados pelo conjunto de instruções.

O modelo de dados do Python (Python Data Model, em inglês) adota como
paradigma que todo dado em um programa escrito com Python é
representado por um <b>objeto</b>. Todo objeto Python tem três aspectos: um
identificador, um tipo e um conteúdo.

O <b>identificador</b> é o nome que o objeto tem no programa.

O tipo do <b>objeto</b> determina não só a natureza dos dados que este armazena
(por exemplo, um número inteiro, um texto), mas também as operações que
são suportadas por ele. Cada objeto em Python é criado a partir de uma classe
(class), que é um elemento do paradigma de programação conhecida como
programação orientada a objetos. Assim,
um objeto do tipo <i>“int”</i> (número inteiro) terá associado a si um conjunto de
funções adequadas à manipulação de números inteiros; um outro objeto do
tipo <i>“list”</i> (lista) terá outras funções que se adequam à manipulação de listas;
e assim por diante.

E o <b>conteúdo</b> do objeto, que é o valor (ou conjunto de valores)
armazenado nele.

Exemplo:

Objetos em Python

 <b>MeuObjeto = 10

 type(MeuObjeto)
 
 class ‘int’</b>

 <footer>* Usou-se o comando type( ) para saber qual o tipo da "Variavel/Objeto".</footer></p> 
 
<p>No Exemplo, podem ser vistos os três aspectos mencionados: o
identificador é MeuObjeto; o tipo é “int”, que representa números inteiros; e
o conteúdo é o valor 10.

Considerando o que foi exposto, a conclusão imediata é que em Python não
existem <b>variáveis</b>, como estas costumam ser conhecidas em outras
linguagens. O que existe, de fato, são os <b>objetos</b>. Pode parecer uma simples
questão de nomenclatura, mas não se trata disso, uma vez que cada objeto,
além de ser utilizado para armazenar seu conteúdo, apresenta um
comportamento próprio associado à classe a que pertence.</p>