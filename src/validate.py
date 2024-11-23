import os

def validate_file(filepath):
    if not os.path.isfile(filepath):
        print(f"Error: The file '{filepath}' does not exist.")
        return False
    
    if not filepath.endswith(".elf"):
        print(f"Error: The file '{filepath}' does not have a valid ELF extension.")
        return False

    with open(filepath, "rb") as f:
        magic_number = f.read(4)
        if magic_number != b'\x7fELF':
            print(f"Error: The file '{filepath}' is not a valid ELF file (invalid magic number).")
            return False

    return True
