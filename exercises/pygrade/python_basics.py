import numpy as np
import re


def solution_one(A):
    # Must be less than 45 bytes
    # OK: 43 bytes
    return np.stack([A[i : i + 7] for i in range(10)])


def solution_two(A):
    # Must be less than 40 bytes
    # NG: 55 bytes
    # return A.replace('t', '*').replace('o', 't').replace('*', 'o')
    # NG: 61 bytes
    # return re.sub('_', '', re.sub(r'o(?!_)', 't', re.sub('t', 'o_', A)))
    # NG: 48 bytes
    # return A.translate(str.maketrans({'t': 'o', 'o': 't'}))
    # OK: 38 bytes
    # Ref: https://qiita.com/tag1216/items/df6c93bdb823dd48af6c
    return A.translate(str.maketrans('to', 'ot'))


def solution_three(A):
    # Must be less than 32 bytes
    # NG: 51 bytes
    # return ", ".join([s for s in A if re.match(r"[A-Z]+", s)])
    # NG: 43 bytes
    # return ", ".join([s for s in A if s[0].isupper()])
    # NG: 40 bytes
    # return ", ".join([s for s in A if s.istitle()])
    # NG: 33 bytes
    # return ", ".join(filter(str.istitle, A))
    # OK? 32 bytes
    return ", ".join(filter(str.istitle,A))


def solution_four(A):
    # Must be less than 10 bytes
    # NG: 19 bytes
    # return A[:,0].reshape(1,5)
    # NG: 17 bytes
    # return A[np.newaxis,:,0]
    # NG: 11 bytes
    # Ref: https://deepage.net/features/numpy-newaxis.html
    return A[None,:,0]
    # Give up!


def solution_five(A):
    # Must be less than 12 bytes
    # NG: 18 bytes
    # return np.where(A<11,0,A)
    # OK? 9+1 bytes
    A[A<11]=0
    return A

