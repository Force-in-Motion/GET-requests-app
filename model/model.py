import random
import string as st

all_symbols = st.ascii_letters + st.digits

def generates_a_password(length):
    result = ''
    for elem in range(0, int(length), 1):
         result += random.choice(all_symbols)
    return result

