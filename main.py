from cryptography.fernet import Fernet
import os
import timeit


def load_key():
    # loading the key in binary mode
    if os.path.exists('./key.key'):
        return open('key.key', 'rb').read()


key = load_key()


def encrypt_folder(folder, enc_key):
    if not os.path.exists(f'./{folder}'):
        return "folder doesn't exists"

    files = os.listdir(folder)
    # print(f'original folder: {len(files)} files')
    # allowed_types = ['txt', 'jpg', 'jpeg', 'png', 'mp4', 'mkv', 'mov', 'pdf']
    # files = [f for f in files if f.lower().split('.')[-1] in allowed_types]
    # print(f'encrypting {len(files)} files')

    try:
        t1 = timeit.default_timer()
        f = Fernet(enc_key)

        for file in files:
            with open(f'./{folder}/{file}', 'rb') as mf:
                file_data = mf.read()
                encrypted_data = f.encrypt(file_data)

            with open(f'./{folder}/{file}.enc', 'wb') as mf:
                mf.write(encrypted_data)

            os.remove(f'./{folder}/{file}')

        t2 = timeit.default_timer()
    except Exception as err:
        return err

    return f"folder encrypted successfully in {round(t2-t1, 2)} seconds"


def decrypt_folder(folder, enc_key):
    if not os.path.exists(f'./{folder}'):
        return "folder doesn't exists"

    files = os.listdir(folder)
    files = [f for f in files if f.endswith('.enc')]
    print(files)
    print(f'decrypting {len(files)} files')

    try:
        t1 = timeit.default_timer()
        f = Fernet(enc_key)

        for file in files:
            with open(f'./{folder}/{file}', 'rb') as mf:
                file_data = mf.read()

            decrypted_data = f.decrypt(file_data)
            original_file = file.replace('.enc', '')

            with open(f'./{folder}/{original_file}', 'wb') as mf:
                mf.write(decrypted_data)

            os.remove(f'./{folder}/{file}')

        t2 = timeit.default_timer()
    except Exception as err:
        return err

    return f"folder decrypted successfully in {round(t2-t1, 2)} seconds"


# print(encrypt_folder('testfolder', key))
# print(decrypt_folder('testfolder', key))
