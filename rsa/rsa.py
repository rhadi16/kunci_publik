# Converts a string to a list of decimal numbers
def str2dec(st):
    dec_list = []
    for i in st:
        dec_list.append(ord(i))
    return dec_list

# Converts a list of decimal numbers to string
def dec2str(dec):
    str_list = []
    for i in dec:
        str_list.append(chr(i))
    return ''.join(str_list)

message = 'Test'
print('Original String: \t', message)

dec = str2dec(message)
print('String into Decimal: \t', dec)

txt = dec2str(dec)
print('Decimal into String: \t', txt)

import random
import math

def generate_prime(beg=1000, end=10000):
    beg_rand = random.randint(beg, end);
    if beg_rand % 2 == 0:
        beg_rand += 1
        
    for possiblePrime in range(beg_rand, end, 2):

        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(3, math.floor(possiblePrime/2), 2):
            if possiblePrime % num == 0:
                isPrime = False

        if isPrime:
            return possiblePrime

# This value is the multiplication of the two prime numbers,
# because the prime numbers are large this value is difficult to factorize
def generate_nkey(p, q):
    return p * q

# This 'e' key with 'n' is considered the public key
def generate_ekey(p, q):
    phi = (p-1) * (q-1)

    for e in range(random.randrange(3, phi-1, 2), phi-1):
        if math.gcd(e, phi) == 1:
            return e

# This 'd' key with 'n' is considered the private key
def generate_dkey(e):
    phi = (p-1) * (q-1)

    d = int(phi / e)
    while (True):
        if (d * e) % phi == 1:
            return d
        d += 1

def endecrypt_message(m, key, n):
    
    res = 1     # Initialize result 
  
    # Update message if it is more than or equal to p 
    m = m % n  
      
    if (m == 0) : 
        return 0
  
    while (key > 0) : 
          
        # If key is odd, multiply key with result 
        if ((key & 1) == 1) : 
            res = (res * m) % n 
  
        # key must be even now 
        key = key >> 1      # key = key/2 
        m = (m * m) % n 
          
    return res

p = generate_prime()
q = generate_prime()

while (p == q):
    q = generate_prime()

print('Two random prime numbers')
print('\tPrime 1: ', p)
print('\tPrime 2: ', q)

n = generate_nkey(p, q)
e = generate_ekey(p, q)
d = generate_dkey(e)

print('\nn key: ', n)
print('e key: ', e)
print('d key: ', d)

print('\nPublic key {e, n}: {%d, %d}' %(e, n))
print('Private key {d, n}: {%d, %d}' %(d, n))

message = 'Rhadiiiiii'
message_dec = str2dec(message)

# Encrypt message using the public key
encrypted = [endecrypt_message(i, e, n) for i in message_dec]

# Decrypt message using the private key
decrypted = [endecrypt_message(i, d, n) for i in encrypted]

print('\nMESSAGE\n\t', message, '\n\t', message_dec)
print('\n\nENCRYPTED\n\t', encrypted)
print('\n\nDECRYPTED\n\t', dec2str(decrypted), '\n\t', decrypted)

message = 'Rhadi Jiii'
message_dec = str2dec(message)

# Encrypt message using the private key
encrypted = [endecrypt_message(i, d, n) for i in message_dec]

# Decrypt message using the public key
decrypted = [endecrypt_message(i, e, n) for i in encrypted]

print('\nMESSAGE\n\t', message, '\n\t', message_dec)
print('\n\nENCRYPTED\n\t', encrypted)
print('\n\nDECRYPTED\n\t', dec2str(decrypted), '\n\t', decrypted)