#!/usr/bin/env python3

# CBC padding oracle attack
# - lenerd

import requests
import sys

def test_systems_security(base_url):
    new_ciphertext = bytes.fromhex('2cc9a9fc7cb4dc60f1df7babc4bf82c1122b12cbd8a1c10e1d7f1d4cf57c60ed8cb3703e30ff4b1a2a9af418df999c71b331721a24e713668d0478351a4ccad77fa6abff498d919b3773e6e25fcad5556545a6339b9d4f42c854f96e940a538342424242424242424242424242424242')
    res = requests.get(f'{base_url}/quote/', cookies={'authtoken': new_ciphertext.hex()})
    print(f'[+] done:\n{res.text}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'usage: {sys.argv[0]} <base url>', file=sys.stderr)
        exit(1)
    test_systems_security(sys.argv[1])
