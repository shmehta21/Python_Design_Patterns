class Singleton:
    
    @staticmethod
    def getInstance():
        if '_instance' not in Singleton.__dict__:
            Singleton._instance = Singleton()
        return Singleton._instance
    
s1 = Singleton.getInstance()
s2 = Singleton.getInstance()

assert s1 is s2
assert id(s1) == id(s2)

print('All assertions have passed')



############## Problems with this approach #####################
# The Singleton does not adhere to the 'Single Responsibility Principle'
# This takes care of instantiation and also keeps track of its state
# Also hard to subclass this Singleton class. What if some other class needs to behave
# like a singleton? You cannot use this as a template as it only checks whether
# its own instance has already been created or not? We need something more flexible
    