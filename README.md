# Price formate

The script ```format_price.py``` rounds any price from 45.000 to 45.
The script ```tests.py``` checks the value of def get_format_price

# How to use

```
 python3 format_price.py -p -12.00
 ```
You can output like this:
```
-12
```
 
# Running the tests

You run tests for a price formate like this:

```
from format_price import get_format_price
import unittest
```


You can run the scrip to use on Linux python or python3 like this:

``` python3 format_price.py ``` 

On Windows you use similarly.

You can output tests.py like this:
```
Ran 12 tests in 0.001s

OK
```


# Project Goals

The code is written for educational purposes. Training course for web-developers -
[DEVMAN.org](https://devman.org)