# practice_rectangle2.py

1. Create a python file `practice_rectangle2.py`.  Modify the program below to so that it has a constructor method that takes a width and height
and sets the attributes accordingly.

```
class Rectangle(object):
    """
    A class representing a rectangle
    """

    def __init__(self):
        """
        Initialize the rectangle dimensions
        :return: None
        """
        self.width = 0
        self.height = 0
```

2.  Add a method to the Rectangle class `get_area()` that returns the area of the rectangle.

3. Write a main() method (outside the class) that creates 3 rectangle instances and prints out the area of each.