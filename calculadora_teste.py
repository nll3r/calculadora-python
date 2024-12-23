while True:
    print("Menu de calculadora")
    print("\t1- Adição")
    print("\t2- Subtração")
    print("\t3- Multiplicação")
    print("\t4- Divisão")
    opc = int(input("Qual pretende escolher?: "))
    match opc:
        case 1:
            num1 = int(input("Primeiro número: "))
            num2 = int(input("Segundo número: "))
            total = num1 + num2
            print(f"O total deu {total}")
        case 2:
            num1 = int(input("Primeiro número: "))
            num2 = int(input("Segundo número: "))
            total = num1 - num2
            print(f"O total deu {total}")
        case 3:
            num1 = int(input("Primeiro número: "))
            num2 = int(input("Segundo número: "))
            total = num1 * num2
            print(f"O total deu {total}")
        case 4:
            num1 = int(input("Primeiro número: "))
            num2 = int(input("Segundo número: "))
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
            else:
                total = num1 / num2
                print(f"O total deu {total}")
        case _:
            print("Número incorreto")
    
    continuar = input("Deseja realizar outra operação? (s/n): ")
    if continuar.lower() != 's':
        break