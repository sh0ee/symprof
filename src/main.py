import sys
from validate import validate_file
from elf import parse_elf
from symbols import extract_symbols
from output import format_output

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <elf-file> [--output <output-file>] [--verbose]")
        sys.exit(1)

    filepath = sys.argv[1]
    output_file = None
    verbose = False

    for i in range(2, len(sys.argv)):
        if sys.argv[i] == '--output' and i + 1 < len(sys.argv):
            output_file = sys.argv[i + 1]
            i += 1  
        elif sys.argv[i] == '--verbose':
            verbose = True

    if not validate_file(filepath):
        print(f"Invalid file: {filepath}")
        sys.exit(1)

    try:
        if verbose:
            print(f"Parsing ELF file: {filepath}")

        elf_data = parse_elf(filepath)
        symbols = extract_symbols(elf_data)
        output = format_output(symbols)

        if verbose:
            print(f"Extracted {len(symbols)} symbols.")

        if output_file:
            try:
                with open(output_file, 'w') as f:
                    f.write(output)
                if verbose:
                    print(f"Output written to {output_file}")
            except IOError as e:
                print(f"Error writing to file {output_file}: {e}")
                sys.exit(1)
        else:
            print(output)

    except Exception as e:
        print(f"An error occurred while processing the ELF file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
