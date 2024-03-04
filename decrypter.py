import os
import pyaes

def decrypt_file(file_name, key):
    try:
        # Abrir o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()
        
        # Remover o arquivo criptografado
        os.remove(file_name)
        
        # Descriptografar o arquivo
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)
        
        # Criar o arquivo descriptografado
        new_file_name = file_name.replace(".ransomwaretroll", "")
        with open(new_file_name, "wb") as new_file:
            new_file.write(decrypt_data)
        
        print(f"Arquivo {file_name} descriptografado com sucesso.")
    
    except Exception as e:
        print(f"Erro ao descriptografar o arquivo {file_name}: {e}")

if __name__ == "__main__":
    # Chave para descriptografia
    key = b"testeransomwares"
    
    # Lista de arquivos a serem descriptografados
    files_to_decrypt = ["teste.txt.ransomwaretroll", "outro_arquivo.txt.ransomwaretroll"]
    
    # Descriptografar cada arquivo
    for file_name in files_to_decrypt:
        decrypt_file(file_name, key)
