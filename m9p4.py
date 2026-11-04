
def get_pay_rate(job_code):
    if job_code == "L":
        return 25
    elif job_code == "A":
        return 30
    elif job_code == "J":
        return 50
    else:
        return 0


total_gross_pay = 0

while True:
    last_name = input("Enter employee last name (0 to stop): ")

    if last_name == "0":
        break

    job_code = input("Enter job code (L, A, J): ").upper()
    hours = float(input("Enter hours worked: "))

    rate = get_pay_rate(job_code)

    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * rate * 1.5
        gross_pay = regular_pay + overtime_pay
    else:
        gross_pay = hours * rate

    print("Employee:", last_name)
    print("Gross pay: $", format(gross_pay, ".2f"))
    print()

    total_gross_pay = total_gross_pay + gross_pay


print("Total gross pay: $", format(total_gross_pay, ".2f"))