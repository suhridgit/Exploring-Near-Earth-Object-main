def __init__(self, **info):
    for key, value in info.items():
        if key == 'designation':
            self.designation = value
        elif key == 'name':
            if value:
                self.name = value
            else:
                self.name = None
        else:
            raise AttributeError("Unknown Attribute")


'''
In [4]: neo = NearEarthObject(designation="test", name="data")
In [5]: neo = NearEarthObject(designation="test", name="data", haha="test")
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-5-720966da7998> in <module>
----> 1 neo = NearEarthObject(designation="test", name="data", haha="test")
<ipython-input-3-c3447129d8be> in __init__(self, **info)
     45                     self.name = None
     46             else:
---> 47                 raise AttributeError("Unknown Attribute")
     48 
AttributeError: Unknown Attribute
In [6]: neo = NearEarthObject(designation="test", name="")
In [7]: neo.name
In [8]: print(neo.name)
None
'''

def generate_tribonacci_numbers():
    a, b, c = 0, 0, 1
    while True:
        a, b, c = b, c, a + b + c
        yield a
    # Yield an infinite stream of Tribonacci numbers! The next value of the sequence will be c + b + a.



def is_tribonacci(num):
    """Return whether `num` is a Tribonacci number."""
    # Be careful to not loop infinitely!
    if num > 1000000000:
        return False
    g = generate_tribonacci_numbers()
    res = num in g
    return res

import random
def random_list(size, start=0, stop=10):
    return list(random.randrange(start, stop) for _ in range(size))



def generate_cases():
    a = 0
    while True:
        yield random_list(a)
        a += 1

'''
for cad in self._approaches:
    neo = [n for n in neos if n.designation == cad._designation]

    # check first if a match is found
    if len(neo):
        neo = neo[0]
        cad.neo = neo
        neo.approaches.append(cad)
'''

'''
Task 2b
loop through all NEOS:
  name_dict[name of current NEO] = current NEO object
  des_dict[designation of current NEO] = current NEO object
  
  loop through all the close approaches:
  if designation of current approach is in des_dict:
    append current approach to des_dict[des of current approach].approaches
    assign des_dict[des of current approach] to approach.neo


'''

# test comment