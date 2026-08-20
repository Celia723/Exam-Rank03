"""
Forbidden functions: sorted(), list.sort()

Escribe una funcion que ordene una lista de cadenas
con prioridad en tres niveles:

1. Primario: por longitud (ascendente)
2. Secundario: lexicográfico (alfabetico, sin distinguir
               mayúsculas, ascendente)
3. Terciario: por número de vocales (ascendente si la
              longitud y el orden léxico coinciden)

La funcion debe manejar:
- Cadenas vací­as y listas vací­as
- Mayúsculas y minúsculas mezcladas
    (tratar como minúsculas al ordenar)
- Caracteres especiales (ignorarlos al contar vocales)

def cryptic_sorter(strings: list[str]) -> list[str]:

cryptic_sorter(["apple","cat","banana","dog","elephant"])
["cat","dog","apple","banana","elephant"]

cryptic_sorter(["aaa","bbb","AAA","BBB"])
["AAA", "aaa", "BBB", "bbb"]

cryptic_sorter(["hello","world","hi","test"])
["hi","test","hello","world"]

cryptic_sorter([])
[]

cryptic_sorter([""])
[""]
"""


def cryptic_sorter(strings: list[str]) -> list[str]:
    new_list = []

    if not strings:
        return strings

    n = len(strings)

    for i in range(n - 1):
        #contar vocales de i
        count_v_i = 0
        for c in strings[i]:
            if c in "AEIOUaeiou":
                count_v_i += 1
        for j in range(i+1, n):

            #contar vocales de j
            count_v_j = 0
            for cj in strings[j]:
                if cj in "AEIOUaeiou":
                    count_v_j += 1
            
            #cogemos todos los datos de cada uno
            clave_i = (len(strings[i]), strings[i].lower(), count_v_i, strings[i])
            clave_j = (len(strings[j]), strings[j].lower(), count_v_j, strings[j])

            if clave_j < clave_i:
                strings[i], strings[j] = strings[j], strings[i]

    return strings

if __name__ == "__main__":

   print(cryptic_sorter(["Holaaaaaaa", "a", "gatito"]))
   print(cryptic_sorter(["apple","cat","banana","dog","elephant"]))
   print(cryptic_sorter(["aaa","bbb","AAA","BBB"]))
   print(cryptic_sorter(["hello","world","hi","test"]))
   print(cryptic_sorter([]))
   print(cryptic_sorter([""]))