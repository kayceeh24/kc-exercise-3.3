# Exercise 3.3 - Months and Years

In this assignment, you will write functions that deal with the lengths of months and years.

## Requirements

Write the following functions.

### Is Leap Year Function

Create the function `is_leap_year` which takes a year as its only argument and returns a Boolean value.  It should return `True` if the given year is a [leap year](https://www.mathsisfun.com/leap-years.html) and `False` otherwise.

This flowchart shows how to determine if a year is a leap year:

![Leap Year Flowchart](https://mrdevet.github.io/ICS3C/assets/images/leap_year.png)

For this function, you will need to determine if the year is evenly divisible by some numbers.  If a number is evenly divisible by a divisor, the remainder will be 0 when divided by that divisor.

Python has the `%` operator, which finds the remainder when dividing another numbers.  If you want to see if `num` divide evenly be `7`, you could use:

```python
if num % 7 == 0:
    ...
```

HINT: You might use nested if structures for this function, though it is not necessary.

**Sample Console**

```
> is_leap_year(2022)
False
> is_leap_year(2020)
True
> is_leap_year(2000)
True
> is_leap_year(1900)
False
```

### Days in Month Function

Also create the function `days_in_month` which takes a year and a month number (`1` = January and `12` = December) as arguments.  The function will return the number of days in that month.

This images shows the number of days in each month.

![Days in Each Month](https://mrdevet.github.io/ICS3C/assets/images/days_in_month.png)

Note that February has 29 days if it is a leap year and 28 days otherwise.  Your function should call `is_leap_year` to determine if the given year is a leap year instead of rewriting that code.

**Sample Console**

```
> days_in_month(2022, 11)
30
> days_in_month(2022, 2)
28
> days_in_month(2022, 1)
31
> days_in_month(2020, 2)
29
```

## Submitting

When you are finished, push your code to GitHub.  Submit it on [Gradescope](gradescope.com) where it will be graded:
* Correctness - 80% (automatic)
* Style - 20% (manual - see [Style Guide](https://mrdevet.github.io/ICS3C/assignments/Style-Guide/))

## Resources

The following lessons will be helpful with this exercise:

* **[Creating Functions](https://mrdevet.github.io/ICS3C/essentials/3-functions/1-Creating-Functions/)**
  * [Defining Functions](https://mrdevet.github.io/ICS3C/essentials/3-functions/1b-Defining-Functions/)
  * [Parameters](https://mrdevet.github.io/ICS3C/essentials/3-functions/1c-Parameters/)
  * [Return Values](https://mrdevet.github.io/ICS3C/3-functions/1d-Return-Values/)
