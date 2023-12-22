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
file_name = "teste.txt" 
a = file_name + ".ransomwaretroll"

try:
  file = open(a, "rb")
  
except: 
  a = input("Digite o nome do arquivo a ser descriptografado: ")
  ret = False
file = open(a, "rb")
# Ler o conteúdo do arquivo
file_data = file.read()
file.close()

os.remove(a)
# Chave de criptografia
key = b'testkey123456789'

aes = pyaes.AESModeOfOperationCTR(key)

crypto_data = aes.encrypt(file_data)
# Salvar o arquivo criptografado
new_file = file_name 
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()


red_bold = "\033[1;31m"
reset_format = "\033[0m"

texto = "Arquivo descriptografado com sucesso!"

print(red_bold + texto + reset_format)
