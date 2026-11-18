def findMaxNumber(numList):
    if isinstance(numList, str):
        raise ValueError("Object must be an array of numbers.")
    maxNum = 0
    for num in numList:
        if not isinstance(num, int):
            raise ValueError("All entries in numList must be numbers.")
        if num > maxNum:
            maxNum = num
    return maxNum

if __name__ == "__main__":
    print("app started")
    print(findMaxNumber([1,2,3,4,5,9,8,7]))