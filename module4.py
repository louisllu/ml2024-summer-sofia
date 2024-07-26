def searchNumber():
    print("Please enter a positive integer N:")
    n = input()

    nums = {}
    for i in range(1, int(n)+1):
        print("Please enter a number you would like to input:")
        x = input()
        nums[x] = nums.get(x, [])
        nums[x].append(i)

    print("Please enter the number you would like to search:")
    target = input()
    if target not in nums:
        print("-1")
    else:
        print(nums[target])

if __name__ == "__main__":
    searchNumber()