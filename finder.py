def findMaxNumber(numList):
    maxNum = 0
    for num in numList:
        if num > maxNum:
            maxNum = num
    return maxNum

if __name__ == "__main__":
    print("app started")
    print(findMaxNumber([1,2,3,4,5,9,8,7]))