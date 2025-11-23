import pandas as pd

#Take user input for numbers
n = int(input("Enter how many rows of numbers you want: "))

data = {'A': [], 'B': []}

for i in range(n):
    a = float(input(f"Enter value A{i+1}: "))
    b = float(inpuprintt(f"Enter value B{i+1}: "))
    data['A'].append(a)
    data['B'].append(b)

#create DataFrame
df = pd.DataFrame(data)

#Ask user which operation to perform
print("\nSelect operations:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")

if choice == '1':
    df['Result'] = df['A'] + df['B']
    operation = "Addition"
elif choice == '2':
    df['Result'] = df['A'] - df['B']
    operation = "Subtraction"
elif choice == '3':
    df['Result'] = df['A'] * df['B']
    operation = "Multiplication"
elif choice == '4':
    df['Result'] = df['A'] / df['B']
else:
    print("Invalid choice!")
    exit()

print(f"\nPandas Calculator = (operation) Result:\n")
print(df)