
def uniao(l1, l2):
    resultado = set()
    for e in l1:
        resultado.add(e)
    for e in l2:
        resultado.add(e)
    return resultado


assert uniao([], []) == set()
assert uniao([1], []) == {1}
assert uniao([], [1]) == {1}
assert uniao([1], [1]) == {1}
assert uniao([1], [2]) == {1, 2}
assert uniao([1, 2], [1, 2]) == {1, 2}
assert uniao([1, 2, 4], [1, 2, 3]) == {1, 2, 3, 4}
