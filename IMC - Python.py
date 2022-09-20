print("Entre com seu peso em kilogramas: ")
peso = float(input("(Ex: 68): "))

print("Entre com sua altura em metros: ")
altura = float(input("(Ex: 1.74): "))


imc = peso/altura**2

print("Seu indice é: %.0f" %imc)

if imc < 16:
	print("Baixo peso Grau III (Severa)")
elif imc < 17:
	print("Baixo peso Grau II (Moderada)")
elif imc < 18.5:
	print("Baixo peso Grau I (Leve)")
elif imc < 25:
	print("Peso adequado")
elif imc < 30:
	print("Obesidade Grau I")
elif imc < 35:
	print("Obesidade Grau II (Severa)")
elif imc < 40:
	print("Obesidade Grau III (Morbida)")
else:
	print("Obesidade")