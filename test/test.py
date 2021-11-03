"""
for vs while
    So we’ve got the for and while loops, which can be used to execute a block of code multiple times. So which do we use and when?
    Usually we’d use the for loop when the number of iterations is fixed. For example, iterating over a fixed list of items in a shopping list.
    The while loop is useful in cases when the number of iterations isn’t known and depends on some calculations and conditions in the code block of the loop.
    For example, ending the loop when the user enters a specific input in a calculator program.
    While both, for and while loops can be used to achieve the same results, however, the for loop has cleaner and shorter syntax, making it a better choice in most cases.
"""

"""
Docstrings:
    (documentation strings) are similar to comments, in that they’re designed to explain code. But! they’re more specific and have a different syntax.
    They’re created by putting a multiline string containing an explanation of the function below the function's first line.
"""


def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))