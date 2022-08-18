import base64

chars = ['a', 'b', 'c', 'd', 'e']

adict = {'k1': 1, 'k2': 'val2'}

# foreach style
for ch in chars:
    print(f"value: {ch}")

# foreach key and value style
for k, v in adict.items():
    print(f"key: {k}, value: {v}")

# index loop
for i in range(0, 5):
    print(f"i : {i}")

# index loop
for i in range(len(chars)):
    print(f"index : {i}")

# index and value style
for i, ch in enumerate(chars):
    print(f"index: {i}, value: {ch}")

# inline loop
print([i for i in range(0, 11)])

# DANGEROUS ONE!
eval("print('hello world')")
eval(base64.decodebytes("cHJpbnQoJ2hlbGxvIHdvcmxkJyk=".encode()))
