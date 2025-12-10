def is_invalid_p1(val:int) -> bool:
    val = str(val)
    l = (len(val))//2
    invalid = val[:l] == val[l:]
    return invalid

def is_invalid_pt2(val:int) ->bool:
    if is_invalid_p1(val): return True

    val = str(val)

    for end in range(len(val)//2):
        sample = val[:end+1]
        skip = len(sample)
        valid = True
        for i in range(end+1, len(val),skip):
            comp = val[i:i+skip]
            if sample != comp:
                valid = False
                break
        if valid: return True
        
    return False

def main(ids:list)-> int:
    sum = 0
    for id in ids:
        l,h = id.split(sep="-")
        for i in range(int(l),int(h)+1):
            if is_invalid_pt2(i):
                sum += i
    
    return sum

def day_1(ids:list)->int:
    sum = 0
    for id in ids:
        l,h = id.split(sep="-")
        for i in range(int(l),int(h)+1):
            if is_invalid_p1(i):
                sum += i
    
    return sum

if __name__ == "__main__":
    with open("Day_2_Input.txt") as file:
        out = main(file.readlines()[0].split(sep=','))
        print(out)
