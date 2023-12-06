from utils import readfile as rf, codarit as ca, onetimepad as otp

# Paths para leitura e escrita de arquivos
input_file_path = 'files/inputs/entrada.txt'
output_file_path = 'files/outputs/saida.txt'

text_content = rf.read_text_file(input_file_path)

# Cria o modelo de probabilidade baseado no texto lido e codifica o texto.
prob_model = ca.create_uniform_probability_model(text_content)
encoded_number = ca.arithmetic_encode(text_content, prob_model)
binary_format = ca.float_to_binary(encoded_number, 64)

key = otp.generate_stream_cipher_key(len(binary_format))
encrypted_binary = otp.xor_operation(binary_format, key)

print("Texto lido: ", text_content)
print("Número codificado: ", encoded_number)
print("Modelo de probabilidade: ", prob_model)
print("Número codificado em binário: ", binary_format)
print("Chave: ", key)
print("Número codificado em binário: ", encrypted_binary)

descrypted_binary = otp.xor_operation(encrypted_binary, key)
print("Número descodificado em binário: ", descrypted_binary)
descrypted_float = ca.binary_to_float(descrypted_binary, 64)
print("Número descodificado: ", descrypted_float)
descrypted_text = ca.arithmetic_decode(descrypted_float, prob_model, len(text_content))
print("Texto descodificado: ", descrypted_text)


