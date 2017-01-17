import sys
import re

def get_input(filename):
    with open(filename, 'r') as f:
        markers= f.read().splitlines()
    return ''.join(markers)

def version1(sequence):
    final= ''
    offset= 0
    while offset < len(sequence):
        t1= ''
        if sequence[offset] != '(':
            final += sequence[offset]
            offset += 1
        else:
            offset +=1
            while sequence[offset] != ')':
                t1 += sequence[offset]
                offset += 1
            offset += 1
            t2= t1.split('x')
            t3= sequence[offset:offset+int(t2[0])]
            final += t3 * int(t2[1])
            offset += int(t2[0])

    return final

if __name__ == "__main__":
    filename= '9.txt'
    sequence= get_input(filename)
    sequence= re.sub(' ','',sequence)
    final= version1(sequence)
    print len(final)    
