# Any changes to this file will not be reflected during testing and grading
# While these are some test cases these are not the only cases used in grading
from lab1_utils import TextbookStack, apply_sequence
from lab1 import breadth_first_search, depth_first_search

if __name__ == '__main__':
    n_pass = 0
    n_tests = 0

    test = TextbookStack(initial_order=[3, 2, 1, 0], initial_orientations=[0, 0, 0, 0])
    print(f"Testing  Breadth First Search on\n{test}")
    sequence = breadth_first_search(test)
    new_stack = apply_sequence(test, sequence)
    expected_sequence = [4]
    correct_sequence = (expected_sequence == sequence)

    print(f"Stack is {'' if new_stack.check_ordered() else 'not '}ordered")
    n_pass += int(correct_sequence)
    n_tests += 1
    print(f"Tests:{n_tests} - Passed: {n_pass}\n")

    print(
        f"Comparing output to expected traces  - "
        f"\t{'PASSED' if correct_sequence else 'FAILED'}"
    )

    n_pass += int(correct_sequence)
    n_tests += 1
    print(f"Tests:{n_tests} - Passed: {n_pass}\n")

    print(f"Testing  Depth First Search on\n{test}")
    sequence = depth_first_search(test)
    new_stack = apply_sequence(test, sequence)
    expected_sequence = [4]
    expected_sequence_alt = [
        1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1,
        2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 4, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2,
        1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 4, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1,
        3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 4, 1, 2, 1, 2,
        1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1,
        2, 1, 2, 1, 2, 1, 4, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2,
        1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 4, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1,
        2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 4, 1, 2, 1, 2, 1, 2, 1, 3,
        1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1,
        2, 1, 4, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2,
        1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1

    ]
    correct_sequence = (expected_sequence == sequence) or (expected_sequence_alt == sequence)
    n_pass += int(correct_sequence)
    n_tests += 1
    print(f"Tests:{n_tests} - Passed: {n_pass}\n")

    print(
        f"Comparing output to expected traces  - "
        f"\t{'PASSED' if correct_sequence else 'FAILED'}"
    )

    n_pass += int(correct_sequence)
    n_tests += 1
    print(f"Tests:{n_tests} - Passed: {n_pass}\n")

    # ---- Larger Test --- #
    test = TextbookStack(initial_order=[3, 2, 0, 1], initial_orientations=[0, 1, 1, 1])
    print(f"Testing  Breadth First Search on\n{test}")
    sequence = breadth_first_search(test)
    new_stack = apply_sequence(test, sequence)
    expected_sequence = [4, 3, 1, 3, 2]
    expected_sequence_alt = [2, 1, 2, 4, 2]
    correct_sequence = (expected_sequence == sequence) or (expected_sequence_alt == sequence)

    print(f"Stack is {'' if new_stack.check_ordered() else 'not '}ordered")
    n_pass += new_stack.check_ordered()
    n_tests += 1
    print(f"Tests:{n_tests} - Passed: {n_pass}\n")

    print(
        f"Comparing output to expected traces  - "
        f"\t{'PASSED' if correct_sequence else 'FAILED'}"
    )

    n_pass += int(correct_sequence)
    n_tests += 1
    print(f"Tests:{n_tests} - Passed: {n_pass}\n")

    print(f"Testing  Depth First Search on\n{test}")
    sequence = depth_first_search(test)
    new_stack = apply_sequence(test, sequence)
    expected_sequence = [
        4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 2, 4, 3, 4, 3, 4,
        3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3,
        4, 3, 4, 3, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 1, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4,
        2, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 2, 4, 3, 4, 3,
        4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4,
        3, 4, 3, 4, 3, 4, 1, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3,
        4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 2, 4, 3, 4,
        3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 1, 4, 3, 4, 3
    ]

    expected_sequence_alt = [
        1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1,
        2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 4, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2,
        1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 4, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1,
        3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 4, 1, 2, 1, 2,
        1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1,
        2, 1, 2, 1, 2, 1, 4, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2,
        1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 4, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1,
        2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 4, 1, 2, 1, 2, 1, 2, 1, 3,
        1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1,
        2, 1, 4, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2
    ]

    correct_sequence = (expected_sequence == sequence) or (expected_sequence_alt == sequence)

    print(f"Stack is {'' if new_stack.check_ordered() else 'not '}ordered")
    n_pass += new_stack.check_ordered()
    n_tests += 1
    print(f"Tests:{n_tests} - Passed: {n_pass}\n")

    print(
        f"Comparing output to expected traces - "
        f"\t{'PASSED' if correct_sequence else 'FAILED'}"
    )

    n_pass += int(correct_sequence)
    n_tests += 1
    print(f"Tests:{n_tests} - Passed: {n_pass}\n")

