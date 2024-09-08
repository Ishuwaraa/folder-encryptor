from cryptography.fernet import Fernet


if __name__ == '__main__':
    def write_key():
        # generating the key and writing in binary to a file
        enc_key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(enc_key)
        return 'encryption key generated'

    print(write_key())
