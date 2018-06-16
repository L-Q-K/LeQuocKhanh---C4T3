import ex_one as one
import ex_two as two
import ex_three as three
import ex_four as four

n = input("n: ")

if n.isdigit():
    n = int(n)
    ex_one_result = one.dec_list(n)
    print("Bài 1:", ex_one_result)
else:
    print("Bài 1: n không hợp lệ")
    
ex_two_result = two.raise_power()
print("Bài 2:", ex_two_result)

x = [0, -1.5, -3.14, 4, 7, 5, 30]
ex_three_result = three.pi_sin_cos_list(x)
print(ex_three_result)

ex_four_result = four.sum_list_abssum_list_abs(x)
print(ex_four_result)
    
