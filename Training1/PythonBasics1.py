# usage of function and passing or arguments
def h(greeting, name):
    return '{}, {}'.format(greeting, name)
print(h('Hi','Anas'))


# usage of function and passing or arguments
def h1(greeting, name='Afaq'):
    return '{}, {}'.format(greeting, name)
print(h1('Hi'))

# usage of function and passing or arguments - tuple
def h2(*args, **kwargs):
    print(args)
    print(kwargs)
h2('Math','Art', name='Joth', age=22)


# usage of function and passing or arguments - list and dictionary
print("------------------")
def h3(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math','Art']
info={'name':'Joth', 'age':22}
h3(*courses, **info)
#single start for list
# double star for dictionary

# usage of function and passing or arguments - list and dictionary
print("------------------")
def h4(*args, **kwargs):
    """this function will take list and dictionary and print it"""
    print(args)
    print(kwargs)

courses = ['Math','Art']
info={'name':'Joth', 'age':22}
h4(courses, info)
#Above example doesnt unpack the list and dictionary. Therefore
#Add single start for list
#Add double star for dictionary