
def calculate_average(hits, at_bats):
    if at_bats == 0:
        return 0

    average = hits / at_bats
    return average


player_count = 0

while True:
    last_name = input("Enter player's last name (0 to stop): ")

    if last_name == "0":
        break

    hits = int(input("Enter number of hits: "))
    at_bats = int(input("Enter number of at bats: "))

    average = calculate_average(hits, at_bats)

    print("Player:", last_name)
    print("Batting average:", format(average, ".3f"))
    print()

    player_count = player_count + 1


print("Total number of players:", player_count)