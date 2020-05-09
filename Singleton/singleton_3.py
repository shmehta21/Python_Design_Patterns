class Singleton(type):
    _instances = {}
    
    # By defining a metaclass __call__ method you are demanding that this gets called
    # before any of the class's or subclasses's __new__ method is called
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)  #Note the difference in super call. 
            cls._instances[cls] = instance
        return cls._instances[cls]
    
    
class Logger( metaclass = Singleton ):
    pass

l1 = Logger()
l2 = Logger()

assert l1 is l2, 'Identity check failed'
assert id(l1) == id(l2), 'Equality check failed'

class Interceptor( metaclass = Singleton ):
    pass

i1 = Interceptor()
i2 = Interceptor()

assert i1 is i2
assert id(l1) == id(l2)

print('All assertions passed')
    
    
    
############ This approach uses a Metaclass  #############
# Metaclasses is a class's class. Instance of metaclass is a class itself
# Metaclass controls the building of a class. Note that the Singleton object
# inherits from type and not object. Subclasses will then inherit from metaclass Singleton
# Separation of concerns holds true in this implementation as well, since metaclass is now a completely different 
# entity and only deals with managing instances. By using metaclass ,it gives an opportunity to use multiple inheritance
# as the instance management task has been delegated to the metaclass ,so the subclass can handle whatever responsibility it wants to handle