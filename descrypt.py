import numpy as np
import math
import utils

# funcion descrypt
def decrypt(key_matrix_inv, cipher_text):
    """
    Argumentos: matriz inversa, texto cifrado
    Regresa: texto plano
    """
    print("La matriz inversa es: \n", key_matrix_inv)
    dimensions = len(cipher_text)
    
    # Crea texto cifrado de la matriz (ASCII Valores - 65 para obtener de 0 a X)

    cipher_text_matrix = []
    for i in range(dimensions):
        cipher_text_matrix.append(ord(cipher_text[i]) - 65)
    
    cipher_text_matrix = np.array(cipher_text_matrix)
    print("Clave matriz cifrada: \n", cipher_text_matrix)

    # multiplica el inverso con la matriz del texto cifrado 
    result = np.array(np.dot(key_matrix_inv, cipher_text_matrix))

    # imprime(resultado[0][1], entero(resultado[0][1]))
    print("Matriz descifrada\n", result) 

    # crea una cadena vacía para texto sin formato
    plain_text = ""
    # convierte la matriz de resultados a texto sin formato usando chr ()
    for i in range(dimensions):
        plain_text += chr(int(round(result[0][i], 0) % 26 + 65))

    # devolver el texto sin formato descifrado
    return plain_text

if __name__ == "__main__":
    # tomar la entrada del usuario
    plain_text = str(input("Texto Plano: "))

    # dimensiones de la matriz = longitud (texto plano) x longitud (texto plano)
    dimensions = len(plain_text)
    
    # matriz de texto plano
    plain_text_matrix = []
    
    # crea una matriz de columnas para caracteres de texto plano
    for i in range(dimensions):
        plain_text_matrix.append(ord(plain_text[i]) - 65)
    
    plain_text_matrix = np.array(plain_text_matrix)
    
    print("Matriz de texto plano\n", plain_text_matrix)

    print("Ingrese valores para la clave: ")

    # tomar valores para la matriz de claves
    key_matrix = []
    for i in range(dimensions):
        row_ = []
        for j in range(dimensions):
            value = int(input(str(i) + ", " + str(j) + " value: "))                         
            row_.append(value)
        key_matrix.append(row_)

    print("Matriz clave: \n")
        
    # para cifrado
    key_matrix = np.array(key_matrix)
    
    # calcular el inverso de la matriz clave usando el módulo inverso multiplicativo
    key_matrix_inv = np.linalg.inv(np.matrix(key_matrix)) * \
            np.linalg.det(key_matrix) * \
            utils.multi_inverse(np.linalg.det(key_matrix), 26) % 26
        
    print(key_matrix)

    print("Matriz clave inversa: \n", key_matrix_inv)
    
    result = key_matrix.dot(plain_text_matrix)
     
    print("Matriz Cifrada: \n", result)
    
    cipher_text = ""

    for i in range(dimensions):
        cipher_text += chr(result[i] % 26 + 65)

    print("Texto Cifrado: \n", cipher_text)

    decrypted_plain_text = decrypt(key_matrix_inv, cipher_text)

    print("Texto plano descifrado: ", decrypted_plain_text)
                
