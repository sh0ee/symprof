import json

def format_output(symbols, output_format='text'):
    if output_format == 'json':
        return json.dumps(symbols, indent=4)
    
    result = ["Symbols:"]
    for symbol in symbols:
        result.append(f"Name: {symbol['name']}, Address: {symbol['address']:#x}, Type: {symbol['type']}")
    return "\n".join(result)

def save_output_to_file(output, output_file):
    with open(output_file, 'w') as f:
        f.write(output)
