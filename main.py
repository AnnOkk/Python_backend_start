
print('==== ex 1 ====')

def greet(name):
    return f"Hello, {name}"
print(greet(name="Ann")) #or
print(greet("Ann"))



def greet1(name,lang='en'):
    return f"Hello, {name}"
print(greet1(name="Ann",lang='en'))
print(greet1("Ann",'fr'))



print("==== ex 2 ====")

def total(*args):
    return sum(args)


def wrapper(values):
    return total(*values)


print(wrapper([1, 2, 3]))

print('==== ex 3 ====')

def greet(name, punctuation="!"):
    return "Hi, " + name + punctuation


def greet_with_options(name, **kwargs):
    return greet(name, **kwargs)


print(greet_with_options("Bob", punctuation="???"))

print('==== ex 4 ====')

def show1(**kwargs):
    for key, value in kwargs.items():
        print(kwargs)


def show(kwrgs, **kwargs):
    print(kwargs)
    print(kwrgs)

show(100, name='Ann',pos='IT')


print('==== ex 5* ====')
##list in parameters is mutable.

def add_item(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items


print(add_item(1))
print(add_item(2))
print(add_item(3))
