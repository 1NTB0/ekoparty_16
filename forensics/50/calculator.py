import hashlib
import base64

input_str = "NOTNOTNOTNOTNOTNOTNOTNOTNOTNOTNOTNOT"

def calculate(string):
    hash_object = hashlib.sha1(string.encode())
    hash_value = str(hash_object.hexdigest())
    #print "hash: " + hash_value

    ret_val = str(base64.b64encode(hash_value.encode()))
    #print "base64: " + ret_val

    return ret_val

for i in range(0, 16777216):
    input_str = calculate(input_str)

output = input_str.replace("=","")
print output
