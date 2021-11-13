if __name__ == '__main__':
    n = int(input())
    lst=[]
    lst = list(map(int,input().strip().split()))[:n]
    a = max(lst)
    while max(lst) == a:
        lst.remove(max(lst))
    print(max(lst))
