def caesar_cipher(filename, shift, direction):
    shift_amount = shift if direction.lower() == 'right' else -shift
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        ciphertext = ""

        for char in content:
            if char.isupper():
                shifted = ord(char) - ord('A')
                shifted = (shifted + shift_amount) % 26
                ciphertext += chr(shifted + ord('A'))
            elif char.islower():
                shifted = ord(char) - ord('a')
                shifted = (shifted + shift_amount) % 26
                ciphertext += chr(shifted + ord('a'))
            else:
                ciphertext += char
       
        output_filename = filename.replace('.', '_encrypted.')
        with open(output_filename, 'w') as file:
            file.write(ciphertext)
        
        print(f"Ciphertext saved to {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")