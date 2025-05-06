def resolve_troco(valor, dinheiro):
    troco = {
        100: 0,
        25: 0,
        10: 0,
        5: 0,
        1: 0
    }
    it = 0
    for nota, quantidade in dinheiro.items():
        while valor >= nota and quantidade > 0:
            it += 1
            troco[nota] += 1
            valor -= nota
            quantidade -= 1
    return troco, it

dinheiro = {
    100: 10000,
    25: 10000,
    10: 10000,
    5: 10000,
    1: 10000
}
valor = 234

result, it = resolve_troco(valor, dinheiro)
print(f"Troco: {result}, Iterações: {it}")