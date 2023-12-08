
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
def cercle(coord, r):
    circle = plt.Circle(coord, r, color='r', fill=False)
    ax.add_patch(circle)
    
cercle((0,0), 5)

def bulles1(n, coord=(0,0), r=5):
    if n == 0:
        return None

    cercle(coord, r)
    x, y = coord
    bulles1(n-1, (x+3*r/2, y), r/2)
    bulles1(n-1, (x, y-3*r/2), r/2)




def bulles2(n):
    for l in range(5):
        for i in range(5):
            bulles1(n, coord=(5, 5))
        plt.xticks(rotation=45)
        plt.yticks(rotation=45)


bulles2(4)
plt.autoscale()
plt.show()