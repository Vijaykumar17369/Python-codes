inp = 'AAABBCCAA'
out = ''
prev = inp[0]
count = 0
for k, i in enumerate(inp):
    if i in prev:
        count+= 1
    else:
        out += prev + str(count)
        prev = i
        count = 1
    if len(inp)-1==k:
        out += prev + str(count)
print(out)
