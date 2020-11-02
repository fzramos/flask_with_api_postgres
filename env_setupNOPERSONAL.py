"""
    This is a version of the env_setup.py file WITHOUT ANY OF MY
    personal information.
"""
import hashlib
import string
import random

def add_to_env(length):
    """
        add_to_env will create environment variables
        that will live inside the .env file when the script
        is run

        parameter: length -- how many characters we will need
        for our secret key
    """

    with open('.env', 'w+') as file:
        database_url = 'postgres+psycopg2://{user}:{pw}@{url}'.format\
            (user='dummy_user',pw='dummpy_password', url = 'dummpy_pg_ip_:_port')
            # should be your real pgadmin password
        data = file.read()
        file.seek(0) # not strictly necessary since seek is automatically at 0
        all_letters = string.ascii_lowercase
        letter_connect = ''.join(random.choice(all_letters) for i in range(length))
        key = 'some extra randomness added to letter_connect using a hashlib hash function'
        file.write(f"SECRET_KEY={key.hexdigest()}\nDATABASE_URL={database_url}".replace('\n ', '\n'))
        # rewriting whole .env file with new url and key
        # not the replace is done because for some reason the simple \n adds a
        #   weird tab/space to the newline, the replace removes the tab and alieviates
        #   errors
        file.truncate()
        # just to ensure random key wasn't made way too long

add_to_env(10)
