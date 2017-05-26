# import re.RegexObject;
# prog = re.compile(pattern)
# result = prog.match(string)
g = (x * x for x in range(10))
for n in g:
    print n
    
def odd():
     print 'step 1'
     yield 1
     print 'step 2'
     yield 3
     print 'step 3'
     yield 5

o = odd()

o.next()
for n in o:
    print n

print '============================================'
def fib():
    a,b= 0,1
    while 1:
        yield b
        i = b
        b = a + b
        a = i
def gnext(x = 0,y = 1):
    g = fib()
    max = y + 1
    n = 1
    l = []
    while n <= max:
        l.append(g.next())
        n = n + 1
    print l[x:y]
    
gnext(3,10)