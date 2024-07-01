# tower of hanoi
def toh(n,s,t,d):
    if n == 0:
        return 
    toh(n-1,s,d,t)
    print(f"Move {n} from {s} to {d}")
    c[0] +=1
    toh(n-1,d,t,s)
c = [0]
n = 3
toh(n,'s','t','d')
print(c)
