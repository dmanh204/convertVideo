import numpy as np
import math
import sys
sys.path.insert(0, 'F:/TaiLieuHocTap/sip/StreamCipher/lightWeightStreamCipher')
import lightweight as lw

def xor_encrypt_decrypt(bin_np, key):
    key_np = np.array(key, dtype=np.uint8) # convert to numpy array
    key_np = np.resize(key_np, bin_np.shape)  # Resize key stream  equal to binary stream.

    result = np.bitwise_xor(bin_np, key_np)
    return result

# Read file txt
with open('Test.txt', 'r') as file:
    stringData = file.read()
# For each 8 characters in string, convert them into an integer number and the string is converted to a tuple
binary_data = tuple(int(stringData[i:i+8], 2) for i in range(0, len(stringData), 8))
# Convert tuple to numpy array for decipher
data = np.array(binary_data, dtype=np.uint8)  # convert to numpy array
# Khoi tao ma dong
key = 0x1234567890abcdef
ma = lw.light(key)
sKey = []
for _ in range(math.ceil(data.size / 32)):
    sKey.extend(ma.run())

# Tien hanh giai ma hoa video bang ma dong
ketqua = xor_encrypt_decrypt(data, sKey)
# Viet vao file binary
with open('testVideo.mp4', 'wb') as file:
    #file.write(binary_data)
    ketqua.tofile(file)