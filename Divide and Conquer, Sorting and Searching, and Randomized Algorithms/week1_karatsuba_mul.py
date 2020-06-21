def decrease_order_twice(long_int: str, min_len: int) -> (str, str):
    return long_int[:-min_len], long_int[-min_len:]


def spit_to_four_parts(first_number, second_number):
    min_len = min(len(first_number), len(second_number)) // 2
    a, b = decrease_order_twice(first_number, min_len)
    c, d = decrease_order_twice(second_number, min_len)
    return a, b, c, d, min_len


def karatsuba_mul(first_number, second_number):
    if len(first_number) <= 1 or len(second_number) <= 1:
        return int(first_number) * int(second_number)

    a, b, c, d, min_len = spit_to_four_parts(first_number, second_number)

    first = int(karatsuba_mul(a, c))
    third = int(karatsuba_mul(b, d))

    gauss_trick_1 = str(int(a) + int(b))
    gauss_trick_2 = str(int(c) + int(d))
    second = int(karatsuba_mul(gauss_trick_1, gauss_trick_2)) - first - third

    return (10 ** (min_len * 2) * first + 10 ** (min_len) * second + third)


num1 = '3141592653589793238462643383279502884197169399375105820974944592'
num2 = '2718281828459045235360287471352662497757247093699959574966967627'

print(
    3141592653589793238462643383279502884197169399375105820974944592 * 2718281828459045235360287471352662497757247093699959574966967627 == karatsuba_mul(
        num1, num2))  # True
