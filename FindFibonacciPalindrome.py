def FindFibonacciPalindrome(sequence):
    if sequence == None or len(sequence) < 1:
        return ()
    start_index = 0
    max_sub_seq_len = 0
    for i in range(len(sequence)):
        len1 = centerExpand(sequence, i, i)
        if len1 > max_sub_seq_len:
            sub_seq = sequence[i - (len1 - 1) // 2: i + (len1 - 1) // 2 + 1]
            if isFibonacci(sub_seq):
                start_index = i - (len1 - 1) // 2
                max_sub_seq_len = len1
        len2 = centerExpand(sequence, i, i + 1)
        if len2 > max_sub_seq_len:
            sub_seq = sequence[i - len2 // 2 + 1: i + len2 // 2 + 1]
            if isFibonacci(sub_seq):
                start_index = i - len2 // 2 + 1
                max_sub_seq_len = len2
    return start_index, max_sub_seq_len


def centerExpand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1


def isFibonacci(sequence):
    if len(sequence) < 3:
        return True
    for i in range(0, len(sequence) - 2):
        if not (sequence[i] == sequence[i + 2] or sequence[i] == sequence[i + 1] + sequence[i + 2] or sequence[i + 2] == sequence[i] + sequence[i + 1]):
            return False
    return True