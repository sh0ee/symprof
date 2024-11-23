from elftools.elf.elffile import ELFFile

def parse_elf(filepath):
    with open(filepath, "rb") as f:
        return ELFFile(f)

def get_symbol_table(elf_data, name_filter=None, address_range=None):
    return [
        {
            "name": symbol.name,
            "address": symbol.entry.st_value,
            "type": symbol.entry.st_info["type"]
        }
        for section in elf_data.iter_sections()
        if section.header.sh_type in ["SHT_SYMTAB", "SHT_DYNSYM"]
        for symbol in section.iter_symbols()
        if (name_filter is None or name_filter in symbol.name) and
           (address_range is None or (address_range[0] <= symbol.entry.st_value <= address_range[1]))
    ]

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

def get_elf_metadata(elf_data):
    return {
        "class": elf_data.header.e_ident['EI_CLASS'],
        "endianness": elf_data.header.e_ident['EI_DATA'],
        "entry_point": elf_data.header.e_entry
    }
