#supprimer fichier

import os file_path = 'example.txt'

try: os.remove(file_path)
print(f"File '{file_path}' deleted successfully.")

except FileNotFoundError: print(f"File '{file_path}' not found.")