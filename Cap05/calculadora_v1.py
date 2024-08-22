# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************\n")

def calcular(arg1, arg2,arg3):
    if arg1 == 1:
        operacao = '+'
        return arg2 + arg3, operacao
    elif arg1 == 2:
        operacao = '-'
        return arg2 - arg3, operacao
    elif arg1 == 3:
        operacao = '*'
        return arg2 * arg3, operacao
    elif arg1 == 4:
        operacao = '/'
        return arg2 / arg3, operacao
    else:
        return "Operação inválida!"

print(
    "Selecione o número referente a operação desejada:\n",
    "[1] - Adição;\n",
    "[2] - Subtração;\n",
    "[3] - Multiplicação;\n",
    "[4] - Divisão."
)
opcao = int(input("Opção desejada: "))
valor_1 = float(input("Digite o primeiro valor: "))
valor_2 = float(input("Digite o segundo valor: "))
resultado = calcular(opcao, valor_1, valor_2)
print("%d %s %d = %d" % (valor_1, resultado[1], valor_2, resultado[0]))
print("\n******************* Fim *******************\n")