# 100SECURITY
# Converter Textos <> Morse
# Por: Marcos Henrique
# Site: www.100security.com.br

import os
from colorama import Fore, Style

# Limpar a Tela
def clear_screen():
    if os.name == 'nt':  # Se for Windows
        os.system('cls')
    else:  # Se for Linux ou macOS
        os.system('clear')
        
clear_screen()

# Inicializa o Colorama
from colorama import init
init(autoreset=True)

# Banner
projeto = f"{Style.BRIGHT}{Fore.YELLOW}# - - - - - - - - 100SECURITY - - - - - - - - #\n"
titulo = f"{Style.BRIGHT}{Fore.GREEN}Converter Textos <> Código Morse"
github = f"{Style.BRIGHT}{Fore.WHITE}GitHub: {Fore.WHITE}github.com/100security/{Style.BRIGHT}{Fore.LIGHTCYAN_EX}texto-morse"
instagram = f"{Style.BRIGHT}{Fore.WHITE}Instagram: {Fore.WHITE}{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}@100security"

# Exibe o texto com as cores e com uma nova linha entre eles
print(f"{projeto}\n{titulo}\n{github}\n{instagram}")

# Dicionário de conversão para Código Morse
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Inversão do dicionário para conversão de Morse para texto
MORSE_TO_TEXT_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

# Função para converter texto em código Morse
def text_to_morse(text):
    text = text.upper()  # Convertendo para maiúsculas
    morse_code = ' '.join(MORSE_CODE_DICT.get(char, '') for char in text)
    return morse_code

# Função para converter código Morse em texto
def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')  # Dividir o código por espaços
    text = ''.join(MORSE_TO_TEXT_DICT.get(code, '') for code in morse_code)
    return text

# Função para converter arquivo de texto em código Morse
def text_file_to_morse(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text_to_morse(text)
    except FileNotFoundError:
        print(f"{Style.BRIGHT}{Fore.RED}Arquivo não encontrado. Verifique o caminho do arquivo.")

# Função para converter arquivo de código Morse em texto
def morse_file_to_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            morse_code = file.read()
        return morse_to_text(morse_code)
    except FileNotFoundError:
        print(f"{Style.BRIGHT}{Fore.RED}Arquivo não encontrado. Verifique o caminho do arquivo.")
    except ValueError:
        print(f"{Style.BRIGHT}{Fore.RED}Erro na conversão. Verifique o conteúdo do arquivo.")

# Função para salvar o conteúdo em um arquivo
def salvar_em_arquivo(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Resultado salvo em {file_name}")

# Função para exibir o menu
def exibir_menu():
    print(f"\n{Style.BRIGHT}{Fore.RED}# - - - - - - - - - M E N U - - - - - - - - - #\n")
    print(f"{Style.BRIGHT}{Fore.WHITE}1 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Texto {Fore.WHITE}para {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Morse")
    print(f"{Style.BRIGHT}{Fore.WHITE}2 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Morse {Fore.WHITE}para {Fore.LIGHTCYAN_EX}Texto")
    print(f"{Style.BRIGHT}{Fore.WHITE}3 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}texto.txt {Fore.WHITE}para {Fore.LIGHTYELLOW_EX}Morse")
    print(f"{Style.BRIGHT}{Fore.WHITE}4 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}morse.txt {Fore.WHITE}para {Fore.LIGHTCYAN_EX}Texto")
    print(f"{Style.BRIGHT}{Fore.WHITE}5 {Style.NORMAL}{Fore.WHITE}- {Style.BRIGHT}{Fore.LIGHTRED_EX}Sair\n")

# Função principal
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            texto = input("Digite o Texto a ser convertido para Código Morse: ")
            morse_result = text_to_morse(texto)
            salvar_em_arquivo('morse.txt', morse_result)
            print(f"Texto original: {Style.BRIGHT}{Fore.LIGHTCYAN_EX}{texto}")
            print(f"Conversão para Morse: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{morse_result}")
        
        elif opcao == '2':
            morse_input = input("Digite o Código Morse separado por espaços: ")
            texto_result = morse_to_text(morse_input)
            salvar_em_arquivo('texto.txt', texto_result)
            print(f"Código Morse: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{morse_input}")
            print(f"Conversão para Texto: {Style.BRIGHT}{Fore.LIGHTCYAN_EX}{texto_result}")
        
        elif opcao == '3':
            file_path = input("Digite o nome do arquivo de texto (.txt): ")
            morse_result = text_file_to_morse(file_path)
            if morse_result:
                salvar_em_arquivo('morse.txt', morse_result)
                print(f"Conversão de {file_path} para Morse: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{morse_result}")
        
        elif opcao == '4':
            file_path = input("Digite o nome do arquivo de Código Morse (.txt): ")
            texto_result = morse_file_to_text(file_path)
            if texto_result:
                salvar_em_arquivo('texto.txt', texto_result)
                print(f"Conversão de {file_path} para Texto: {Style.BRIGHT}{Fore.LIGHTCYAN_EX}{texto_result}")
        
        elif opcao == '5':
            print(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}Saindo...")
            break

        else:
            print(f"{Style.BRIGHT}{Fore.RED}Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()
