<p align="center">
    <img src="https://www.svgrepo.com/show/376344/python.svg" height="170" width="195" alt="Python" />
</p>

<h1 align="center">Python 3</h1>


## Tipos estruturados de dados

<p>Em contraposição aos tipos simples, os tipos estruturados são compostos,
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
seu conteúdo alterado, sem que sua instância seja recriada.</p>