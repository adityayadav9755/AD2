import graph
import math

grph = graph.Graph()

n = -3
l = 0.125
x = []
y = []
# z = []
w = []
# u = []
v = []
t = []
# while n <= 3:
#     x.append(n)
#     y.append(pow(2, n))
#     n +=0.1
#
# while l <= 8:
#     u.append(l)
#     z.append(math.log(l, 2))
#     l += 0.1


for m in range(-4, 10):
    w.append(m)

for a in range (-10, 10):
    x.append(a)
    y.append(n + math.cos(a))

for a in range(-5, 10):
    v.append(a)
    t.append(0)


grph.graph(x=x, y=y)
# grph.graph(x=u, y=z)
grph.graph(x=w, y=w)
grph.graph(x=v, y=t)
grph.graph(x=t, y=v)
grph.show()

print(math.cos.__doc__)
