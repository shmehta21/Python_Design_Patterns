class Singleton:
    _instances = {}
    
    #__new__ is called when each class is instantiated and BEFORE __init__
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls, *args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    

class Logger( Singleton ):
    pass

l1 = Logger()
l2 = Logger()

assert l1 is l2
assert id(l1) == id(l2)

class Interceptor( Singleton ):
    pass

i1 = Interceptor()
i2 = Interceptor()

assert i1 is i2
assert id(l1) == id(l2)

print('All assertions passed')


############ This fixes the Single Responsiblity issue  #############
# Does it by building a base class for all singletons
# As seen above any class that intends to be a Singleton can extend from this Super Class Singleton
# This approach leads to one more benefit: Separation of Concern as the custom class wanting to be a Singleton
# just deals with its own functionality and leaves the responsibility of managing instances on parent Singleton class