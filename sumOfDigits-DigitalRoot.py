def digit_sum(n):
    if n<10:
        return n
    return n%10 + digit_sum(n//10)
def digital_root(n):
    if n < 10:
        return n
    return digital_root(digit_sum(n))