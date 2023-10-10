
def diferenca(l1, l2):
    resultado = set()
    for e in l1:
        if e not in l2:
            resultado.add(e)
    return resultado


assert diferenca([], []) == set()
assert diferenca([1], []) == {1}
assert diferenca([], [1]) == set()
assert diferenca([1], [1]) == set()
assert diferenca([1], [2]) == {1}
assert diferenca([1, 2], [1, 2]) == set()
assert diferenca([1, 2, 4], [1, 2, 3]) == {4}
