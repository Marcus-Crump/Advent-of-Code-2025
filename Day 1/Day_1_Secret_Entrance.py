from bs4 import BeautifulSoup as soup
import requests as r

def main():
    op = {"R":1, "L":-1}
    place = 50
    count = 0

    with open("/Users/kat/Projects/PythonStuff/Advent of Code/2025/Day 1 Input.txt", 'r') as input:
        for l in input:
            dir = op[l[0]]
            val = int(l[1:])

            place += (dir*val)

            if place % 100 == 0:
                count += 1
                place = 0
            elif place > 100:
                place %= 100
            elif place < 0:
                place = 100 - (-1*place)%100

    print (count)

def man(input):
    op = {"R":1, "L":-1}
    place = 50
    count = 0

    for l in input:
        dir = op[l[0]]
        val = int(l[1:])

        place += (dir*val)

        if place % 100 == 0:
            count += 1
            place = 0
        elif place > 100:
            place %= 100
        elif place < 0:
            place = 100 - (-1*place)%100
    return count

def men():
    op = {"R":1, "L":-1}
    place = 50
    count = 0

    with open("/Users/kat/Projects/PythonStuff/Advent of Code/2025/Day 1 Input.txt", 'r') as input:
        for l in input:
            dir = op[l[0]]
            val = int(l[1:])

            if val >= 100:
                count += val // 100
                val %= 100
            crosses = place != 0
            place += (dir*val)

            if place % 100 == 0:
                count += 1
                place = 0
            elif place > 100:
                if crosses:
                    count += 1
                place %= 100
            elif place < 0:
                if crosses:
                    count += 1
                place = 100 - (-1*place)%100

    return count

if __name__ == "__main__":
    
    main()
    print(men())