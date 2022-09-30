def sum_squares_equal(n): #Mostra que a soma dos quadrados sempre é igual ao resultado:
    soma = 0
    if not type(n) is int or n< 0:
        print("Não é inteiro, ou menor que 0")
        return 
    for i in range(n+1):
        soma += pow(i,2)
    print(soma)    
    resultado = n*(n+1)*(2*n+1)/6
    print(resultado)
    if resultado == soma:
        return(print("A soma deu igual ao resultado n(n+1)(2n+1)/6"))
    else:
        return("Houve problema no teste")
    
print(sum_squares_equal("a"))