privkey = [160, 123, 130, 41, 5, 190, 61, 114, 124, 184, 209, 112, 196, 223, 39, 72, 109, 48, 177, 209, 184, 203, 160, 181, 127, 127, 48, 225, 24, 6, 157, 126, 173, 69, 251, 59, 150, 199, 119, 218, 111, 105, 167, 77, 234, 212, 250, 210, 166, 70, 108, 87, 92, 26, 84, 230, 217, 91, 76, 6, 139, 58, 116, 95]
header = [0 for _ in range(0x10)]
sig = b"K-PRIV"

for i, x in enumerate(sig):
    header[i] = x
base = 128          # fixed
mode = 1            # private key file
header[6] = mode
header[7] = base

data = []
l = []
for x in privkey:
    length = 0
    while x != 0:
        data.append(x%base)
        x = x // base
        length += 1
    l.append(length)

length_off = 0x30
data_off = 0x100

header[12] = length_off % 256
header[13] = length_off // 256
header[14] = data_off % 256
header[15] = data_off // 256

header += [0 for i in range(length_off-len(header))]
header += l
header += [0 for i in range(data_off-len(header))]

data = ''.join(hex(x)[2:].zfill(2) for x in data)
data = bytes.fromhex(data)

data_crc = [0, 0, 0, 0]
for i, x in enumerate(data):                # Calculate Checksum
    data_crc[i%4] ^= x

for i in range(4):
    header[8+i] = data_crc[i]

header = ''.join(hex(x)[2:].zfill(2) for x in header)
header = bytes.fromhex(header)

f = open("key.priv", "wb")
f.write(header)
f.write(data)