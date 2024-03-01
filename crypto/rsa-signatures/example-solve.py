import base64
import json
import sys
import requests
from Crypto.Util.number import long_to_bytes

def json_to_cookie(j: str) -> str:
    """Encode json data in a cookie-friendly way using base64."""
    # The JSON data is a string -> encode it into bytes
    json_as_bytes = j.encode()
    # base64-encode the bytes
    base64_as_bytes = base64.b64encode(json_as_bytes, altchars=b'-_')
    # b64encode returns bytes again, but we need a string -> decode it
    base64_as_str = base64_as_bytes.decode()
    return base64_as_str

def main(base_url):
    msg = b'You got a 12 because you are an excellent student! :)'
    signature = 0x43a854cb7e2af5a284976dee56f176acda500aa1593b6c7d039c01a39ce432cbb12b8a7e73cc506af319122d7bb75416df4a3befa05e65418e3b58a721291d2058d577cb11f0562318e8f21ef58238c4248e086668dfff58cac0d490657a539cf3c389162a8dc92d5f8dd2d5acf6a33c5cf837d1544ab7f54a7e14d3c3d743670f57e28d1b158f216edb11f89369b233c762dc5aa093071aac7b80b4164cb4918f79513472836f1f02fa1a1ce89d292db28d1e85fc1de23f1f42b839c42960f51d9cba6cba726b18b27912b4abc337ff53bdd314b3365707244f836322c5ac35f51dbd5d3e4a3e807d94f4b21136dc67bd9f1ff128b5dbfeafa75cd7030e6ee966125a44dbe4880bf687d81d5b2c0987e67d8989a99fda980d8e8e264ef1c69b7ae91f4077a2bd03ca6aa8b44d3060cb21091579f782c268cd06fbeb0643ae397c73a0570b81314e305899e023aa8243e0b8e7ce959d0976682c888bbb3401ecf519dbc769043f28dd77afdc210b8d0f879c82423de2b3e6fa6090e6c6841b0a

    c = json_to_cookie(json.dumps({'msg': msg.hex(), 'signature': long_to_bytes(signature).hex() }))

    resp = requests.get(f'{base_url}/quote/', cookies={'grade': c})
    print(resp.text)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'usage: {sys.argv[0]} <base url>', file=sys.stderr)
        exit(1)
    main(sys.argv[1])
