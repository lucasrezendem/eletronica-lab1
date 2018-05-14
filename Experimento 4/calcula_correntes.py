arquivoNome = ["tabela10V","tabela5V","tabela0V"]
vcc = [10,5,0]
i=0
Rc = 99.62
Rb = 9890
for nome in arquivoNome:
  arq = nome+".txt"
  arquivo = open(str(arq))
  print(arq)
  for linha in arquivo:
    termos = linha.split(" |")
    Vbb = float(termos[0])
    Vbe = float(termos[1])
    Vce = float(termos[2])
    Ib = (Vbb-Vbe)/Rb
    Ic = (vcc[i]-Vce)/Rc
    print("Ib = " + Ib.__str__())
    print("Ic = " + Ic.__str__())
    print("===========================================")
  i+=1
