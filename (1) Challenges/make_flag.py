offset = 0x63d4
inc = 56

flag = b"W3_4R3_CyK0rP47H" # custom your flag!
assert len(flag) == 16
key = [198, 72, 164, 148, 119, 168, 190, 251, 181, 245, 10, 218, 189, 55, 52, 187]

f = open("c:/Users/L0Z1K/Desktop/WCTF/CyKorPath.exe", "rb")
data = list(f.read())
f.close()

for x, y in zip(flag, key):
    data[offset] = x^y
    offset += inc

data = b"".join(x.to_bytes(1, 'big') for x in data)
f = open("c:/Users/L0Z1K/Desktop/WCTF/CyKorPath.exe", "wb")
f.write(data)

