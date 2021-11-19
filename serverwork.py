from phe import paillier
import json
import time
from extract_data import download_data, upload_data, bucket
# accuracy 0.8852459016393442
# enc_x-enc_y


def predict(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, public_key):
    conditions_checklist = []
    results_list = []
    conditions_checklist.append(cp - public_key.encrypt(0.5))
    conditions_checklist.append(ca - public_key.encrypt(0.5))
    conditions_checklist.append(thal - public_key.encrypt(2.5))
    conditions_checklist.append(exang - public_key.encrypt(0.5))
    conditions_checklist.append(thalach - public_key.encrypt(96.5))
    results_list.append([1.0, 0.0])
    conditions_checklist.append(chol - public_key.encrypt(316.5))
    results_list.append([0.0, 17.0])
    conditions_checklist.append(age - public_key.encrypt(61.5))
    results_list.append([1.0, 0.0])
    results_list.append([0.0, 1.0])
    conditions_checklist.append(oldpeak - public_key.encrypt(1.65))
    conditions_checklist.append(fbs - public_key.encrypt(0.5))
    conditions_checklist.append(age - public_key.encrypt(58.0))
    results_list.append([0.0, 3.0])
    conditions_checklist.append(trestbps - public_key.encrypt(177.0))
    results_list.append([1.0, 0.0])
    results_list.append([0.0, 1.0])
    results_list.append([1.0, 0.0])
    results_list.append([3.0, 0.0])
    conditions_checklist.append(oldpeak - public_key.encrypt(0.65))
    conditions_checklist.append(age - public_key.encrypt(42.0))
    results_list.append([3.0, 0.0])
    results_list.append([0.0, 4.0])
    results_list.append([13.0, 0.0])
    conditions_checklist.append(trestbps - public_key.encrypt(109.0))
    conditions_checklist.append(chol - public_key.encrypt(233.5))
    results_list.append([0.0, 2.0])
    results_list.append([3.0, 0.0])
    conditions_checklist.append(chol - public_key.encrypt(301.5))
    conditions_checklist.append(thalach - public_key.encrypt(105.5))
    conditions_checklist.append(oldpeak - public_key.encrypt(0.7))
    results_list.append([0.0, 1.0])
    results_list.append([4.0, 0.0])
    results_list.append([41.0, 0.0])
    conditions_checklist.append(chol - public_key.encrypt(303.5))
    results_list.append([0.0, 2.0])
    results_list.append([8.0, 0.0])
    conditions_checklist.append(age - public_key.encrypt(56.5))
    conditions_checklist.append(thalach - public_key.encrypt(148.0))
    conditions_checklist.append(oldpeak - public_key.encrypt(0.5))
    results_list.append([0.0, 5.0])
    conditions_checklist.append(age - public_key.encrypt(50.0))
    results_list.append([4.0, 0.0])
    conditions_checklist.append(age - public_key.encrypt(53.5))
    results_list.append([0.0, 4.0])
    results_list.append([1.0, 0.0])
    conditions_checklist.append(trestbps - public_key.encrypt(176.0))
    conditions_checklist.append(trestbps - public_key.encrypt(111.0))
    conditions_checklist.append(slope - public_key.encrypt(0.5))
    results_list.append([1.0, 0.0])
    conditions_checklist.append(thalach - public_key.encrypt(152.5))
    results_list.append([1.0, 0.0])
    results_list.append([0.0, 7.0])
    conditions_checklist.append(thal - public_key.encrypt(2.5))
    results_list.append([0.0, 52.0])
    conditions_checklist.append(ca - public_key.encrypt(0.5))
    results_list.append([0.0, 6.0])
    results_list.append([1.0, 0.0])
    results_list.append([1.0, 0.0])
    conditions_checklist.append(sex - public_key.encrypt(0.5))
    conditions_checklist.append(age - public_key.encrypt(62.5))
    conditions_checklist.append(ca - public_key.encrypt(0.5))
    results_list.append([0.0, 3.0])
    conditions_checklist.append(trestbps - public_key.encrypt(116.0))
    results_list.append([0.0, 1.0])
    results_list.append([3.0, 0.0])
    results_list.append([0.0, 12.0])
    conditions_checklist.append(chol - public_key.encrypt(244.5))
    conditions_checklist.append(oldpeak - public_key.encrypt(2.0))
    conditions_checklist.append(fbs - public_key.encrypt(0.5))
    conditions_checklist.append(restecg - public_key.encrypt(0.5))
    conditions_checklist.append(trestbps - public_key.encrypt(162.0))
    results_list.append([3.0, 0.0])
    results_list.append([0.0, 1.0])
    conditions_checklist.append(cp - public_key.encrypt(2.5))
    results_list.append([0.0, 4.0])
    results_list.append([1.0, 0.0])
    results_list.append([0.0, 5.0])
    results_list.append([4.0, 0.0])
    conditions_checklist.append(oldpeak - public_key.encrypt(3.1))
    conditions_checklist.append(trestbps - public_key.encrypt(119.0))
    results_list.append([0.0, 1.0])
    results_list.append([9.0, 0.0])
    results_list.append([0.0, 1.0])
    return conditions_checklist, results_list


# for loading of data
def get_data():
    download_data(bucket, "storeFiles/data.json", "data.json")
    with open('data.json', 'r') as f:
        dt = json.load(f)
    data = json.loads(dt)
    return data


# for creating the condition list based on tree in the server
def data_work():
    data = get_data()
    pub_k = data['public_key']
    public_key = paillier.PaillierPublicKey(n=int(pub_k['n']))
    encrypted_vals = [paillier.EncryptedNumber(public_key, int(t[0]), int(t[1])) for t in data['values']]
    (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal) = encrypted_vals
    return predict(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal,
                   public_key=public_key)


# for encrypting the data sent
def serialize_data():
    conditions, results= data_work()
    data = get_data()
    pub_k = data['public_key']
    public_key = paillier.PaillierPublicKey(n=int(pub_k['n']))
    encrypted_data = {'public_key': {'n': public_key.n},
                      'conditions': [(str(val.ciphertext()), val.exponent) for val in conditions], 'results': results}
    serialized = json.dumps(encrypted_data)
    return serialized


if __name__ == '__main__':
    time1 = time.time()
    datafile = serialize_data()
    with open('encrypted_results.json', 'w') as enc_file:
        json.dump(datafile, enc_file)
    upload_data(bucket=bucket, key="storeFiles/encrypted_results.json", filename="encrypted_results.json")
    time2 = time.time() - time1
    print("Uploaded Data file at", time.strftime('%H:%M:%S %Z'), "\nTotal time taken is %.2fs" %time2)

