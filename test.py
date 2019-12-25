from FindFibonacciPalindrome import FindFibonacciPalindrome
def test():
    test_case = [
        # startIndex is left boundary and palindrome's length is equal to 1
        ([1], (0, 1)),
        ([1, 2], (0, 1)),
        ([1, 2, 3], (0, 1)),
        # startIndex is left boundary and palindrome's length is great to 1
        ([1, 2, 1], (0, 3)),
        ([1, 2, 2, 1], (0, 1)),
        ([1, 2, 3, 2, 1], (0, 5)),
        ([1, 2, 3, 3, 2, 1], (0, 1)),
        ([3, 0, 3, 3, 0, 3], (0, 6)),
        # startIndex is not left boundary
        ([100, 101, 3, 0, 3, 3, 0, 3, 30, 20], (2, 6))
    ]
    for item in test_case:
        res = FindFibonacciPalindrome(item[0])
        expected = item[1]
        e = 'sequence is {}, {} is expected, res is {}'.format(str(item[0]), str(item[1]), res)
        assert res == expected, e


if __name__ == '__main__':
    test()