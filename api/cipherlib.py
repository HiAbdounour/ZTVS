from random import randint as rdt

def reversible_cipher_function(x:str):
    if len(x)==1:
        # encrypt
        hash = str(rdt(int("1"*64),int("1"*128)))
        pos = int(hash[0])+52
        H = f"{hash[:pos]}{ord(x)}{hash[pos:]}"
    elif len(x)>1:
        # decrypt
        pos = int(x[0])+52
        H = chr(int(x[pos:pos+2]))
    else:
        raise RuntimeError("An unauthorized action was intended by the user.")
    return H