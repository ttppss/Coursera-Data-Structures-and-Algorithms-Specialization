# Uses python3
import sys

def get_change(m):
    #write your code here
    counter = 0
    ten = int(m/10)
    #print(ten)
    five = int(m%10/5)
    #print(five)
    one = int(m%10%5)
    #print(one)
    counter = ten + five + one
    return counter

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
