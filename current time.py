import time
time.ctime()
print time.ctime()

my_subject1 = 'My best code %s' % time.ctime()
print "subject1", my_subject1, type(my_subject1)
my_subject2 = 'My best code {0}'.format(time.ctime())
print  my_subject2
print 'My best code my_subject2'

print "//*[text()='my_subject']"