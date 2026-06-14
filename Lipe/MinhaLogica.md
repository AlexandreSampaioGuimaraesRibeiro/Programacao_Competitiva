# Lógica do Code forces numero: 1899A - Game with Integers

O programa começa lendo a quantidade de casos de teste que serão analisados.

quantidade_testes = int(input())

Em seguida, é utilizado um laço de repetição para processar cada caso de teste individualmente.

for teste in range(quantidade_testes):

Dentro do laço, o número informado pelo usuário é lido e armazenado na variável numero.

numero = int(input())

Após isso, é calculado o resto da divisão do número por 3 utilizando o operador módulo (%).

resto = numero % 3

Quando o resto é igual a 0, significa que o número é divisível por 3. Em seguida, uma estrutura condicional verifica o valor do resto.

if resto == 0:
    vencedor = "Second"
else:
    vencedor = "First"

Se o resto for 0, a variável vencedor recebe "Second".
Caso contrário, recebe "First". Por fim, o reultado é exibido na tela.
print(vencedor)

Complexidade:

Para cada caso de teste, o programa realiza apenas uma leitura de entrada, uma operação de módulo, uma verificação condicional, uma saída. Dessa forma, o tempo de execução é O(1) para cada caso de teste.

