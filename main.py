def localidade():
    
def fora_da_localidade():
    
def autoestrada():
    
    


while True:
    print("Onde circulava o veiculo?")
    print("Escolha uma opção:")
    print("1 - Localidade")
    print("2 - Fora da localidade")
    print("3 - Autoestrada")
    print("0 - Sair")
    
    loc = int(input("Introduza o local: "))

    if loc == "1":
        localidade()
    elif loc == "2":
        fora_da_localidade()
    elif loc == "3":
        autoestrada()
    elif loc == "0":
        print("Calcular multas encerrado!")
        break
    else:
        print("Erro! Introduza um numero de 1 a 3") 