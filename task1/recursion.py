def rev(n):
    if len(n)==0:
        return ""
    else:
        return n[-1]+rev(n[:-1])
def rev_s(s):
    word=s.split()
    r_word=[rev(i) for i in word]
    return " ".join(r_word)
s=input()
print(rev_s(s))
