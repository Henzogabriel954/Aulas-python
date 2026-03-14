Months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while True:
    num = int(input("Enter a number from 1 to 12. Exit 0: "))
    if num == 0:
        print("leaving...")
        break
    try:
        print(Months[num-1])
    except IndexError:
        print("Invalid number. Please enter a number from 1 to 12 or 0 to exit.")