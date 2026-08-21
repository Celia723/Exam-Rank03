"""
Write a function that checks if two strings are anagrams.
They must contain exactly the same letters with the same quantity,
ignoring case and spaces.

def anagram(s1: str, s2: str) -> bool:

anagram("listen", "silent")
True

anagram("Triangle", "Integral")
True

anagram("Dormitory", "Dirty Room")
True

anagram("hello", "world")
False

anagram("", "")
True

anagram("abc", "abcc")
False
"""

def anagram(s1: str, s2: str) -> bool:
    s1_l = s1.lower()
    s2_l = s2.lower()

    s1_clean = [c for c in s1_l if c.isalnum()]
    s2_clean = [c for c in s2_l if c.isalnum()]

    if len(s1_clean) != len(s2_clean):
        return False
    
    for c in s1_clean:
        if c in s2_clean:
            s2_clean.remove(c)
        else:
            return False

    if not s2_clean:
        return True
    else:
        return False


if __name__ == "__main__":
    print(anagram("listen", "silent"))
    print(anagram("Triangle", "Integral"))
    print(anagram("Dormitory", "Dirty Room"))
    print(anagram("hello", "world"))
    print(anagram("", ""))
    print(anagram("abc", "abcc"))