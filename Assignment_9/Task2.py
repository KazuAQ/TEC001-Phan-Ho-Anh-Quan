def find_keyword_lines(file_path, keyword):
    line_numbers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, start=1):
                if keyword in line:
                    line_numbers.append(line_num)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")
    return line_numbers