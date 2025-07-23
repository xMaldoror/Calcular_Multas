#Front_end_1.1
print("Bem vindo ao Calculador de Multas\n")

#Conceitos operativos 
#Front_end_1.2
while True:    
    try:
        velocidade = float(input("A que velocidade circulava: "))
        break
    except ValueError:
        print("Erro: a velocidade deve ser um número inteiro positivo.")
        
#Funções
def localidade():
    if velocidade > 50:
        print("\n-->A sua multa será de 60€<--")
    elif velocidade >= 90:
        print("\n-->A sua multa será de 120€<--")
    elif velocidade >= 120:
        print("\n-->A sua  multa será de 320€<--")
    
def fora_da_localidade():
    if velocidade > 90:
        print("\n-->A sua multa será de 60€<--")
    elif velocidade >= 120:
        print("\n-->A sua  multa será de 120€<--")

def autoestrada():
    if velocidade > 120:
        print("\n-->A sua multa será de 60€<--")
    elif velocidade >= 150:
        print("\n-->A sua multa será de 120€<--")
    elif velocidade >= 175:
        print("\n-->A sua  multa será de 360€<--")
    

#Front_end_2
while True:
    print("\nOnde circulava o veiculo?")
    print("Escolha uma opção:")
    print("1 - Localidade")
    print("2 - Fora da localidade")
    print("3 - Autoestrada")
    print("0 - Sair")
    
    loc = int(input("\nIntroduza o local: "))
    

    if loc == 1:
        localidade()
    elif loc == 2:
        fora_da_localidade()
    elif loc == 3:
        autoestrada()
    elif loc == 0:
        print("Calcular multas encerrado!")
        break
    else:
        print("Erro! Introduza um numero de 1 a 3") 