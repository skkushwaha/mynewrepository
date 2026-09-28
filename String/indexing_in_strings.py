# indexing on string
str = 'Core Python'

# access each character using while loop
n = len(str)
i=0
while i<n:
    print(str[i], end='')
    i=i+1
print()
# access in reverse order
i = -1
while i >= -n:
    print(str[i], end='')
    i -= 1
print()

# access in reverse order using negative index
i = 0
while i <= n:
    print(str[-i], end='')
    i += 1