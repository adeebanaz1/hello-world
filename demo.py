"""Module to calculate area of a circle."""

def area_of_circle(radius):
  """
  Calculate the area of Circle

  Args:
    radius(float) : Radius of the  Circle

  Returns:
    float : Area of the Circle
  """
  
  pi = 3.14
  return pi*radius*radius

def main():
    """Main function to print area of a circle with radius 10."""
    area = area_of_circle(10)
    print(area)


if __name__ == "__main__":
  main()
