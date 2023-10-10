def main():
    x = int(input())
    for i in range(1, x+1):
        j = 1
        cnt = i
        while cnt > 0:
            print(j, end=" ")
            j += 2
            cnt -= 1
        print()
if __name__ == "__main__":
    main()
