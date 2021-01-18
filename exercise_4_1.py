"""
Created on Mon Sep 21 18:21:22 2020

@author: giris
"""

def compute_parity(x: int) -> int:
    parity_x = []
    pre_compute_parity = [10] * 16
    # Create array of pre-computed parities for 4 bit nibbles
    for i in range(0,16):
        p = i
        p ^= (p>>2)
        p ^= (p>>1)
        pre_compute_parity[i] = p & 1
    for num in x:
        p = num
        p ^= (p>>32)
        p ^= (p>>16)
        p ^= (p>>8)
        p ^= (p>>4)
        p = pre_compute_parity[p & 15] 
        parity_x.append(p)
    return parity_x


if __name__ == '__main__':
    x = [2**3, 2**14-1, 24, 13]
    expected_parity = [1, 0, 0, 1]
    #actual_parity = [1, 14, 2, 3]
    actual_parity = compute_parity(x)
    if actual_parity == expected_parity:
        print ("SUCCESS")
    else:
        print("Actual = ", actual_parity, "\nExpected = ", expected_parity)
