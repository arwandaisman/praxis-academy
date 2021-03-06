'spam eggs'  # single quotes

'doesn\'t'  # use \' to escape the single quote...
"doesn't"  # ...or use double quotes instead
'"Yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said.'

'"Isn\'t," they said.'
print('"Isn\'t," they said.')
s = 'First line.\nSecond line.'     # \n means newline
s                                   # without print(), \n is included in the output
print(s)                            # with print(), \n produces a new line

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'

'Py' 'thon'

text = ('Put several strings within parentheses '
        'to have them joined together.')
text

prefix = 'py'
prefix 'ton' 

('un' * 3) 'ium'

prefix + 'thon'

word = 'python'
word[0]
word[5]

word[-1]
word[-2]
word[-6]

word[0:2]
word[2:5]

word[2:]
word[4:]

word[:2]
word[4:]
word[-2:]

word[42]

word[4:42]
word[42:]

word[0] = 'J'
word[2:] = 'py'

'J' + word[1:]
word[:2] + 'py'

s = 'supercalifragilisticexpialidocious'
len(s)

