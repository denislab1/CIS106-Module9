
def calculate_mpg(miles, gallons):
    if gallons == 0:
        return 0

    mpg = miles / gallons
    return mpg


trip_count = 0

while True:
    city = input("Enter destination city (0 to stop): ")

    if city == "0":
        break

    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons used: "))

    mpg = calculate_mpg(miles, gallons)

    print("Destination:", city)
    print("Miles traveled:", miles)
    print("Miles per gallon:", format(mpg, ".2f"))
    print()

    trip_count = trip_count + 1


print("Total number of trips:", trip_count)