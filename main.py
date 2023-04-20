grau = int(input( "digite qual o grau de aprovação, só pode ser do primeiro e do segundo grau"))
if grau==1:
      print("a aprovação é do primeiro grau")
      valorA= flot(input("digite o valor de a"))
      if valorA == 0 :
          print("valor invalido")
      else:
          valorB = float(input("digite o valor B"))
          print(f"a raiz da aprovação '{valorA} * x + {valorB} = 0' é { - valorB / valorA :.2f} ")
         
elif grau == 2:
    print ("A aprovação é do segundo grau")
    valorA = float (input("digite o valor do a"))
    if valorA ==0:
        print("valor de um invalido")
    else:
        valorB = flot (input ("digite o valor de b"))
        valorC = flot (input("digite o valor de c"))
        delta = valorB ** 2 - 4 * valorA * valorC
        if delta < 0:
            print("A emissão não possui raízes reais")
        elif delta == 0:
                print(" A emissão possui apenas uma raízes real")
                print (f" o valor da raiz é { - valorB / (2 * valorA):.2f } ")
        elif delta >0 :
            print ("A emissão possui duas raízes reais")
            resposta = delta 
            resposta = resposta **0,5
            resposta2 = (- valorB + resposta) / (2* valorA)
            resposta3 = (- valorB - resposta ) / (2* valorA)
            print(f"o valor de x1 é { resposta2 :.2f} " )
            print(f"o valor de x2 é { resposta3 :.2f} ")
else:
    print("grau invalido")
                        