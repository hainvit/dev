x = 'hello, world'
x1 = '''hello world,
pro'''

print('*x: ', x)
print('*x[1]: ', x[1])
print('*x[2:5]: ', x[2:5])
print('*len(x): ', len(x))

x3 = 'Hello, World '
print('x.strip: ', x.strip())
print('x.lower: ', x.lower())
print('x.upper: ', x.upper())
print('replace: ', x3.replace('o', 'A'))
print('a.split(,): ', x3.split(','))

# check string
print('check string: ', 'e' in x3)
print('check string not in: ', 'he' not in x3)

# string format
txt = 'hello {}'
formatTxt = 'world'
print(txt.format(formatTxt))
