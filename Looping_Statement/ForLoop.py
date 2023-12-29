# WAP to count the number of digits and alphabet in a string

string = input("Enter the string")
num_count = 0
char_count = 0
void_space_Count = 0
spcl_count=0

for element in string:

    askii = ord(element)
    if (askii>=65 and askii<=90) or (askii>=97 and askii<=122):
        char_count+=1
    elif(askii>=48 and askii<=57):
        num_count+=1
    elif(askii==32):
        void_space_Count+=1
    else:
        spcl_count+=1
print(f'Char Count is {char_count}')
print(f'Num Count is {num_count}')
print(f'void space Count is {void_space_Count}')
print(f'spcl Count is {spcl_count}')
