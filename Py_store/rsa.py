def factoring(n):#number to be factorized
    lists = []
    for i in range(1, int((n**0.5) + 1)):
        if n % i == 0:
            lists.append(i)
            lists.append(n // i)
    if len(lists) == 2:
        print(f"{lists[0] * lists[1]} = {lists[0]} * {lists[1]}")
    else:
        for a in range(1, len(lists)):
            if lists[a] * lists[a + 1] == n:
                print(f'{n} = {list[a + 1]} * {lists[a]}')
                break
            else:
                continue

factoring(4)
