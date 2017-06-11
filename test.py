from pprint import pprint
l = [1, 2, 3, 4, 5]

x = (1, 2, 3, 4, 5, 6, 6)
y = {1,2, 23, 4, 5, 6, 6}
d = {"table":1, "chair":4}
print type(l), l
print type(x), x
print type(y), y
print type(d), d

print '=='*23
pprint(dir(l))


x= ["a", "b", "c"]
print "".join(x)