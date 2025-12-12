def day_3_p1(line:str) -> int:
    volts = -1

    for i in range(len(line)):
        comp = int(line[i]) * 10

        for j in range(i+1, len(line)):
            comp += int(line[j])
            volts = max(volts,comp)
            comp -= int(line[j])
    
    return volts

# I left this in here because I thought it was funny
# After reading a reddit comment, I thought about using recursive backtracking
# This idea worked on the example (the sample txt file) because it is small
# But do to its exponential time complexity, it would not work
# I wonder if I can calculate the program for my computer...
def nope(volts:str, line:str) -> str:
    print(volts)
    if len(line) == 0 or len(volts) == 12:
        return volts
    choose = volts + line[0]
    num1 = day_3_p2(choose, line[1:])
    num2 = day_3_p2(volts,line[1:])
    if num2 == "":
        return num1
    ret = str(max(int(num1),int(num2)))
    return ret


def day_3_p2(line:str) -> int:
    start = 0 
    ret = [""]*12

    for i in range(12):
        mval = -1
        for c in range(start, len(line)+i-11):
            if int(line[c]) > mval:
                mval = int(line[c])
                start = int(c)+1
        ret[i] = str(mval)
    # print("".join(ret))
    return int("".join(ret))

def main():
    with open("Day_3_Input.txt", "r") as file:
            sum = 0
            for line in file:
                sum += day_3_p1(line.strip())
            print(f"Day 3 Part 1 Sum: {sum}")
    
    with open("Day_3_Input.txt", "r") as file:
        sum = 0
        for line in file:
            sum += day_3_p2(line.strip())
        print(f"Day 3 Part 2 Sum: {sum}")

if __name__ == "__main__":
    main()