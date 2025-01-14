#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule la factorielle d'un nombre entier n de manière récursive.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        # Vérifie que l'utilisateur a fourni un argument
        if len(sys.argv) != 2:
            print("Usage: ./factorial.py <number>")
            sys.exit(1)

        # Convertit l'argument en entier
        number = int(sys.argv[1])

        # Vérifie si le nombre est négatif
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            # Calcule et affiche la factorielle
            print(factorial(number))

    except ValueError:
        # Gère le cas où l'argument n'est pas un entier
        print("Please provide a valid integer.")
        