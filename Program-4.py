import math
def allfactors(n):
    factors = set()
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            if n // i != i:
                factors.add(n // i)
    factors.add(1)
    factors.add(n)
    return factors
if __name__ == "__main__":
    n = int(input())
    arr = []
    ans = [0] * 10
    for _ in range(n):
        num = int(input())
        arr.append(num)
        factors = allfactors(num)
        for factor in factors:
            if factor < 10:
                ans[factor] += 1
    for i in range(1, 10):
        print(f"{i} : {ans[i]}")
