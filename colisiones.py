import random

def calcular_nueva_velocidad(masaNave, masaAsteroide, velocidadNaveI, velocidadAsteroide):
    velocidadNaveF = ((masaNave - masaAsteroide) * velocidadNaveI + 2 * masaAsteroide * velocidadAsteroide) / (masaNave + masaAsteroide)
    velocidadAsteroideFinal = ((masaAsteroide - masaNave) * velocidadAsteroide + 2 * masaNave * velocidadNaveI) / (masaNave + masaAsteroide)
    return velocidadNaveF, velocidadAsteroideFinal

def calcular_distancia(velocidadNaveI, tiempo):
    return velocidadNaveI * tiempo

def jugar():
    print("\n¡Estás en una nave espacial y un asteroide se aproxima rápidamente!")
    
    masaNave = random.randint(5000, 10000)  
    masaAsteroide = random.randint(1000, 5000) 
    velocidadNaveI = random.uniform(5, 15)  
    velocidadAsteroide = random.uniform(10, 30)
    tiempo = random.uniform(1, 3)  
    
    print(f"\nDATOS DE LA NAVE Y DEL ASTEROIDE:\n")
    print(f"Masa de la nave: {masaNave} kg \nVelocidad inicial: {velocidadNaveI:.2f} m/s")
    print(f"Masa del asteroide: {masaAsteroide} kg \nVelocidad inicial: {velocidadAsteroide:.2f} m/s")
    print(f"Tiempo hasta el impacto: {tiempo:.2f} segundos")
    
    print("\n¡El asteroide se acerca rápidamente! Debes tomar una decisión para salvar la nave, podrá escapar del asteroide antes de que colisionen?")
    
    velocidadNaveF, velocidadAsteroideFinal = calcular_nueva_velocidad(masaNave, masaAsteroide, velocidadNaveI, velocidadAsteroide)
    
    distancia_nave = calcular_distancia(velocidadNaveF, tiempo)
    distancia_asteroide = calcular_distancia(velocidadAsteroide, tiempo)
    
    print("\nOpciones:")
    print("1. Acelerar la nave para aumentar la velocidad y moverla más rápido.")
    print("2. Intentar desviarse para cambiar el ángulo de la nave.")
    print("3. Quedarse quieto y esperar el impacto.")
    
    decision = input("Elige tu acción (1, 2 o 3): ")

    if decision == "1":
        print(f"\nElegiste acelerar la nave. La nave se movería {distancia_nave:.2f} metros.")
        if distancia_nave >= distancia_asteroide:
            print("Eso! La nave se movió lo suficiente para evitar el asteroide.")
        else:
            print("No fue suficiente. El asteroide golpeó la nave :(")
    
    elif decision == "2":
        print(f"\nElegiste desviarte y ahora la nave se mueve a {velocidadNaveF:.2f} m/s.")
        if distancia_nave >= distancia_asteroide:
            print("Eso! La nave se movió lo suficiente para esquivar el asteroide")
        else:
            print("No te desviaste lo suficiente. El asteroide golpeó la nave :(")
    
    else:
        print(f"\nTe quedaste quieto y el asteroide se movería {distancia_asteroide:.2f} metros.")
        if distancia_asteroide > distancia_nave:
            print("Nimodorris, el asteroide te golpeó :(")
        else:
            print("OMG! El asteroide pasó por otro lado")

    continuar = input("\n¿Quieres jugar otra vez? (sí/no): ").lower()
    if continuar == "sí":
        jugar()
    else:
        print("Gracias por jugar")

def main():
    print("Bienvenido al juego de colisión espacial")
    while True:
        print("\nMenú del juego")
        print("1. Empezar a jugar")
        print("2. Salir")
        
        opcion = input("\nIngrese una opción del menú: ")
        if opcion == "1":
            jugar()
        elif opcion == "2":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

main()
