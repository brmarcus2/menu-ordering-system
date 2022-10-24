# Menu Ordering System

## Code Hierarchy
All source code is in the src directory. The arguments are parsed are validated in order.py.
An Order object is created with the validated arguments and creates a Breakfast, Lunch, or Dinner object depending on the arguments given. 

The Breakfast, Lunch, and Dinner objects are subclasses of Meal. The common functions are implemented in Meal, and the specific requirements for each meal are implemented in Breakfast, Lunch, or Dinner. 

## Running the Program
The program is designed to be run from the command line with the meal (Breakfast, Lunch, or Dinner) as the first argument and the specific order as the second argument.

Then an error or the successful order will be printed to screen. For example, if run from the root directory:

* Input: ```python src/order.py Breakfast 1,2,3```


* Output: ```Eggs, Toast, Coffee```

## Testing
All unit tests are in the test directory and use pytest. Running the command pytest from the command line in the root directory will run all unit tests.

## Requirements
Python3 and pytest are required.