def day_3_p1(line:str) -> int:
    volts = -1

    for i in range(len(line)):
        comp = int(line[i]) * 10

        for j in range(i+1, len(line)):
            comp += int(line[j])
            volts = max(volts,comp)
    
    return volts


def day_3_p2(line:str) -> int:
    return "not made yet"


def main():
    with open("Day_3_Input.txt", "r") as file:
            sum = 0
            for line in file:
                sum += day_3_p1(line)
            print(f"Day 3 Part 1 Sum: {sum}")
    
    with open("Day_3_Input.txt", "r") as file:
        sum = 0
        for line in file:
            sum = day_3_p2(line)
        print(f"Day 3 Part 2 Sum: {sum}")

if __name__ == "__main__":
    main()