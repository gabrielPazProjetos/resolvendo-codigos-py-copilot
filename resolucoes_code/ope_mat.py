num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

if operacao == '+':
    resultado = num1 + num2
    print(f"Resultado da soma: {resultado}")
elif operacao == '-':
    resultado = num1 - num2
    print(f"Resultado da subtração: {resultado}")
elif operacao == '*':
    resultado = num1 * num2
    print(f"Resultado da multiplicação: {resultado}")
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado da divisão: {resultado}")
    else:
        print("Erro: divisão por zero não é permitida.")
else:
    print("Operação inválida. Use apenas +, -, * ou /.")
