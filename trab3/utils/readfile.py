def read_text_file(file_path) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    print("Conteúdo original lido: ", content)
    return content

def write_encoded_file(encoded_number, output_file_path) -> None:
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(str(encoded_number))
