a = int(input("Enter the number of students in class 1: "))
b = int(input("Enter the number of students in class 2: "))
c = int(input("Enter the number of students in class 3: "))
desks_a = (a + 1) // 2
desks_b = (b + 1) // 2
desks_c = (c + 1) // 2
total_desks = desks_a + desks_b + desks_c
print(f"The total number of desks needed is: {total_desks}")