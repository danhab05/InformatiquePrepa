

def canJump(nums):
# def canJump(self, nums):
    n = len(nums)
    indice = 0

    c = True
    for i in range(n-1):
        indice = i
        print(indice)
        while indice + 1 < n:
            previous = indice + nums[indice]
            if previous == indice:
                break
            else:
                indice = previous
            if indice + 1 >= n:
                return True

    return False


print(canJump([3,0,8,2,0,0,1]))