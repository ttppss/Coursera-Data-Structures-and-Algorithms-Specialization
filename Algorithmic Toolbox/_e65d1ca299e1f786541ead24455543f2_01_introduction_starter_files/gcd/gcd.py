# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    if a<b:
    	lst = [a, b%a]
    	while(lst[-1] != 0):
    		lst.append(lst[-2]%lst[-1])
    	return lst[-2]
    elif a>b:
    	lst = [b, a%b]
    	while(lst[-1] != 0):
    		lst.append(lst[-2]%lst[-1])
    	return lst[-2]

if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
