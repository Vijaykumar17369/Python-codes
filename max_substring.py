inp='dcdt'
a = dict()
start =0
length =0
max_start=0
for num,value in enumerate(inp):
    if value not in a:
        length+=1
    else:
        start=a[value]+1
        length+=1
    a[value]=num
    if (length-start)>max_start:
        max_length=length-start
        max_start = start
print(inp[max_start:(max_length+max_start)])



inp = 'dcdt'
a = dict()
start = 0
max_start = 0
max_length = 0
length = 0

for num, value in enumerate(inp):
    if value not in a or a[value] < start:
        length += 1
    else:
        start = a[value] + 1
        length = num - start + 1

    a[value] = num

    if length > max_length:
        max_length = length
        max_start = start

result = inp[max_start:(max_length + max_start)]
print(result)
