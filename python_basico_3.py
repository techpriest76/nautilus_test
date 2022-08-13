#say if a given number is a palindrome

def is_pali(list1,list2):
    for i in range(len(list1)):
        if list1[i]!=list2[i]:
            return False
        return True

number=str(input("give me a number and I'll tell you if it's a palindrome: "))
number_list=[]
reversed_list=[]
for i in number:
    number_list.append(int(i))
    reversed_list.append(int(i))
reversed_list.reverse()

if is_pali(number_list,reversed_list):
    print("it's a palindrome!")
else:
    print("it's not a palindrome :(")
