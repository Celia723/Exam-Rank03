"""
Nombre del ejercicio: py_echo_validator
Archivos esperados	: py_echo_validator.py
Funciones permitidas: Ninguna
--------------------------------------------------------------------------------

Escribe una función que compruebe si una cadena de texto es un palíndromo, ignorando los espacios y sin distinguir mayúsculas o minúsculas. Considera únicamente los caracteres alfabéticos para la comparación.

La función debe devolver True si el texto es un palíndromo y False en caso contrario.

Tu función debe declararse de la siguiente manera:

def echo_validator(text: str) -> bool:

Ejemplos:

Input: echo_validator("racecar")
Output: True

Input: echo_validator("A man a plan a canal Panama")
Output: True

Input: echo_validator("race a car")
Output: False

Input: echo_validator("Was it a car or a cat I saw")
Output: True

Input: echo_validator("hello")
Output: False

Input: echo_validator("Madam Im Adam")
Output: True

Input: echo_validator("")
Output: False
"""

def echo_validator(text: str) -> bool:

    clean_word = []
    for c in text.lower():
        if c >= 'a' and c <= 'z': #if c.isalpha()
            clean_word.append(c)

    reverse = clean_word[::-1]

    if not reverse:
        return False

    return reverse == clean_word


if __name__ == "__main__":
    print(echo_validator("racecar"))
    print(echo_validator("A man a plan a canal Panama"))
    print(echo_validator("race a car"))
    print(echo_validator("Was it a car or a cat I saw"))
    print(echo_validator("hello"))
    print(echo_validator("Madam Im Adam"))
    print(echo_validator(""))