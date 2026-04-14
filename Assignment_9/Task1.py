def count_lines(file_path):
    count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():
                    count += 1
        return count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0

if __name__ == "__main__":
    file_path = input("Enter the path to your text file: ")
    total_lines = count_lines(file_path)
    print(f"Total non-blank lines: {total_lines}")