T = int(input())
 
for _ in range(T):
    n = int(input())
    r = input()
    b = input()
    
    red_wins = 0
    blue_wins = 0
    
    for i in range(n):
        if r[i] > b[i]:
            red_wins += 1
        elif b[i] > r[i]:
            blue_wins += 1
            
    if red_wins > blue_wins:
        print("RED")
    elif blue_wins > red_wins:
        print("BLUE")
    else:
        print("EQUAL")