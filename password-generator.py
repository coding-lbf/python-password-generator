import random

def generate_password():
  chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'
  password = ''
  for c in range(8):
    password += random.choice(chars)
  return password
  
print(generate_password())
