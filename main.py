import math

def calculate_gcd_lcm(num1, num2):
    gcd = math.gcd(num1, num2)
    lcm = (num1 * num2) // gcd
    return gcd, lcm

num1, num2 = map(int, input("Please enter two numbers: ").split())

gcd, lcm = calculate_gcd_lcm(num1, num2)

print(f"{gcd} {lcm}")
