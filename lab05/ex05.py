
def intersecao(l1, l2):
    resultado = set()
    for e in l1:
        if e in l2:
            resultado.add(e)
    return resultado


assert intersecao([], []) == set()
assert intersecao([1], []) == set()
assert intersecao([], [1]) == set()
assert intersecao([1], [1]) == {1}
assert intersecao([1], [2]) == set()
assert intersecao([1, 2], [1, 2]) == {1, 2}
assert intersecao([1, 2, 4], [1, 2, 3]) == {1, 2}
