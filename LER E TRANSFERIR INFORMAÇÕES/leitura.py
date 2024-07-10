import pandas as pd

def read_txt_file(file_path):
    """Reads and prints the contents of a .txt file."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print(f"Contents of {file_path}:")
        print(content)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")

def read_xlsx_file(file_path):
    """Reads and prints the contents of a .xlsx file."""
    try:
        df = pd.read_excel(file_path)
        print(f"Contents of {file_path}:")
        print(df)
    except FileNotFoundError:
        print(f"Leitura {file_path} terminada com sucesso!")
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")

# Example usage:
txt_file_path = 'pessoa.txt'
xlsx_file_path = ''

read_txt_file(txt_file_path)
read_xlsx_file(xlsx_file_path)
