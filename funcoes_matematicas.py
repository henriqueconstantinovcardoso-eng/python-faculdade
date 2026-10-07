def potencia(base, expoente):
    # Caso base: qualquer número elevado a 0 é 1
    if expoente == 0:
        return 1
    # Passo recursivo
    else:
        return base * potencia(base, expoente - 1)

def multiplicacao_recursiva(a, b):
    if b == 0:
        return 0
    else:
        return a + multiplicacao_recursiva(a, b - 1)

print("=== Testando Funções Recursivas ===")
b = int(input("Informe a base da potência: "))
e = int(input("Informe o expoente (positivo): "))

resultado_pot = potencia(b, e)
print(f"O resultado de {b} elevado a {e} é: {resultado_pot}")

num1 = int(input("Informe o primeiro número para multiplicação: "))
num2 = int(input("Informe o segundo número para multiplicação: "))
resultado_mult = multiplicacao_recursiva(num1, num2)
print(f"O produto de {num1} x {num2} calculado recursivamente é: {resultado_mult}")
