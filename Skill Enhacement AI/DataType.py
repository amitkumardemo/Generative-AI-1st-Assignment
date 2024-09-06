# Basic data types in Python:
int_example = 10  # Integer
float_example = 10.5  # Float
string_example = "Hello"  # String
list_example = [1, 2, 3]  # List
tuple_example = (1, 2, 3)  # Tuple
dict_example = {'name': 'John', 'age': 25}  # Dictionary

# Mutable vs Immutable:
# Mutable: Can be changed after creation
list_example[0] = 10  # Lists are mutable
# Immutable: Cannot be changed after creation
try:
    tuple_example[0] = 10  # Tuples are immutable, this will raise an error
except TypeError:
    print("Tuples are immutable.")
