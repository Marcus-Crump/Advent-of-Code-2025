def is_invalid_p1(val:int) -> bool:
    val = str(val)
    l = (len(val))//2
    invalid = val[:l] == val[l:]
    return invalid

def main_p1(ids:list)-> int:
    sum = 0
    for id in ids:
        l,h = id.split(sep="-")
        for i in range(int(l),int(h)+1):
            if is_invalid_p1(i):
                sum += i
    
    return sum

def main_p2(ids:list)-> int:
    pass

if __name__ == "__main__":
    with open("Day_2_Input.txt") as file:
        out = main_p1(file.readlines()[0].split(sep=','))
        print(out)