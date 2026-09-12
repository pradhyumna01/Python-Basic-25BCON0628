n = int(input("Enter the number of terms: "))
t1, t2 = 0, 1
print("Fibonacci Series: ", end="")
for i in range(1, n + 1):
    print(t1, end=", ")
    t1, t2 = t2, t1 + t2
