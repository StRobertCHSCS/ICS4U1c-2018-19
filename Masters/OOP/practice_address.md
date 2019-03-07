# practice_address.py

1. Define a class called Address that has the attributes below.  
All fields have a default value of “” (empty string) except for country 
which is defaulted to “Canada”
```
address_line1: str
address_line2: str
postal_code: str
city: str
province: str
country: str
```

2. Define a `main()` function and within it, create two Address instances, one called `home_address`, another called `work_address`. 
Assign values to the object fields. Use the instances to print out each address in a format similar to the following:

```text
street address line 1
street address line 2 (if it has a value)
city, province, postalcode
Country
```

3. Write a `print_address(addr)` function that takes an Address object 'addr' and prints out an 
address in the format specified in the question 2.  Edit your `main()` function to print ou the `home_address` and `work_address` using the `print_address()` function. 
