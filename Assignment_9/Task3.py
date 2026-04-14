def average_score(filename):
    total_score = 0
    count = 0
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    name, score = line.split(',')
                    total_score += float(score)
                    count += 1
        
        if count == 0:
            print("No records found in the file.")
            return 0
        
        average = total_score / count
        print(f"Average score: {average:.2f}")
        return average
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0
    except ValueError:
        print("Error: Invalid data format. Expected 'name,score' format.")
        return 0