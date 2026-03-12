import random
import csv


def guardar_tabla_csv(lista_puntaje):
    categorias_csv = ['E', 'F', 'P', 'G', '1', '2', '3', '4', '5', '6']

    with open("jugadas.csv", "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["jugada", "j1", "j2"])

        for i in range(len(categorias_csv)):
            valor_j1 = lista_puntaje[0][i]
            valor_j2 = lista_puntaje[1][i]

            if valor_j1 is None:
                valor_j1 = ""
            if valor_j2 is None:
                valor_j2 = ""

            writer.writerow([categorias_csv[i], valor_j1, valor_j2])


def crear_archivo_jugadas(lista_puntaje):
    guardar_tabla_csv(lista_puntaje)


def tirar1dado():
    return random.randint(1, 6)


def es_generala(lista_dados):
    dados_ordenados = sorted(lista_dados)
    return dados_ordenados[0] == dados_ordenados[1] == dados_ordenados[2] == dados_ordenados[3] == dados_ordenados[4]


def tirar_dados():
    tirada_counter = 1

    lista_dados = [
        random.randint(1, 6),
        random.randint(1, 6),
        random.randint(1, 6),
        random.randint(1, 6),
        random.randint(1, 6)
    ]

    primera_tirada = lista_dados[:]

    print(f'Dado 0: {lista_dados[0]}, Dado 1: {lista_dados[1]}, Dado 2: {lista_dados[2]}, Dado 3: {lista_dados[3]}, Dado 4: {lista_dados[4]}')

    valido = False
    while not valido:
        tirar_again = input('Desea tirar los dados de nuevo? (V o F): ').upper()
        if tirar_again == 'V' or tirar_again == 'F':
            valido = True
        else:
            print('Ingrese V o F')

    planto_primera_tirada = False
    generala_real = False

    if tirar_again == 'F':
        planto_primera_tirada = True
        if es_generala(lista_dados):
            generala_real = True
        return lista_dados, planto_primera_tirada, generala_real

    while tirada_counter < 3 and tirar_again == 'V':
        valido = False
        while not valido:
            try:
                intentos = int(input('Cuantos dados quiere volver a tirar?: '))
                if 0 <= intentos <= 5:
                    valido = True
                else:
                    print('Ingrese un numero valido')
            except ValueError:
                print('Ingrese un numero valido')

        if intentos == 0 and tirada_counter == 1:
            planto_primera_tirada = True
            if es_generala(lista_dados):
                generala_real = True
            return lista_dados, planto_primera_tirada, generala_real

        dados_ya_elegidos = []

        i = 1
        while i <= intentos:
            valido = False
            while not valido:
                try:
                    dado_a_tirar = int(input('Cual dado quiere volver a tirar?: '))
                    if dado_a_tirar in [0, 1, 2, 3, 4]:
                        if dado_a_tirar not in dados_ya_elegidos:
                            valido = True
                        else:
                            print('Ese dado ya fue elegido en esta tirada')
                    else:
                        print('Ingrese un numero valido')
                except ValueError:
                    print('Ingrese un numero valido')

            dados_ya_elegidos.append(dado_a_tirar)
            lista_dados[dado_a_tirar] = tirar1dado()
            i += 1

        print(f'Dado 0: {lista_dados[0]}, Dado 1: {lista_dados[1]}, Dado 2: {lista_dados[2]}, Dado 3: {lista_dados[3]}, Dado 4: {lista_dados[4]}')

        tirada_counter += 1

        if tirada_counter < 3:
            valido = False
            while not valido:
                tirar_again = input('Desea tirar los dados de nuevo? (V o F): ').upper()
                if tirar_again == 'V' or tirar_again == 'F':
                    valido = True
                else:
                    print('Ingrese V o F')

    return lista_dados, planto_primera_tirada, generala_real


def pedir_categoria_disponible(jugador, lista_puntaje):
    lista_categorias = ['E', 'F', 'P', 'G', '1', '2', '3', '4', '5', '6']
    disponibles = []

    for i in range(len(lista_categorias)):
        if lista_puntaje[jugador][i] is None:
            disponibles.append(lista_categorias[i])

    print("Categorias disponibles:", disponibles)

    cat_elegida = input('Que categoría elige para sus dados?: ').upper()
    while cat_elegida not in disponibles:
        cat_elegida = input('Esa categoria no esta disponible. Que categoría elige?: ').upper()

    return cat_elegida


def pedir_categoria_de_lista(lista_categorias_validas):
    print("Categorias validas disponibles:", lista_categorias_validas)

    cat_elegida = input('Debe elegir una categoria valida: ').upper()
    while cat_elegida not in lista_categorias_validas:
        cat_elegida = input('Esa categoria no es valida. Debe elegir una categoria valida: ').upper()

    return cat_elegida


def pedir_categoria_para_cero(jugador, lista_puntaje):
    lista_categorias = ['E', 'F', 'P', 'G', '1', '2', '3', '4', '5', '6']
    disponibles = []

    for i in range(len(lista_categorias)):
        if lista_puntaje[jugador][i] is None:
            disponibles.append(lista_categorias[i])

    print("No hay jugadas validas disponibles.")
    print("Debe elegir una categoria pendiente para anotarse 0.")
    print("Categorias pendientes:", disponibles)

    cat_elegida = input('Que categoría elige para anotarse 0?: ').upper()
    while cat_elegida not in disponibles:
        cat_elegida = input('Esa categoria no esta disponible. Que categoría elige?: ').upper()

    return cat_elegida


def obtener_indice_categoria(cat_elegida):
    if cat_elegida == 'E':
        return 0
    elif cat_elegida == 'F':
        return 1
    elif cat_elegida == 'P':
        return 2
    elif cat_elegida == 'G':
        return 3
    elif cat_elegida == '1':
        return 4
    elif cat_elegida == '2':
        return 5
    elif cat_elegida == '3':
        return 6
    elif cat_elegida == '4':
        return 7
    elif cat_elegida == '5':
        return 8
    else:
        return 9


def calcular_puntaje_categoria(lista_dados, cat_elegida, planto_primera_tirada):
    dados = sorted(lista_dados)
    puntaje = 0
    entra = False

    if cat_elegida == 'E':
        if dados == [1, 2, 3, 4, 5] or dados == [2, 3, 4, 5, 6]:
            puntaje = 20
            if planto_primera_tirada:
                puntaje += 5
            entra = True

    elif cat_elegida == 'F':
        if ((dados[0] == dados[1] == dados[2] and dados[3] == dados[4]) or
            (dados[0] == dados[1] and dados[2] == dados[3] == dados[4])):
            puntaje = 30
            if planto_primera_tirada:
                puntaje += 5
            entra = True

    elif cat_elegida == 'P':
        if (dados[0] == dados[1] == dados[2] == dados[3] or
            dados[1] == dados[2] == dados[3] == dados[4]):
            puntaje = 40
            if planto_primera_tirada:
                puntaje += 5
            entra = True

    elif cat_elegida == 'G':
        if dados[0] == dados[1] == dados[2] == dados[3] == dados[4]:
            puntaje = 50
            entra = True

    elif cat_elegida == '1':
        for elem in dados:
            if elem == 1:
                puntaje += 1
        if puntaje > 0:
            entra = True

    elif cat_elegida == '2':
        for elem in dados:
            if elem == 2:
                puntaje += 2
        if puntaje > 0:
            entra = True

    elif cat_elegida == '3':
        for elem in dados:
            if elem == 3:
                puntaje += 3
        if puntaje > 0:
            entra = True

    elif cat_elegida == '4':
        for elem in dados:
            if elem == 4:
                puntaje += 4
        if puntaje > 0:
            entra = True

    elif cat_elegida == '5':
        for elem in dados:
            if elem == 5:
                puntaje += 5
        if puntaje > 0:
            entra = True

    elif cat_elegida == '6':
        for elem in dados:
            if elem == 6:
                puntaje += 6
        if puntaje > 0:
            entra = True

    return puntaje, entra


def obtener_categorias_validas(lista_dados, jugador, lista_puntaje, planto_primera_tirada):
    lista_categorias = ['E', 'F', 'P', 'G', '1', '2', '3', '4', '5', '6']
    categorias_validas = []

    for i in range(len(lista_categorias)):
        if lista_puntaje[jugador][i] is None:
            puntaje, entra = calcular_puntaje_categoria(lista_dados, lista_categorias[i], planto_primera_tirada)
            if entra:
                categorias_validas.append(lista_categorias[i])

    return categorias_validas


def categorias(lista_dados, jugador, lista_puntaje, planto_primera_tirada):
    categorias_validas = obtener_categorias_validas(lista_dados, jugador, lista_puntaje, planto_primera_tirada)

    if len(categorias_validas) == 0:
        categoria_cero = pedir_categoria_para_cero(jugador, lista_puntaje)
        indice_cero = obtener_indice_categoria(categoria_cero)
        lista_puntaje[jugador][indice_cero] = 0
        print(f'Se anotaron 0 puntos en la categoria {categoria_cero}.')
        guardar_tabla_csv(lista_puntaje)
        return lista_puntaje

    cat_elegida = pedir_categoria_disponible(jugador, lista_puntaje)
    puntaje, entra = calcular_puntaje_categoria(lista_dados, cat_elegida, planto_primera_tirada)

    while not entra:
        print(f'Sus dados no califican para entrar a {cat_elegida}.')
        print('Debe elegir una categoria valida entre las disponibles para esta jugada.')
        cat_elegida = pedir_categoria_de_lista(categorias_validas)
        puntaje, entra = calcular_puntaje_categoria(lista_dados, cat_elegida, planto_primera_tirada)

    indice = obtener_indice_categoria(cat_elegida)
    lista_puntaje[jugador][indice] = puntaje
    print(f'La jugada entra en la categoria {cat_elegida}. Puntaje obtenido: {puntaje}')

    guardar_tabla_csv(lista_puntaje)
    return lista_puntaje


def mostrar_puntajes(lista_puntaje):
    categorias_nombres = ['E', 'F', 'P', 'G', '1', '2', '3', '4', '5', '6']

    print('\nPUNTAJES:')
    print('      ', end='')
    for categoria in categorias_nombres:
        print(f'{categoria:>4}', end='')
    print()

    print('J1 -> ', end='')
    for valor in lista_puntaje[0]:
        if valor is None:
            print(f'{"-":>4}', end='')
        else:
            print(f'{valor:>4}', end='')
    print()

    print('J2 -> ', end='')
    for valor in lista_puntaje[1]:
        if valor is None:
            print(f'{"-":>4}', end='')
        else:
            print(f'{valor:>4}', end='')
    print()


def calcular_total(puntajes_jugador):
    total = 0
    for valor in puntajes_jugador:
        if valor is not None:
            total += valor
    return total

def main():
    lista_puntaje = [
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None]
    ]

    crear_archivo_jugadas(lista_puntaje)

    ganador_generala_real = None

    for ronda in range(10):
        print(f'\n----- RONDA {ronda + 1} -----')

        for jugador in range(2):
            print(f'\nTurno del jugador {jugador + 1}')

            lista_dados, planto_primera_tirada, generala_real = tirar_dados()

            if generala_real:
                indice_g = obtener_indice_categoria('G')
                lista_puntaje[jugador][indice_g] = 80
                guardar_tabla_csv(lista_puntaje)

                ganador_generala_real = jugador + 1
                print(f'\nGENERALA REAL del jugador {jugador + 1}.')
                print(f'Se anotan 80 puntos en G y el jugador {jugador + 1} gana inmediatamente.')
                break

            lista_puntaje = categorias(lista_dados, jugador, lista_puntaje, planto_primera_tirada)
            mostrar_puntajes(lista_puntaje)

        if ganador_generala_real is not None:
            break

    if ganador_generala_real is None:
        print('\nJuego terminado.')
        print('\nPUNTAJES FINALES:')
        mostrar_puntajes(lista_puntaje)

        total_j1 = calcular_total(lista_puntaje[0])
        total_j2 = calcular_total(lista_puntaje[1])

        print(f'\nTotal jugador 1: {total_j1}')
        print(f'Total jugador 2: {total_j2}')

        if total_j1 > total_j2:
            print('Gana el jugador 1')
        elif total_j2 > total_j1:
            print('Gana el jugador 2')
        else:
            print('Empate')


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()



