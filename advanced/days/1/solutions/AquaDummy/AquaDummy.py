#arthurjiang
#11/11/2022

a = ("j h 0 g 4 5 j 0 j f g m 4 0 f g h y 7 u t 0 3 d 2 0 f h n 0 g f 4 0 0 0 5 7 q 0 w d 1 2 v c x 4 0 8 9 p y i 2 3 1 4 0 0 g j h 0")

a = a.split()
a = list(a)

for x in range(4):
    for x in (a):
        try:
            int(x)
        except:
            a.remove(x)
        else:
            r =1

for x in (a):
    try:
        a.remove("0")
    except:
        break
a.sort(reverse=True)
a = "".join(a)
print(a)


