#explicação:
# 
# 
# Neste problema precisamos verificar se um número é "t-primo" — isto é, se ele é o quadrado exato 
# de um número primo. Dado um conjunto de valores F, para cada valor X verificamos: existe um inteiro r
#  tal que r^2 = X e r é primo? Se sim, retornamos "SIM", caso contrário "NÃO". Para eficiência em entradas grandes,
#  construímos um crivo de Eratóstenes até sqrt(max(F)) e depois, para cada X, checamos se é quadrado perfeito e se sua 
# raiz inteira é primo