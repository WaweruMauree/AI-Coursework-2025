import math

def days_to_seconds():
    """Program 1: Convert days to seconds"""
    print("\n=== Days to Seconds Converter ===")
    try:
        days = float(input("Enter the number of days: "))
        seconds = days * 24 * 60 * 60  # days * hours * minutes * seconds
        print(f"{days} days = {seconds:,.0f} seconds")
    except ValueError:
        print("Please enter a valid number.")

def sphere_volume():
    """Program 2: Calculate volume of a sphere"""
    print("\n=== Sphere Volume Calculator ===")
    try:
        radius = float(input("Enter the radius of the sphere: "))
        if radius < 0:
            print("Radius cannot be negative.")
            return
        
        # Volume formula: (4/3) * π * r³
        volume = (4/3) * math.pi * (radius ** 3)  # Using exponential operator **
        print(f"Volume of sphere with radius {radius} = {volume:.2f} cubic units")
    except ValueError:
        print("Please enter a valid number.")

def square_area_perimeter():
    """Program 3: Calculate area and perimeter of a square using functions"""
    
    def calculate_area(side):
        """Calculate area of square"""
        return side ** 2
    
    def calculate_perimeter(side):
        """Calculate perimeter of square"""
        return 4 * side
    
    print("\n=== Square Area and Perimeter Calculator ===")
    try:
        side_length = float(input("Enter the side length of the square: "))
        if side_length < 0:
            print("Side length cannot be negative.")
            return
        
        area = calculate_area(side_length)
        perimeter = calculate_perimeter(side_length)
        
        print(f"Square with side length {side_length}:")
        print(f"Area = {area:.2f} square units")
        print(f"Perimeter = {perimeter:.2f} units")
    except ValueError:
        print("Please enter a valid number.")

def check_case():
    """Program 4: Determine if character is uppercase or lowercase"""
    
    def determine_case(char):
        """Function to determine case of character"""
        if char.isupper():
            return "uppercase"
        elif char.islower():
            return "lowercase"
        elif char.isalpha():
            return "letter (neither upper nor lower case)"
        else:
            return "not a letter"
    
    print("\n=== Character Case Checker ===")
    char = input("Enter a character: ")
    
    if len(char) != 1:
        print("Please enter exactly one character.")
        return
    
    case_type = determine_case(char)
    print(f"The character '{char}' is {case_type}.")

def pseudocode_program():
    """Program 5: Python equivalent of given pseudocode"""
    print("\n=== Pseudocode Program ===")
    
    # SET x TO 0, y TO 20
    x = 0
    y = 20
    
    print("Initial values: x = 0, y = 20")
    print("Processing loop:")
    
    # REPEAT ... UNTIL y IS LESS THAN 6
    iteration = 1
    while y >= 6:
        print(f"Iteration {iteration}: y = {y}, x = {x:.4f}")
        
        # SUBTRACT 4 FROM y
        y = y - 4
        
        # ADD 2/y TO x
        x = x + (2 / y)
        
        iteration += 1
    
    print(f"Final result: x = {x:.6f}")

def array_average():
    """Program 6: Input 5 values and calculate average"""
    print("\n=== Array Average Calculator ===")
    
    # Initialize array to store 5 values
    values = []
    
    print("Please enter 5 values:")
    
    # Use loop to get 5 values from user
    for i in range(5):
        try:
            value = float(input(f"Enter value {i + 1}: "))
            values.append(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return
    
    # Calculate average
    total = sum(values)
    average = total / len(values)
    
    # Display results
    print(f"\nValues entered: {values}")
    print(f"Sum of values: {total}")
    print(f"Average: {average:.2f}")

def main():
    """Main menu function"""
    while True:
        print("\n" + "="*50)
        print("PYTHON PROGRAMS COLLECTION")
        print("="*50)
        print("1. Days to Seconds Converter")
        print("2. Sphere Volume Calculator") 
        print("3. Square Area and Perimeter Calculator")
        print("4. Character Case Checker")
        print("5. Pseudocode Program")
        print("6. Array Average Calculator")
        print("7. Exit")
        print("="*50)
        
        choice = input("Select a program (1-7): ").strip()
        
        if choice == '1':
            days_to_seconds()
        elif choice == '2':
            sphere_volume()
        elif choice == '3':
            square_area_perimeter()
        elif choice == '4':
            check_case()
        elif choice == '5':
            pseudocode_program()
        elif choice == '6':
            array_average()
        elif choice == '7':
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Please enter 1-7.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

