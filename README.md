# Price formate

The script ```format_price.py``` rounds any price from 45.000 to 45.
The script ```tests.py``` checks the value of  ```format_price.py```

# How to use

There is some methods of check in tests.py:
 
```python
 def test_check_digits(self):
```
There check a price if it is inputed the other digits.
```python
 def test_check_negative(self):
```
There check a price if it is inputed the negative digit.
```python
def test_check_empty(self):
```
There check a price if it is inputed the empty price.
```python
def test_check_string(self):
```
There check a price if it is inputed a string.
```
 def test_cheks_zero(self):
 ```
 There check a price if it is inputed a zero.

You run tests for a price formate like this:
```python
from format_price import get_format_price
import unittest
```


# Running the tests

You can run the scrip to use on Linux python or python3 like this:

``` python3 tests.py ``` 

On Windows you use similarly.


# Project Goals

The code is written for educational purposes. Training course for web-developers -
[DEVMAN.org](https://devman.org))