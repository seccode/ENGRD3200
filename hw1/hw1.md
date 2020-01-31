# Problem Set 1
## 1.)
```
import numpy as np

# True smallest positive real number
smallest = np.nextafter(0, 1)  # 5e-324

# True Machine Epsilon
eps = np.finfo(float).eps  # 2.220446049250313e-16

# Function to manually find Machine Epsilon


def findEps():
    prev, curr = 1, 1
    while (1 + curr) > 1:
        prev, curr = curr, curr / 2
    return prev

# Function to manually find smallest positive real number


def findSmallest():
    prev, curr = 1, 1
    while (curr - 0) != 0:
        prev, curr = curr, curr / 2
    return prev


# Assert manual functions produce correct results
assert findEps() == eps, "Calculated machine epsilon is incorrect"
assert findSmallest() == smallest, "Calculated smallest positive \
                                real number is incorrect"

```
The results we get from running the above code is that our assertions are correct. Our calculated machine epsilon and smallest positive real number (2.220446049250313e-16 and 5e-324 respectively), match those found by explicitly querying these values in Python.

## 2.)
![alt text](hw1p2.jpg)

## 3.)
## 4.)
## 5.)