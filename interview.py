#type(),dir(),getattr(),hasattr(),isinstance()


tu = (12,45,22222,103,6)
print '{0} {2} {1} {2} {3} {2} {4} {2}'.format(*tu)
#12 22222 45 22222 103 22222 6 22222




li = [12,45,78,784,2,69,1254,4785,984]
print map('the number is {}'.format,li)   



from datetime import datetime,timedelta

once_upon_a_time = datetime(2010, 7, 1, 12, 0, 0)
delta = timedelta(days=13, hours=8,  minutes=20)

gen =(once_upon_a_time +x*delta for x in xrange(20))

print '\n'.join(map('{:%Y-%m-%d %H:%M:%S}'.format, gen))