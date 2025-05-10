def insert_element(lst):
    element = int(input("Enter an element to insert: "))
    lst.append(element)
    print(lst)

def remove_element(list):
    element = int(input("Enter an element to remove:  "))
    if element in lst:
        lst.remove(element)
    else:
        print("Element not found in the list. ")
    print(lst)

def append_element(lst):
    element = int(input("Enter an element to append: "))
    lst.append(element)
    print(lst)

def length(lst):
    print(f"Size of the list is: {len(lst)}")

def pop_element(lst):
    if lst:
        lst.pop()
    else:
        print("The list is already empty.")
    print(lst)

def clear_list(lst):
    lst.clear()
    print(lst)

lst = [1,4,5,2]
print(f"Given list is {lst}")

flag=True
while flag:
     print("<--------------MENU-------------->")
     print("1. Insert")
     print("2. Remove")
     print("3. Append")
     print("4. Length")
     print("5. Pop")
     print("6. Clear")
     print("<-------------------------------->")

     choice = int(input("Enter your choice: "))

     if choice == 1:
         insert_element(lst)
     elif choice == 2:
         remove_element(lst)
     elif choice == 3:
         append_element(lst)
     elif choice == 4:
         length(lst)
     elif choice == 5:
         pop_element(lst)
     elif choice == 6:
         clear_list(lst)
     else:
         print("Invalid input.")
     
    
     pick = input("Do you want to continue (y/n): ")
     if pick == 'y' or pick == 'yes':
        flag = True
        print()
     elif pick == 'n' or pick == 'no':
          flag = False
     else:
         print("Please enter a valid input (y/n): ")