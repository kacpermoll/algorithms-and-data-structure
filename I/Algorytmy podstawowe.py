#Wyszukiwania największej liczby w danym zbiorze (każda liczba jest oddzielona średnikiem i mogą to być liczby zmiennoprzecinkowe)
"""
number = 0

lis_of_numbers = [0.11,12, 13.12, 14.44, 15, 6.142, -0.1, 14.99, 17]

for i in range(len(lis_of_numbers)):
    if number<lis_of_numbers[i]:
        number = lis_of_numbers[i]
    
print("The gratest number in your list is ", number)
"""

#Konwersja odwrotnej notacji polskiej (w obie strony).
priority = {
    '(':0,
    ')':0,
    '+':1,
    '-':1,
    '*':2,
    '/':2,
    "^":3
}
stack = []
result=[]
operations_list = []

def test_higher_priority(operator1, operator2):
    higher_priority = operator2
    
    if priority[operator1] >= priority[operator2]:
        higher_priority = operator1

    return higher_priority

operation = input("Please enter your operation(without whitespaces): ")

i=0
while i < len(operation):
    #checking if the character is a number to correctly assign greater numbers than 9
    if operation[i].isnumeric():
    
        number_to_move=""
        while operation[i].isnumeric():
            #concatenating into the correct number 
            number_to_move=number_to_move+operation[i]

            i +=1    
            #breaking the loop to not go out of string range 
            if i>len(operation)-1:
                break
        #moving the number to the list
        operations_list.append(number_to_move)
    
    else:
        
        #moving number to the list
        operations_list.append(operation[i])
        i+=1

#first number/operator always goes straight away into result list
result.append(operations_list[0])

for i in range(1,len(operations_list)):

    if i>len(operations_list)-1:
        break
    #if following character is a number move it to result list
    elif operations_list[i].isnumeric():
        result.append(operations_list[i])
    #if following character is an operator check other conditions
    else:
        #if stack is empty put operator on the stack
        if not stack:
            stack.append(operations_list[i])

        elif operations_list[i]=="(":
            stack.append(operations_list[i])

        #put operator on a stack if the taken operator is greater than the last operator on a stack
        elif operations_list[i] == test_higher_priority(operations_list[i],stack[-1]):
            stack.append(operations_list[i])
        #while the taken operator is equal or less than the last operator,
        #move last operator from stack into result list, then put taken operator on a stack 
        elif stack[-1] >= test_higher_priority(operations_list[i],stack[-1]): 
            while stack[-1] >= test_higher_priority(operations_list[i],stack[-1]):
                result.append(stack.pop())
                if not stack:
                    break
            stack.append(operations_list[i])

while stack:
    
    if stack[-1] == "(" or stack[-1] == ")":
        stack.pop()
    else:
        result.append(stack.pop())
  
print(result)


for i in result:
    if i.isnumeric():
        stack.append(i)
    else:
        a,b = stack.pop(), stack.pop()
        stack.append(f"({b}{i}{a})")

print(stack)


    