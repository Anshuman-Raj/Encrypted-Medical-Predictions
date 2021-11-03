from phe import paillier
import json


def generate_keys():
    pub, priv = paillier.generate_paillier_keypair()
    key_hash = {'public_key' : {'n': pub.n}, 'private_key': {'p': priv.p, 'q': priv.q}}
    with open('client_keys.json', 'w') as k:
        json.dump(key_hash, k)
    return
# generate_keys()

def get_key():
    with open('client_keys.json', 'r') as k:
        key_hash = json.load(k)
        pub = paillier.PaillierPublicKey(n=int(key_hash['public_key']['n']))
        priv = paillier.PaillierPrivateKey(pub, int(key_hash['private_key']['p']),int(key_hash['private_key']['q']))
        return pub, priv


def serialize_data(public_key, values):
    encrypted_data = {'public_key': {'n': public_key.n},
                      'values': [(str(val.ciphertext()), val.exponent) for val in values]}
    serialized = json.dumps(encrypted_data)
    return serialized


public_, _private = get_key()
vals = [58, 0, 3, 150, 283, 1, 0, 162, 0, 1, 2, 0, 2]
enc_values = [public_.encrypt(t) for t in vals]
data_to_be_sent = serialize_data(public_, enc_values)
with open('data.json', 'w') as dt:
    json.dump(data_to_be_sent, dt)

