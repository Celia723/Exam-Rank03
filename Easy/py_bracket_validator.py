"""
Escribe una funcion que compruebe si los parentesis de una
cadena estan bien emparejados y anidados.
Admite tres tipos: (), [], {}.

La funciГіn debe:
- Devolver True si todos los parГ©ntesis estГЎn bien emparejados
- Devolver True si la cadena no tiene parГ©ntesis
- Devolver False si faltan pares o el anidamiento es incorrecto
- Ignorar caracteres que no sean parГ©ntesis

def bracket_validator(s: str) -> bool:

bracket_validator("()")
True

bracket_validator("()[]{}")
True

bracket_validator("(]")
False

bracket_validator("([)]")
False

bracket_validator("{[]}")
True

bracket_validator("hello(world)")
True

bracket_validator("((())")
False

bracket_validator("")
True
"""


def bracket_validator(s: str) -> bool:
    
    pila = []
    parejas = {')': '(', ']': '[', '}': '{'}

    for x in s:
        if x in"([{":
            pila.append(x)
        elif x in ")]}":
            if not pila or pila.pop() != parejas[x]:
                return False
            else:
                continue
    
    if not pila:
        return True
    else:
        return False

if __name__ == "__main__":

    print(bracket_validator("()")) # True
    print(bracket_validator("()[]{}"))  # True
    print(bracket_validator("([)]")) # False
    print(bracket_validator("{[]}"))  # True
