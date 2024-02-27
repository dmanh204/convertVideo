import numpy as np
import sys
import math
sys.path.insert(0, 'F:/TaiLieuHocTap/sip/StreamCipher/lightWeightStreamCipher')
import lightweight as lw

def xor_encrypt_decrypt(bin_np, key):
    key_np = np.array(key, dtype=np.uint8)
    key_np = np.resize(key_np, bin_np.shape) # Resize key stream  equal to binary stream.

    result = np.bitwise_xor(bin_np, key_np)
    return result

# File mp4 can ma hoa
mp4 = 'sample.mp4'
data = np.fromfile(mp4, dtype=np.dtype('B'))# Doc tu file binary .mp4 ra numpy array

# Khoi tao ma dong
key = 0x1234567890abcdef
ma = lw.light(key)
sKey = []
for _ in range(math.ceil(data.size / 32)):
    sKey.extend(ma.run())

# Tien hanh ma hoa video bang ma dong
ketqua = xor_encrypt_decrypt(data, sKey)
output = ''.join(format(byte, '08b') for byte in ketqua)# chuyen cac phan tu trong numpy array tu dang binary
# sang dang string roi ghep vao output.
with open('Test.txt', 'w') as file: # Viet ket qua vao file .txt
    file.write(output)