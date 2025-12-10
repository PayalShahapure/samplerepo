import arithmetic
import geometry


print("Hello World!!")

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))

arithmetic.add(num1,num2)

arithmetic.sub(num1,num2)


len=int(input("Enter len:"))
br=int(input("Enter br:"))

geometry.calc_rect_area(len,br)
geometry.calc_rect_peri(len,br)