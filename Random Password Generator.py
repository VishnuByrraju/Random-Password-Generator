
import string
import random

a = list(string.ascii_letters)
b = list(string.digits)
c = list(string.punctuation)
d = int(input("How many letters"))
e = int(input("How many Numbers"))
f = int(input("How many special characters"))
h = []
for i in range(d):
    r = random.randint(0, len(a))
    h.append(a[r])
for i in range(e):
    r = random.randint(0, len(b))
    h.append(b[r])
for i in range(f):
    r = random.randint(0, len(c))
    h.append(c[r])
random.shuffle(h)
lr = ""
for i in h:
    lr += i
print(lr)
