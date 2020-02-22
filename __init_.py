def x():
    global p
    p = 20
    print(p)
    return p


print(x)
z = x()
print(z + 2)