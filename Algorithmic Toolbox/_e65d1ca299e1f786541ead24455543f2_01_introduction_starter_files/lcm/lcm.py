# Uses python3
import sys

def lcm_naive(a, b):
    current_gcd = 1
    if a<b:
    	lst = [a, b%a]
    	while(lst[-1] != 0):
    		lst.append(lst[-2]%lst[-1])
    	current_gcd = lst[-2]
    elif a>b:
    	lst = [b, a%b]
    	while(lst[-1] != 0):
    		lst.append(lst[-2]%lst[-1])
    	current_gcd = lst[-2]
    
    return (a * b / current_gcd)
    
if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

