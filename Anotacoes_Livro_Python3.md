<p align="center">
    <img src="https://www.svgrepo.com/show/376344/python.svg" height="170" width="195" alt="Python" />
</p>

<h1 align="center">Python 3</h1>



## Objetos e Comandos de Entrada e Saída em Python


<p> Em essência, para ser útil, um programa de computador precisa ser capaz
de receber dados de entrada, armazená-los em algum lugar, manipulá-los de
algum modo, produzindo resultados, e, por fim, exibi-los de maneira
apropriada, por meio de algum dispositivo.</p>

<p>Desse modo, serão apresentados os objetos e os tipos de dados disponíveis
na linguagem Python, os quais permitem o armazenamento de dados e sua
manipulação, bem como serão vistos os comandos da linguagem utilizados
para exibição em tela e leitura de dados do teclado.</p>

### Objetos e classes: Conceito de variáveis

<p>Para que um algoritmo possa ser implementado em um computador, é
preciso que exista um meio de armazenamento dos dados que serão
manipulados. Assim, chega-se ao conceito existente em todas as linguagens
de programação e que é usualmente designado pelo termo “variável”.</p>

<p>Em programação de computadores, uma variável é um elemento da
linguagem que ocupa um ou mais bytes na memória RAM do computador.
Esse local da memória é capaz de reter, ou seja, armazenar o elemento de
dado. No programa, a variável é identificada por um nome ou identificador. Por exemplo:

<b>idade = 36</b>

Assim, pode-se entender que do ponto de vista do programador a variável 'idade' é
um nome que contém o dado '36', e do ponto de vista do computador a variável 'idade'
é um endereço de memória que retém um conjunto de bits que representam
esse dado '36'.</p>

### Modelo de dados de Python

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
 
No Exemplo, podem ser vistos os três aspectos mencionados: o
identificador é MeuObjeto; o tipo é “int”, que representa números inteiros; e
o conteúdo é o valor 10.

Considerando o que foi exposto, a conclusão imediata é que em Python não
existem <b>variáveis</b>, como estas costumam ser conhecidas em outras
linguagens. O que existe, de fato, são os <b>objetos</b>. Pode parecer uma simples
questão de nomenclatura, mas não se trata disso, uma vez que cada objeto,
além de ser utilizado para armazenar seu conteúdo, apresenta um
comportamento próprio associado à classe a que pertence.
    
### Tipos simples de dados

Em Python, estão disponíveis
os tipos simples relacionados a seguir.

<b>• Número inteiro (int)</b>: capazes de armazenar números inteiros
positivos, zero ou negativos.

<b>• Número real (float)</b>: capazes de armazenar números reais positivos ou
negativos, além do zero. O separador decimal é o ponto “.”.

<b>• Boleano (bool)</b>: armazena valores lógicos (True ou False). 
O valor True pode ser representado por 1 e o False 
por 0 e, por isso, alguns autores consideram valores 
do tipo bool como sendo do tipo inteiro

<b>• Número complexo (complex)</b>: armazena um número complexo do tipo
4 + 3j (note-se, na parcela imaginária, que é utilizada a letra “j” em vez
da letra “i”).

A linguagem Python tem suporte completo às operações
aritméticas envolvendo números complexos. Essa característica é
muito útil em programas voltados à solução de problemas de física e
engenharia, nos quais há uma forte presença de números complexos,
por exemplo, estudo de vibrações, circuitos elétricos e sistemas
dinâmicos.



### Tipos estruturados de dados

Em contraposição aos tipos simples, os tipos estruturados são compostos,
ou seja, seu conteúdo é constituído por outros elementos. Assim sendo, tais
tipos representam agregados de objetos que podem ser acessados e
manipulados em conjunto ou isoladamente.
Os tipos compostos mais importantes para esta fase do aprendizado são:

<b>• Cadeia de texto (str)</b>: também denominados strings, objetos deste tipo
contêm qualquer sequência de caracteres, incluindo letras, algarismos e
caracteres especiais. Servem para armazenar nomes, endereços, texto
em geral, bem como quaisquer dados aos quais não se aplicam ou não
se realizam operações aritméticas.

<b>• Lista (list)</b>: de todos os tipos disponíveis em Python, é um dos mais
versáteis e poderosos. Uma lista caracteriza-se por ser um conjunto de
itens entre colchetes e separados por vírgulas. Os itens não precisam
ser todos do mesmo tipo e podem ser acessados e manipulados
individualmente, todos de uma vez ou em grupos. Este é um tipo
mutável.


<b>• Tupla (tuple)</b>: são semelhantes às listas, no entanto, seus componentes
não podem ser alterados. Este é um tipo imutável. Uma tupla
caracteriza-se por ser um conjunto de itens entre parênteses e separados
por vírgulas.


<b>• Conjunto (set e frozenset)</b>: um conjunto é uma coleção não ordenada
de elementos não duplicados e caracteriza-se por itens entre chaves e
separados por vírgulas. Tem diversos usos possíveis e suporta
operações matemáticas típicas de conjuntos, como união, interseção e
diferença, muito úteis em alguns algoritmos. O tipo set é mutável,
enquanto que frozenset é imutável.


<b>• Dicionário (dict)</b>: também designado como tipo mapeado, um
dicionário é uma coleção de pares “chave:valor” não ordenados, com a
obrigatoriedade de que as chaves sejam únicas (não duplicadas) dentro
do dicionário. Enquanto as listas e tuplas são indexadas por um número
inteiro, os dicionários são indexados pela chave associada ao valor.
Dicionários são mutáveis.

Os objetos existentes na linguagem podem ser classificados como
<b>imutáveis</b> <i>(immutables)</i> ou <b>mutáveis</b> <i>(mutables)</i>. Um objeto imutável tem
conteúdo fixo, ou seja, não pode ser alterado sem que o objeto seja
reconstruído. Os tipos numéricos (int, float, complex), os strings, tuplas e
frozenset são imutáveis, de modo que, quando um novo conteúdo for
atribuído ao objeto, sua instância anterior é removida, e uma nova instância,
criada. Os tipos lista, dicionário e set são mutáveis, de modo que podem ter
seu conteúdo alterado, sem que sua instância seja recriada.
