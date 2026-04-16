try:
    a = float(input("Enter the numerator: "))
    b = float(input("Enter the denominator: "))
    
    result = a/b

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numeric values.")

else:
    print("Division successful!")
    print("Result:", result)

finally:
    print("Execution completed.")