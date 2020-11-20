import random
import math
import numpy

def rotation(xy, r=None):
    if r==None:
        theta = random.random() * 2.0 * math.pi
        print(random.random())
    else:
        theta = r * 2.0 * math.pi
    ct = math.cos(theta)
    st = math.sin(theta)

    r = numpy.array([[ct, st], [-st, ct]])
    # return numpy.einsum('ptc,ci->pti', xy, r)
    return numpy.einsum('tc,ci->ti', xy, r)


print(rotation(numpy.array([[1,2]])))
