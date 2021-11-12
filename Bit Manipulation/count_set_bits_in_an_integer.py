
def setBitsCount(num):
    ans = 0
    while num > 0:
        ans += num % 2
        num = num >> 1
    return ans

if __name__=="__main__":
    print(setBitsCount(6))
    print(setBitsCount(8))