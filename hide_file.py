import sys

filename = sys.argv[1]
key = int(sys.argv[2])

with open(filename, 'rb') as f:
    data = f.read()

data = [(key ^ c) for c in data]

with open("_"+filename, 'wb') as f:
    f.write(bytes(data))
