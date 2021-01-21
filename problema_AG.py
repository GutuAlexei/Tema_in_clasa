with open ('input.txt' , 'r') as f:
    x=list(eval(f.readline()))
with open ('output.txt' , 'w') as f:
    f.write('a)' + str(x) + '\n')
    a=sorted(x)
    f.write('b)'+str(a)+'\n')
    x.sort(reverse=True)
    f.write('c)'+str(x)+'\n')
    f.write('d)'+str(len(a))+'\n')
    f.write('e)'+str(max(a))+'\n')
    f.write('f)'+str(min(a))+'\n')
    f.write('g)'+str( x + [111])+'\n')
    x[1]=222
    f.write('h)'+str(x)+'\n')