# Programming Assignment 1

## Course: CSCI 360 - Introduction to Artificial Intelligence

-----

### Setting up the environment

Follow the command line instruction below to initialize you repository
locally. Replace `YOUR-GITHUB-REPO-HERE` with the url that GitHub
generates for you repository.

```
git clone YOUR-GITHUB-REPO-HERE

conda env create --file csci360_prog_assingment_1.txt

pip install -r requirements.txt

```

### Writing Your Code:

All of the code that will be evaluated and graded will live in
[`lab1.py`](lab.py).

You can use any python package that is installed by `pip` or `conda`
when you created the environment.

You are provided with [`lab1_utils.py`](`lab1_utils.py`) which contains
the `TextbookStack` class. The constructor for this class expects two
lists that represents the order. The first list `initial_order` is a
list of length `n` that expects each integer `[0, n-1]` to be present
once, The second list `initial_orientation` should be a list of length
`n` of exclusively `0`s and `1`s. Will represent the Textbook facing up.

```
>>> from lab1_utils import TextbookStack

# Construct a stack of books in reverse order
>>> stack = TextbookStack(initial_order=[2, 1, 0], initial_orientations=[0, 0, 0])
>>> print(stack)
TextbookStack:
 	 order: [2 1 0]
	 orientations:[0 0 0]
```


You can access the current order and orientation of the books by
accessing the attributes `TextbookStack.order` and
`TextbookStack.orientations` respectively.

```
>>> stack.order
array([2, 1, 0])
>>> stack.orientations
array([0, 0, 0])
```

Calling the command `flip_stack(position)` will flip the books up to the
`position`. For example if you want to flip the top book of your `stack`
you should call `stack.flip_stack(1)`.

```
>>> stack.flip_stack(2)
>>> stack.order
array([1, 2, 0])
>>> stack.orientations
array([1, 1, 0])
```

You can make a copy of a stack by invoking the `.copy()` this will
create a new object with the same current order and orientations as the
stack from which you invoked the method. You can use `==` to compare the
equivalence of two stacks.

```
>>> new_stack = stack.copy()
>>> new_stack == stack
True
>>> new_stack.flip_stack(3)
>>> new_stack == stack
False
```


Finally, you can check if the stack is ordered by invoking the
`check_ordered`

```
>>> stack.check_ordered()
False
>>> stack.flip_stack(2)
>>> stack.flip_stack(3)
>>> stack.check_ordered()
True
```
All of your algorithm should be contained in the designated blocks
inside of `breadth_first_search` and `depth_first_search` and should
return the sequence of flips that your search algorithms find.

## Testing Your Code:

We have given you example tests that you can run from the terminal by
invoking:

```
python test.py
```

from inside your the directory. These are starting points that reflect
the same type of tests that we will run in order to evaluate and grade
the correctness of your algorithm.
