import hug

@hug.get('/happy_birthday')

def happy_birthday(name , age: hug.types.number = 1):
    return "Happy {age} Birthday {name}!".format(**locals())