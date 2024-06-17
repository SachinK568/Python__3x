# pi = 3.142
# r=int(input("radius of circle:"))
# area =pi*r*r
# print(area)

def area_circle(r):
    pi=3.142
    area=pi*r*r #Core logic
    return area
r=int(input("Enter r\n"))
print("Area value=",area_circle(r))
print(area_circle(10))
