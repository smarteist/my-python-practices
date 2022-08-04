import base64

chars = ['a', 'b', 'c', 'd', 'e']

# foreach style
for ch in chars:
    print(f"value: {ch}")

# index loop
for i in range(len(chars)):
    print(f"index : {i}")

# index and value style
for i, ch in enumerate(chars):
    print(f"index: {i}, value: {ch}")

# DANGEROUS ONE!
eval("print('hello world')")
eval(base64.decodebytes("cHJpbnQoJ2hlbGxvIHdvcmxkJyk=".encode()))

print([i for i in range(0, 11)])
