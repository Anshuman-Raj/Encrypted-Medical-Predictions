from phe import paillier
import json
from extract_data import upload_data, bucket
import sys
import time
from tkinter import *


def generate_keys():
    pub, priv = paillier.generate_paillier_keypair()
    key_hash = {'public_key': {'n': pub.n}, 'private_key': {'p': priv.p, 'q': priv.q}}
    with open('client_keys.json', 'w') as k:
        json.dump(key_hash, k)
    return


generate_keys()


def get_key():
    with open('client_keys.json', 'r') as k:
        key_hash = json.load(k)
        pub = paillier.PaillierPublicKey(n=int(key_hash['public_key']['n']))
        priv = paillier.PaillierPrivateKey(pub, int(key_hash['private_key']['p']), int(key_hash['private_key']['q']))
        return pub, priv


def serialize_data(public_key, values):
    encrypted_data = {'public_key': {'n': public_key.n},
                      'values': [(str(val.ciphertext()), val.exponent) for val in values]}
    serialized = json.dumps(encrypted_data)
    return serialized


# 58, 0, 3, 150, 283, 1, 0, 162, 0, 1, 2, 0, 2
# 58 0 3 150 283 1 0 162 0 1 2 0 2
# 50 1 2 140 233 0 1 163 0 0.6 1 1 3
def fin():
    root.destroy()

time1 = time.time()
root = Tk()
root.geometry('300x120')
root.title('Uploaded Data')

public_, _private = get_key()
# vals = list(map(int, input().split()))
vals = [float(i) for i in sys.argv[1:]]

enc_values = [public_.encrypt(t) for t in vals]
data_to_be_sent = serialize_data(public_, enc_values)
with open('data.json', 'w') as dt:
    json.dump(data_to_be_sent, dt)
upload_data(bucket=bucket, key="storeFiles/data.json", filename="data.json")
time2 = time.time() - time1
on_screen = "Uploaded Data file at " + time.strftime('%H:%M:%S %Z') + "\nTotal time taken to upload is %.2fs" % time2
root.eval('tk::PlaceWindow . center')
lebel = Label(master=root, text=on_screen)
lebel.pack()
button = Button(master=root, command=fin, text='OK', height=3, width=8)
button.place(x=110, y=50)
root.mainloop()

