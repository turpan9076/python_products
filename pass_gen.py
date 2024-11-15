import string
import secrets

def pass_gen(size=12):
   chars = string.ascii_lowercase + string.digits
   chars += string.ascii_uppercase
   chars += '%&$#()'

   return ''.join(secrets.choice(chars) for x in range(size))

print(pass_gen(10))