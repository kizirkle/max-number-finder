def findMaxNumber(numList):
    if isinstance(numList, str):
        raise ValueError("Object must be an array of numbers.")
    maxNum = 0
    for num in numList:
        if not isinstance(num, int):
            # return num
            raise ValueError("All entries in numList must be numbers.")
        if num > maxNum:
            maxNum = num
    return maxNum

if __name__ == "__main__":
    print("app started")
    nums = input("Give a List Of Numbers separated by a single comma:")
    arr = nums.split(',')
    numarr=[]
    for num in arr:
         numarr.append(int(num))
    print(findMaxNumber(numarr))