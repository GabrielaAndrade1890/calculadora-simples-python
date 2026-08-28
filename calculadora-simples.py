print('| CALCULADORA SIMPLES |')
print('========================')

numero1 = float(input('Digite o primeiro número: '))
print()
numero2 = float(input('Digite o segundo número: '))
print()

print('Escolha a operação básica:')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print()

operacao = input('Digite o número da operação desejada: ')
print()

if operacao == '1':
    resultado = numero1 + numero2
    print(f'O resultado da soma foi: {resultado}')
elif operacao == '2':
    resultado = numero1 - numero2
    print(f'O resultado da subtração foi: {resultado}')
elif operacao == '3':
    resultado = numero1 * numero2
    print(f'O resultado da multiplicação foi: {resultado}')
elif operacao == '4':
    resultado = numero1 / numero2
    print(f'O resultado da divisão foi: {resultado}')