from math import sqrt

#### Fonction secondaire


def isprime(p):
    if p<2:
        return False
    for i in range (2,int(sqrt(p))+1):
        if p%i==0:
            return False
    return True

## Suppression de la demande d'entrée utilisateur pour compatibilité avec les tests



#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
    #nombre = int(input("Entrez un nombre : "))
    #print(f"{nombre} est premier ? {isprime(nombre)}")