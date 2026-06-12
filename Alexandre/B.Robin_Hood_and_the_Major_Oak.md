# Lógica do problema

Neste problema, o objetivo é calcular a quantidade total de folhas presentes
em uma árvore em um determinado ano $X$, levando em conta que as folhas
produzidas em anos anteriores podem ainda estar na árvore.

## Modelagem

Cada ano $i$ produz uma quantidade de folhas igual a $a_i^{a_i}$, onde $a_i$
é o valor de entrada associado àquele ano. As folhas produzidas no ano $i$
permanecem na árvore durante $b_i$ anos consecutivos, ou seja, elas ainda
estão presentes no ano $X$ se a condição abaixo for satisfeita:

$$b_i + a_i - 1 \geq f$$

onde $f$ é o segundo valor do ano atual $X$. Isso equivale a dizer que o
intervalo de permanência das folhas do ano $i$ ainda alcança o ano $X$.

## A função `quantidade(matriz, v)`

A função recebe a matriz com todos os anos registrados até o momento e o
índice $v$ do ano atual, operando em dois casos:

**Caso base** — quando $b_v = 1$ (as folhas duram apenas 1 ano):

$$\text{resultado} = a_v^{a_v}$$

Neste caso, apenas as folhas do próprio ano $X$ estão presentes na árvore,
sem contribuição de anos anteriores.

**Caso geral** — quando $b_v > 1$ (as folhas duram mais de 1 ano):

A função percorre todos os anos anteriores e acumula a contribuição de cada
ano $i$ cujas folhas ainda estejam na árvore no ano $X$, isto é, aqueles que
satisfazem:

$$\texttt{matriz[i][1]} + t - 1 \geq f, \quad \text{com } \texttt{matriz[i]}
\neq \texttt{matriz[v]}$$

O total de folhas presentes na árvore no ano $X$ é então:

$$\text{folhas} = \sum_{\substack{i \,:\, b_i + t - 1 \,\geq\, f \\ i \,\neq\,
v}} a_i^{a_i}$$

## Verificação de paridade

Com o total de folhas calculado, o programa verifica se ele é par ou ímpar:

$$\text{total} \mod 2 = \begin{cases} 0 & \Rightarrow \texttt{True} \quad
\text{(quantidade par de folhas)} \\ 1 & \Rightarrow \texttt{False} \quad
\text{(quantidade ímpar de folhas)} \end{cases}$$

## Fluxo geral

O programa recebe o número de casos de teste $T$ e, para cada caso, lê o ano
$a$ e o tempo de permanência das folhas $b$. A cada novo caso, a função
`quantidade` consulta todos os anos já registrados, soma as contribuições
válidas e imprime `True` se o total for par ou `False` se for ímpar.