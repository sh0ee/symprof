from elf import get_symbol_table
import cxxfilt

def filter_symbols(symbols, symbol_type=None):
    if symbol_type:
        return [symbol for symbol in symbols if symbol['type'] == symbol_type]
    return symbols

def demangle_symbol(name):
    return cxxfilt.demangle(name) if name else name

def extract_symbols(elf_data, symbol_type=None):
    symbol_table = get_symbol_table(elf_data)
    symbols = []

    for entry in symbol_table:
        demangled_name = demangle_symbol(entry["name"])
        symbols.append({
            "name": demangled_name,
            "address": entry["address"],
            "type": entry["type"]
        })

    return filter_symbols(symbols, symbol_type)
