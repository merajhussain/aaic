
def string_features(s1,s2):
    s1list=  set(s1.split(' '))
    s2list=  set(s2.split(' '))


    return len(s1list & s2list), list(s1list-s2list), list(s2list-s1list)




s1=input("enter string1:")
s2=input("enter string2:")

a,b,c = string_features(s1,s2)

print(a)
print(b)
print(c)

