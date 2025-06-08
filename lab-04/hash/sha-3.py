from Crypto.Hash import SHA3_256

def sha3(message):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.digest()
def main():
    text =  input ("Nhập chuỗi cần băm SHA3-256: ").encode('utf-8')
    hashed_text = sha3(text)
    print("Chuoi can ban da nhap :", text.decode('utf-8'))
    print("Mã băm SHA3-256 của chuỗi là:", hashed_text.hex())
if __name__ == "__main__":
    main()