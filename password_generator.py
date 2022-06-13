import string as s
import random as r
def password_generator():
    min_chars, max_chars, special_chars = 8, 64, "#$~%&([{}])^*"
    passwd = ''.join(r.choices(s.ascii_letters + s.digits + special_chars, \
    k = r.randint(min_chars,max_chars)))
    return passwd
print(password_generator())
