def check_hemoglobin():
    sex = input("Please enter your biological sex (male/female): ").lower()
    hemoglobin = float(input("Please enter your hemoglobin value (g/l): "))

    if sex == 'female':
        if hemoglobin < 117:
            status = "low"
        elif 117 <= hemoglobin <= 155:
            status = "normal"
        else:
            status = "high"
    elif sex == 'male':
        if hemoglobin < 134:
            status = "low"
        elif 134 <= hemoglobin <= 167:
            status = "normal"
        else:
            status = "high"
    else:
        return "Invalid sex entered. Please enter 'male' or 'female'."

    return f"Your hemoglobin value is {status}."

print(check_hemoglobin())