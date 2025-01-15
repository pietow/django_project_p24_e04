class Root:
    def ping(self):
        print('ping root')


class A(Root):
    def ping(self):
        print('ping A')
        super().ping()

class B(Root):
    def ping(self):
        print('ping B')
        # super().ping()

class Leaf(A, B):
    def ping(self):
        print('ping Leaf')
        super().ping()

leaf = Leaf()
leaf.ping()
print(Leaf.__mro__) # (<class '__main__.Leaf'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Root'>, <class 'object'>)

'ping Leaf'
'ping A'
'ping B'