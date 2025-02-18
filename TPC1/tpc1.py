def soma_num(texto):
    
    somaTotal = 0
    somador = True
    i = 0
    numTemp = ""
    
    while i < len(texto):
        
        if (texto[i:i+3].lower() == 'off'):
            somador = False
            i = i+2
            
        elif (texto[i:i+2].lower() == 'on'):
            somador = True
            i = i+1
            
        elif (texto[i] == '='):
            print(somaTotal)
            
        elif (texto[i] == '-' and somador and i+1<len(texto)):
            i=i+1
            numTemp = '-'
            while(i < len(texto) and texto[i].isdigit()):
                numTemp += texto[i]
                i = i+1
            somaTotal = somaTotal + (int(numTemp))
            numTemp = ""
            continue
        
        elif (texto[i].isdigit() and somador):
            numTemp += texto[i]
            while(i+1 < len(texto) and texto[i+1].isdigit()):
                numTemp += texto[i+1]
                i = i+1
            
            somaTotal = somaTotal + (int(numTemp))
            numTemp = ""
            i = i+1
            continue
        
        i = i+1
        
    return somaTotal

message = input("Digite a sua Mensagem!\n")
print(soma_num(message))