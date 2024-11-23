from elftools.elf.elffile import ELFFile

def parse_elf(filepath):
    with open(filepath, "rb") as f:
        return ELFFile(f)

def get_symbol_table(elf_data):
    symbol_table = []
    for section in elf_data.iter_sections():
        if section.header.sh_type in ["SHT_SYMTAB", "SHT_DYNSYM"]:
            for symbol in section.iter_symbols():
                symbol_table.append({
                    "name": symbol.name,
                    "address": symbol.entry.st_value,
                    "type": symbol.entry.st_info["type"]
                })
    return symbol_table

def get_section_headers(elf_data):
    section_headers = []
    for section in elf_data.iter_sections():
        section_headers.append({
            "name": section.name,
            "type": section.header.sh_type,
            "address": section.header.sh_addr,
            "size": section.header.sh_size
        })
    return section_headers
