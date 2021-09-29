import random
import string
import logging as logger

def generate_random_email_and_password(domain=None,email_prefix=None):
    if not domain:
        domain = 'demostore.com'

    if not email_prefix:
        email_prefix = 'testuser'

    random_email_string_len = 5
    random_string = ''.join(random.choices(string.ascii_lowercase,k=random_email_string_len))

    email = email_prefix + '_' + random_string + '@' + domain
    logger.info(f"Generated random email: {email}")

    random_password_string_len = 12
    random_password = ''.join(random.choices(string.ascii_letters, k=random_password_string_len))

    #email = email_prefix + '_' + random_string + '@' + domain
    #logger.info(f"Generated random email: {email}")

    random_info = {"email": email, "password":random_password}

    return random_info