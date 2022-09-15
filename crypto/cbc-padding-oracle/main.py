import json
import secrets
from flask import Flask, request, make_response, redirect, url_for
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from secret_data import encryption_key, secret

app = Flask(__name__)
quotes = open('quotes.txt', 'r').readlines()


def encrypt(message: bytes) -> bytes:
    """Encrypt a message using our encryption key."""
    # generate a random IV
    iv = secrets.token_bytes(16)
    aes = AES.new(encryption_key, AES.MODE_CBC, iv=iv)
    # pad the plaintext to a multiple of the AES block size
    plaintext = pad(message, 16)
    # encrypt the padded plaintext
    ciphertext = aes.encrypt(plaintext)
    # return the iv concatenated to the ciphertext
    return iv + ciphertext


def decrypt(ciphertext: bytes) -> bytes:
    """Decrypt a ciphertext using our encryption key."""
    # the IV is stored in the first 16 B of the ciphertext
    iv = ciphertext[:16]
    aes = AES.new(encryption_key, AES.MODE_CBC, iv=iv)
    # decrypt the ciphertext
    plaintext = aes.decrypt(ciphertext[16:])
    # remove the padding of the plaintext
    message = unpad(plaintext, 16)
    return message


@app.route('/')
def index():
    """Landing page, hand out authentication tokens."""
    # create a response object
    response = make_response('<p>Here, have a cookie!</p>')
    # totally secure way to create an authentication token:

    # - create a secret plaintext (NB: `{secret}` is substituted for a secret
    # string, which you need to recover)
    plaintext = f'You never figure out that "{secret}". :)'.encode()
    # - encrypt this plaintext
    token = encrypt(plaintext)
    # - store the ciphertext hex-encoded in a cookie
    response.set_cookie('authtoken', token.hex())
    return response


@app.route('/quote/')
def quote():
    """Show quotes to the right users."""
    # check if an authentication token is there
    token = request.cookies.get('authtoken')
    if token is None:
        return redirect(url_for('index'))
    try:
        # try to decode/decrypt the token
        token = bytes.fromhex(token)
        plain = decrypt(token).decode()
    except Exception as e:
        return str(e)
    # check if this token is valid
    if plain == secret + ' plain CBC is not secure!':
        return f'<quote>\n{secrets.choice(quotes)}</quote>'
    else:
        return 'No quote for you!'
