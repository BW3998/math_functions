from math import *

def radians(deg):
    return deg * pi / 180

def find_factors(num):
    factors = []
    num = abs(num)
    for i in range (1,num+1):
        if num % i == 0:
            factors.append(i)
    return factors

def rational_roots(constant,*coefficients):
    n = len(coefficients)
    n_factors = find_factors(coefficients[-1])
    constant_factors = find_factors(constant)
    roots = []
    for p in constant_factors:
        for q in n_factors:
            num = p/q
            test = constant
            for i in range(1,n+1):
                test += coefficients[i-1] * (num**i)
            if test == 0:
                roots.append(num)
    return roots

def heron(a,b,c):
    s = (a+b+c)/2
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    return area

def to_base(num,base):
    digits = ""
    while num:
        x = int(num) % base
        # print(x)
        digits = str(x) + digits
        num = int((num - x) / base)
        # print(num)
    return(int(digits))

def from_base(num,base):
    ans = 0
    num = str(num)
    for i in range(0,len(num)):
        position = (i+1)*-1
        # print(position)
        new_digit = (base**i)*int(num[position])
        # print(new_digit)
        ans += new_digit 
    return(ans)

def base_converter(first_base,second_base,num):
    num = from_base(num,first_base)
    return(to_base(num,second_base))

def reg_polygon(s,n):
    area = (n*(s**2))/(4*(tan(radians(180/n))))
    interior_angle = 180*(n-2)/n
    return area, interior_angle

def shoelace(*coordinates):
    n = len(coordinates)
    x_values = []
    y_values = []
    for i in range(0,n):
        if i % 2 == 0:
            y_values.append(coordinates[i])
        else:
            x_values.append(coordinates[i])
    first_num = x_values[-1]*y_values[0]
    second_num = y_values[-1]*x_values[0]
    for x in range(0,int(n/2-1)):
        first_num += x_values[x]*y_values[x+1]
        second_num += y_values[x]*x_values[x+1]
    area = (first_num-second_num)/2
    return area

def permutation(n,r):
    numerator = factorial(n)
    denominator = factorial(n-r)
    ans = numerator/denominator
    return ans

def combination(n,r):
    ans = permutation(n,r)/(factorial(r))
    return ans

def arithmetic_series(first_term,last_term,n):
    ans = (first_term+last_term)*n/2
    return ans

def geometric_series(first_term,ratio,n):
    ans = (first_term*(1-(ratio**n)))/(1-ratio)
    return ans

def factors_sum(num):
    ans = 0
    for i in find_factors(num):
        ans += i
    return ans

def sine_triangle_area(a,b,angle_c):
    area = a*b*(sin(angle_c))/2
    return area

# heron()
# base_converter()
# rational_roots()
# reg_polygon()
# shoelace()
# permutation()
# combination()
# arithmetic_series()
# geometric_series()
# find_factors()
# factors_sum()

# Stewarts Theorem: b^2m+c^2n = a(d^2+mn)
# Cubic Vieta: (ax^3+bx^2+cx+d)
## Sum of roots: -b/a
## Sum of product of roots: c/a
## Product of roots: -d/a
# Sum of First n Odd: n^2
# Sum of First n Even: n(n+1)
# Sum of First n Integers: n(n+1)/2
#