import sys
import numpy as np

def cifrar_descifrar_mensaje(mensaje, clave):
    # Asegurarse de que el mensaje tenga una longitud par agregando un espacio en blanco si es necesario
    if len(mensaje) % 2 != 0:
        mensaje += " "

    # Cifrado
    numeros = []
    for letra in mensaje:
        numeros.append(ord(letra))

    matriz = np.array(numeros).reshape((2, int(len(numeros)/2)))

    matriz_cifrada = np.dot(clave, matriz)

    numeros_cifrados = matriz_cifrada.flatten()

    texto_cifrado = ""
    for numero in numeros_cifrados:
        texto_cifrado += chr(numero)

    # Descifrado
    matriz_descifrada = np.dot(np.linalg.inv(clave), matriz_cifrada)

    numeros_descifrados = matriz_descifrada.flatten()

    texto_descifrado = ""
    for numero in numeros_descifrados:
        texto_descifrado += chr(int(round(numero)))

    return texto_cifrado, texto_descifrado

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pregunta2.py <mensaje>")
        sys.exit(1)

    clave = np.array([[3, 5], [2, 7]])
    mensaje_ingresado = sys.argv[1]

    mensaje_cifrado, mensaje_descifrado = cifrar_descifrar_mensaje(mensaje_ingresado, clave)

    print("Mensaje original: ", mensaje_ingresado)
    print("Mensaje cifrado: ", mensaje_cifrado)
    print("Mensaje descifrado: ", mensaje_descifrado)