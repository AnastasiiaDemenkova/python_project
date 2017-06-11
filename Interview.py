import value as value

for i in range(1,11):
    print i

i=1
while i<=10:
    print i
    i+=1

a=10
b=20
if a>b:
    print "ten is greater than twenty"
elif a==b:
    print "ten equal twenty"
else:
    print "{} is greater than {}".format (a,b)

# FizzBuzz
for num in xrange (1,101):
    if num % 5 == 0 and num % 3 == 0:
        print "FizzBuzz"
    elif num % 5 == 0:
        print "Fizz"
    elif num % 3 == 0:
        print "Buzz"
    else:
        print num

# Fibonacci sequense
a,b = 0,1
for i in xrange (0,10):
    print "current iteration", i
    print a
    a,b = b,a + b


# Lists#add element, delete element, append elements(end of list)
my_list = [10,20,30,40]
for i in my_list:
   print i

# Tuples#immutable
my_tuple = (1,2,3,4,5,6,7,8,9,10)
for i in my_tuple:
    print i

# Dictionaries
my_dict = {"dog":"Bobby", "age":"3", "color":"white"}
for key, val in my_dict.iteritems():
    print "My {} is {}".format(key, val)

# set# set removes duplicates
my_set = {10,20,30,40,50}
for i in my_set:
    print i

# list comprehensions
my_lists = [1,2,3,4,5,6,7,8,9,10]
# Give me each number in a list squared
squared = [num*num for num in my_lists]
print squared

# Fibonacci generator
def fib(num):
    a,b = 0,1
    for i in xrange (0, num):
        yield "{}: {}".format(i+1,a)
        a,b = b, a+b
for item in fib(10):
    print item

# OOP
class Person(object):
    def __init__(self,name):
        self.name = name
    def reveal_identify(self):
        print "My name is {}". format(self.name)
miu = Person("Miu")
miu.reveal_identify()
class SuperHero(Person):
    def __init__(self, name, hero_name):
        super (SuperHero, self). __init__(name)
        self.hero_name = hero_name
    def reveal_identify(self):
        super (SuperHero,self).reveal_identify()
        print "...and I am {}".format(self.hero_name)
variable = SuperHero ("Miu", "SpiderMan")
variable.reveal_identify()

print str(144)
