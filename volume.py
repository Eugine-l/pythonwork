import math
def calculate_cylinder_volume(radius,height):
    base_area = math.pi*radius**2
    volume = base_area*height
    return volume
radius = 6
height = 24
volume = calculate_cylinder_volume(radius,height)
print("Volume of the cylinder:",volume)
