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
    lista_dados=[dado1, dado2, dado3, dado4, dado5]
    print (f'Dado 0: {lista_dados[0]}, Dado 1: {lista_dados[1]}, Dado 2: {lista_dados[2]}, Dado 3: {lista_dados[3]}, Dado 4: {lista_dados[4]}')
    valido=False
    while not valido:
        tirar_again=input ('Desea tirar los dados de nuevo? (V o F): ')
        if tirar_again=='V' or tirar_again=='F':
            valido=True
        else: 
            print('ingrese V o F')
    while tirada_counter<3 and tirar_again=='V':
        valido=False
        while not valido:
            try:
                intentos=int(input('Cuantos dados quiere volver a tirar?: ')) 
                if intentos<=5:
                    valido=True
                else:
                    print('ingrese un numero valido')
            except:
                print('ingrese un numero valido') 
        i=1
        while i<=intentos:
            valido=False
            while not valido:
                try:
                    dado_a_tirar=int(input ('Cual dado quiere volver a tirar?: ')) 
                    if dado_a_tirar==0 or dado_a_tirar==1 or dado_a_tirar==2 or dado_a_tirar==3 or dado_a_tirar==4:
                        valido=True
                    else:
                        print('ingrese un numero valido')
                except:
                    print('ingrese un numero valido') 
            lista_dados[dado_a_tirar]=tirar1dado()
            i+=1
        print (f'Dado 0: {lista_dados[0]}, Dado 1: {lista_dados[1]}, Dado 2: {lista_dados[2]}, Dado 3: {lista_dados[3]}, Dado 4: {lista_dados[4]}')
        tirada_counter+=1
        if tirada_counter<3:
            tirar_again=input ('Desea tirar los dados de nuevo? (V o F): ')
    return (lista_dados)

def categorias (lista_dados):
    lista_puntajes=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    sorted(lista_dados)             
    lista_categorias=['E', 'F', 'P', 'G', '1', '2', '3', '4', '5', '6']
    print(lista_categorias)
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
            lista_puntajes[0]=puntaje_escalera
    
    if cat_elegida=='F':
        puntaje_full=0
        is_full=True
        if not ((lista_dados[0]==lista_dados[1]==lista_dados[2] and lista_dados[3]==lista_dados[4]) or (lista_dados[0]==lista_dados[1] and lista_dados[2]==lista_dados[3]==lista_dados[4])):
            is_full=False
        if not is_full:
            print ('Sus dados no califican para entrar a FULL.')
        else:
            puntaje_full+=30
            lista_puntajes[1]=puntaje_full

    if cat_elegida=='P':
        puntaje_poker=0
        is_poker=True
        if not (lista_dados[0]==lista_dados[1]==lista_dados[2]==lista_dados[3] or lista_dados[1]==lista_dados[2]==lista_dados[3]==lista_dados[4]):
            is_poker=False
        if not is_poker:
            print ('Sus dados no califican para entrar a POKER.')
        else:
            puntaje_poker+=40
            lista_puntajes[2]=puntaje_poker
    
    if cat_elegida=='G':
        puntaje_generala=0
        is_generala=True
        if not (lista_dados[0]==lista_dados[1]==lista_dados[2]==lista_dados[3]==lista_dados[4]):
            is_generala=False
        if not is_generala:
            print ('Sus dados no califican para entrar a GENERALA.')
        else:
            puntaje_generala+=50
            lista_puntajes[3]=puntaje_generala
    
    if cat_elegida=='6':
        puntaje_seis=0
        is_seis=True
        for elem in lista_dados:
            if elem==6:
                puntaje_seis+=elem
        if puntaje_seis==0:
            print ('Sus dados no califican para entrar a SEIS.')
            is_seis=False
        if is_seis:
            lista_puntajes[9]=puntaje_seis

    if cat_elegida=='5':
        puntaje_cinco=0
        is_cinco=True
        for elem in lista_dados:
            if elem==5:
                puntaje_cinco+=elem
        if puntaje_cinco==0:
            print ('Sus dados no califican para entrar a CINCO.')
            is_cinco=False
        if is_cinco:
            lista_puntajes[8]=puntaje_cinco
    
    if cat_elegida=='4':
        puntaje_cuatro=0
        is_cuatro=True
        for elem in lista_dados:
            if elem==4:
                puntaje_cuatro+=elem
        if puntaje_cuatro==0:
            print ('Sus dados no califican para entrar a CUATRO.')
            is_cuatro=False
        if is_cuatro:
            lista_puntajes[7]=puntaje_cuatro

    if cat_elegida=='3':
        puntaje_tres=0
        is_tres=True
        for elem in lista_dados:
            if elem==3:
                puntaje_tres+=elem
        if puntaje_tres==0:
            print ('Sus dados no califican para entrar a TRES.')
            is_tres=False
        if is_tres:
            lista_puntajes[6]=puntaje_tres

    if cat_elegida=='2':
        puntaje_dos=0
        is_dos=True
        for elem in lista_dados:
            if elem==2:
                puntaje_dos+=elem
        if puntaje_dos==0:
            print ('Sus dados no califican para entrar a DOS.')
            is_dos=False
        if is_dos:
            lista_puntajes[5]=puntaje_dos
    
    if cat_elegida=='1':
        puntaje_uno=0
        is_uno=True
        for elem in lista_dados:
            if elem==1:
                puntaje_uno+=elem
        if puntaje_uno==0:
            print ('Sus dados no califican para entrar a UNO.')
            is_uno=False
        if is_uno:
            lista_puntajes[4]=puntaje_uno
            
    
    
def escribir_csv(lista):  
    with open('jugadas.csv', 'a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(lista)
    


    


        
    


def main():
    # Aqui ejecutas tus soluciones
    print(tirar_dados())


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()



