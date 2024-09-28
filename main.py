import math

def calculate_circumference(radius):
    # Formula for circumference: C = 2 * π * r
    circumference = 2 * math.pi * radius
    return circumference

# Example usage
radius = float(input("Enter the radius of the circle: "))
circumference = calculate_circumference(radius)
print(f"The circumference of the circle is: {circumference}")
