
import random
import string as st


class Service:

    all_symbols = st.ascii_letters + st.digits

    @classmethod
    def generates_a_password(cls, length):
        result = ''
        for elem in range(0, int(length), 1):
            result += random.choice(cls.all_symbols)
        return result
