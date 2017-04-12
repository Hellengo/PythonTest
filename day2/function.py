import re

def sayhi(name,age,salary,job="IT"):
    print "name is:", name
    print "age is:", age
    print "salary is:", salary
    print "job is:", job

sayhi("Hellengo",28,50000,"CEO")


def multiply(x,y):
    if x>y:
        return x*y
    else:
        return x/y

print multiply(6,4)


def sayhi1(*args):
    print args


def sayhello(**kwargs):
    print kwargs
    if kwargs.has_key("name"):
        print kwargs["name"]
    else:
        print "must input name"

sayhello(name="hellengo", job="CEO")


print map(lambda x:x**2, range(10))


def run():
    print "test1"
    yield 1