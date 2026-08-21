"""
Write a function that checks if the string 'small' is a subsequence
of 'big'. A subsequence means all characters of 'small' appear in 'big'
in the same order, but not necessarily consecutively.
Function is case-sensitive.

def hidenp(small: str, big: str) -> bool:

hidenp("abc", "a1b2c3")
True

hidenp("ace", "abcde")
True

hidenp("aec", "abcde")
False

hidenp("", "abc")
True

hidenp("abc", "ab")
False

hidenp("aaaa", "aaa")
False

hidenp("sing","subsequence testing")
True
"""

def hidenp(small: str, big: str) -> bool:
  
    n = 0
    if small is big:
        return True
    
    if not small:
        return True

    for i in big:
        if i == list(small)[n]:
            n += 1
        if n == len(small) and :
            return True

    if n != len(small):
        return False     

    
    return n == len(small)   


if __name__ == "__main__":

    print(hidenp("abc", "a1b2c3"))
    print(hidenp("ace", "abcde"))
    print(hidenp("aec", "abcde")) 
    print(hidenp("", "abc"))
    print(hidenp("abc", "ab"))
    print(hidenp("aaaa", "aaa"))
    print(hidenp("sing","subsequence testing"))