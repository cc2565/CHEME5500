import matplotlib.pyplot as plt

class Graph:
    def __init__(self, func):
        self.func = func
    
    def plot(self,filename):
        self.filename = filename
        x = range(300)
        y = [self.func(i) for i in x]
        plt.plot(x,y)
        plt.show()
        plt.savefig('%s.jpg' %filename)
    pass

f1 = lambda x : x
f2 = lambda x : x**2

g1 = Graph(f1)
g1.plot("demo1")

g2 = Graph(f2)
g2.plot("demo2")