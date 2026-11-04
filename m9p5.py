
def calculate_tuition(credit_hours, district_code):
    if district_code == "I":
        tuition = credit_hours * 250
    elif district_code == "O":
        tuition = credit_hours * 550
    else:
        tuition = 0

    return tuition


total_tuition = 0

while True:
    last_name = input("Enter student last name (0 to stop): ")

    if last_name == "0":
        break

    credit_hours = int(input("Enter credit hours: "))
    district_code = input("Enter district code (I or O): ").upper()

    tuition = calculate_tuition(credit_hours, district_code)

    print("Student:", last_name)
    print("Tuition owed: $", format(tuition, ".2f"))
    print()

    total_tuition = total_tuition + tuition


print("Total tuition owed: $", format(total_tuition, ".2f"))