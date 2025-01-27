#Primeira questao SOMA = 91
#Segunda questao
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    
    return fib_sequence

n = 10
print(f"First {n} Fibonacci numbers: {fibonacci(n)}")
import json
####################################################################################################
#Terceira questao
def calcular_faturamento(dados):
    faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

    menor_faturamento = min(faturamento)
    maior_faturamento = max(faturamento)

    media_mensal = sum(faturamento) / len(faturamento)

    dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

with open('faturamento.json', 'r') as file:
    dados = json.load(file)

menor, maior, dias_acima_media = calcular_faturamento(dados)

print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
####################################################################################################
#Quarta questao
def calcular_percentual_faturamento(faturamento_por_estado):
    total_mensal = sum(faturamento_por_estado.values())
    percentual_por_estado = {estado: (valor / total_mensal) * 100 for estado, valor in faturamento_por_estado.items()}
    return percentual_por_estado

faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

percentual_por_estado = calcular_percentual_faturamento(faturamento_por_estado)

for estado, percentual in percentual_por_estado.items():
    print(f"{estado}: {percentual:.2f}%")
####################################################################################################
# Quinta questao
def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

string_original = "Exemplo de string"
string_invertida = inverter_string(string_original)

print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")
####################################################################################################