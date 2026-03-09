import random

def tirar1dado ():
    dado=random.randint(1,6)
    return dado

def tirar_dados():
    tirada_counter=1
    dado1= random.randint(1,6)
    dado2= random.randint(1,6)
    dado3= random.randint(1,6)
    dado4= random.randint(1,6)
    dado5= random.randint(1,6)
    tirar_again='V'
    lista_dados=[dado1, dado2, dado3, dado4, dado5]
    print (f'Dado 0: {lista_dados[0]}, Dado 1: {lista_dados[1]}, Dado 2: {lista_dados[2]}, Dado 3: {lista_dados[3]}, Dado 4: {lista_dados[4]}')
    
    tirar_again=input ('Desea tirar los dados de nuevo? (V o F): ')
    while tirada_counter<3 and tirar_again=='V':
        intentos=int(input('Cuantos dados quiere volver a tirar?: '))
        i=1
        while i<=intentos:
            dado_a_tirar=int(input ('Cual dado quiere volver a tirar?: ')) #Recordar 2 try except y reconocer V y F en minus
            lista_dados[dado_a_tirar]=tirar1dado()
            i+=1
        print (f'Dado 0: {lista_dados[0]}, Dado 1: {lista_dados[1]}, Dado 2: {lista_dados[2]}, Dado 3: {lista_dados[3]}, Dado 4: {lista_dados[4]}')
        tirada_counter+=1
        if tirada_counter<3:
            tirar_again=input ('Desea tirar los dados de nuevo? (V o F): ')
    return (lista_dados)

def categorias (lista_dados):
    sorted(lista_dados)             
    lista_categorias=['E', 'F', 'P', 'G', '1', '2', '3', '4', '5', '6']
    cat_elegida=input('Que categoría elige para sus dados?: ')
    
    while cat_elegida not in lista_categorias:
        cat_elegida=input('Eso no es una categoria. Que categoría elige para sus dados?: ')
    
    if cat_elegida=='E':
        puntaje_escalera=0
        is_escalera=True
        for i in range(len(lista_dados)-1):
            if lista_dados[i]+1!=lista_dados[i+1]:
                is_escalera=False
        if not is_escalera:
            print ('Sus dados no califican para entrar a ESCALERA.')
        else:
            puntaje_escalera+=20
    
    if cat_elegida=='F':
        puntaje_full=0
        is_full=True
        if not ((lista_dados[0]==lista_dados[1]==lista_dados[2] and lista_dados[3]==lista_dados[4]) or (lista_dados[0]==lista_dados[1] and lista_dados[2]==lista_dados[3]==lista_dados[4])):
            is_full=False
        if not is_full:
            print ('Sus dados no califican para entrar a FULL.')
        else:
            puntaje_full+=30

    if cat_elegida=='P':
        puntaje_poker=0
        is_poker=True
        if not (lista_dados[0]==lista_dados[1]==lista_dados[2]==lista_dados[3] or lista_dados[1]==lista_dados[2]==lista_dados[3]==lista_dados[4]):
            is_poker=False
        if not is_poker:
            print ('Sus dados no califican para entrar a POKER.')
        else:
            puntaje_poker+=40
    
    if cat_elegida=='G':
        puntaje_generala=0
        is_generala=True
        if not (lista_dados[0]==lista_dados[1]==lista_dados[2]==lista_dados[3]==lista_dados[4]):
            is_generala=False
        if not is_generala:
            print ('Sus dados no califican para entrar a GENERALA.')
        else:
            puntaje_generala+=50
    
    if cat_elegida=='6':
        puntaje_seis=0
        is_seis=True
        for elem in lista_dados:
            if elem==6:
                puntaje_seis+=elem
                
        
        if not (lista_dados[0]==lista_dados[1]==lista_dados[2]==lista_dados[3]==lista_dados[4]):
            is_generala=False
        if not is_seis:
            print ('Sus dados no califican para entrar a GENERALA.')
        else:
            puntaje_generala+=50
    


        
    


def main():
    # Aqui ejecutas tus soluciones
    print(tirar_dados())


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()



