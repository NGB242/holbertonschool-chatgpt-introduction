#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    # Vérifie qu'un argument est fourni
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)

    try:
        # Convertit l'argument en entier
        number = int(sys.argv[1])

        # Gère les cas négatifs
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            # Calcule et affiche la factorielle
            print(factorial(number))
    except ValueError:
        # Gestion des arguments non valides
        print("Please provide a valid integer.")
        