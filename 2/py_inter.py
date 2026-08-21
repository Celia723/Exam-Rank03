"""
Write a function that returns a string with the characters that appear
in both strings, without repetitions. Characters are added in the order
they appear in the first string.

def inter(s1: str, s2: str) -> str:

inter("hello", "world")
"lo"

inter("banana", "band")
"ban"

inter("abcabc", "bc")
"bc"

inter("abc", "xyz")
""

inter("", "abc")
""

"""

def inter(s1: str, s2: str) -> str:

    resultado = ""

    for i in s1:
        n = 0 #contador de cuantas veces coinciden dos letras
        for j in s2:
            if i == j:
                n += 1
        
        if n  > 0 and i  not in resultado:
            resultado += i
    
    if not resultado:
        return '""'
    return resultado


if __name__ == "__main__":

    print(inter("hello", "world"))
    print(inter("bainana", "baniid"))
    print(inter("abcabc", "bc"))
    print(inter("abc", "xyz"))
    print(inter("", "abc"))