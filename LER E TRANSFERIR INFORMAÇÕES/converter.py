import pandas as pd

def txt_to_xlsx(txt_file_path, xlsx_file_path):
    """Reads a .txt file and writes its content to a .xlsx file with proper cell formatting."""
    try:
        # Lê o conteúdo do arquivo .txt
        with open(txt_file_path, 'r') as file:
            content = file.readlines()

        # Remove possíveis quebras de linha no final de cada linha
        content = [line.strip() for line in content]

        # Separa cada linha em chave e valor
        data = [line.split(':', 1) for line in content]
        
        # Cria um DataFrame do pandas com as linhas do arquivo .txt
        df = pd.DataFrame(data, columns=['Chave', 'Valor'])

        # Escreve o DataFrame em um arquivo .xlsx
        df.to_excel(xlsx_file_path, index=False)

        print(f"As informações de {txt_file_path} foram transferidas para {xlsx_file_path} com sucesso.")
      
    except FileNotFoundError:
        print(f"File {txt_file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Especifica os caminhos dos arquivos
txt_file_path = 'pessoa.txt'
xlsx_file_path = 'pessoa.xlsx'

# Chama a função para converter o conteúdo do arquivo .txt para .xlsx
txt_to_xlsx(txt_file_path, xlsx_file_path)
