#Make a program that says if the first and last items in a list are the same

list_one=[1,2,5,1,2,0,6,1]
list_two=[2,4,5,5,6,1,2,3,4]

def check_alpha_omega(array):
    print(array)
    if array[0]==array[-1]:
        print("the elements are the same")
    else:
        print("the elements are not the same")

check_alpha_omega(list_one)
print(' ')
check_alpha_omega(list_two)

