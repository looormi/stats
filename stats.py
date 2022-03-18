def median(list):

    if len(list) == 0:

        return 0

    list.sort() 

    midIndex = int(len(list) / 2)

    if len(list) % 2 == 1:

        return list[midIndex]      

    else:

        return (list[midIndex] + list[midIndex - 1]) / 2


def mean(list):


    if len(list) == 0:

        return 0

    total = 0

    for number in list:

        total += number

    return total / len(list)    


def mode(list):

    if len(list) == 0:

        return 0

    numberDictionary = {}     

    for digit in list:

        number = numberDictionary.get(digit, None)

        if number == None:

            numberDictionary[digit] = 1

        else:

            numberDictionary[digit] = number + 1


    maxValue = max(numberDictionary.values())

    modeList = []

    for key in numberDictionary:


        if numberDictionary[key] == maxValue:

            modeList.append(key)      

    return modeList     

def main():

    print("Enter List: ")

    a = int(input(" "))
    b = int(input(" "))
    c = int(input(" "))
    d = int(input(" "))
    e = int(input(" "))
    f = int(input(" "))
    g = int(input(" "))

    list =  [a ,b ,c ,d ,e ,f ,g]


    print("List:", list)    

    print ("Mode: ", mode(list))

    print ("Median :", median(list))

    print ("Mean: ", mean(list))

main()
