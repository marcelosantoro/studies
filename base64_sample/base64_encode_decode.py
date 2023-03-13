import base64

# String a ser codificada
string = "Hello, world!"

# Codificando a string
encoded_string = base64.b64encode(string.encode('utf-8'))
print("String codificada:", encoded_string)

# Decodificando a string
decoded_string = base64.b64decode(encoded_string).decode('utf-8')
print("String decodificada:", decoded_string)