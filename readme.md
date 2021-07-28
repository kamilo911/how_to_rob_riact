### Brief

In this exercise, let's try to solve a classic problem.

Bob is a thief. After months of careful planning, he finally manages to crack the security systems of a high-class apartment.

In front of him are many items, each with a value (v) and weight (w). Bob, of course, wants to maximize the total value he can get; he would gladly take all of the items if he could. However, to his horror, he realizes that the knapsack he carries with him can only hold so much weight (W).

Given a knapsack with a specific carrying capacity (W), help Bob determine the maximum value he can get from the items in the house. Note that Bob can take only one of each item.

All values given will be strictly positive. Items will be represented as a list of pairs, wi and vi, where the first element wi is the weight of the ith item and vi is the value for that item.

For example:

Items: [ { "weight": 5, "value": 10 }, { "weight": 4, "value": 40 }, { "weight": 6, "value": 30 }, { "weight": 4, "value": 50 } ]

Knapsack Limit: 10

For the above, the first item has weight 5 and value 10, the second item has weight 4 and value 40, and so on.

In this example, Bob should take the second and fourth item to maximize his value, which, in this case, is 90. He cannot get more than 90 as his knapsack has a weight limit of 10.
Exception messages

Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. Not every exercise will require you to raise an exception, but for those that do, the tests will only pass if you include a message.

To raise a message with an exception, just write it as an argument to the exception type. For example, instead of raise Exception, you should write:

raise Exception("Meaningful message indicating the source of the error")

Running the tests

To run the tests, run pytest heist_test.py

Alternatively, you can tell Python to run the pytest module: python -m pytest heist_test.py
Common pytest options

```bash
    -v : enable verbose output
    -x : stop running tests on first failure
    --ff : run failures from previous test before running other test cases
```

For other options, see python -m pytest -h
### Evaluation Criteria

    Python best practices
    Show us your work through your commit history
    Completeness: did you complete the features? Are all the tests running?
    Correctness: does the functionality act in sensible, thought-out ways?
    Maintainability: is it written in a clean, maintainable way?

### Code Submit

Please organize, design, and document your code as if it were going into production - then push your changes to the master branch. After you have pushed your code, you may submit the assignment on the assignment page.

All the best and happy coding,

The RiACT ApS Team
