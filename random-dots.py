from random import random
from flat import document, shape, gray

d = document(100, 100, 'mm')
p = d.addpage()
figure = shape().nostroke().fill(gray(0))

for i in range(10000):
    x = random()*96.0 + 2.0
    y = random()*96.0 + 2.0
    r= random()**2
    p.place(figure.circle(x, y, r))

d.pdf('random-dots.pdf')