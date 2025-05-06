def sdm(s, f, n):
    intervals = sorted(zip(s, f), key=lambda x: x[1])
    selected_intervals = []
    last_end_time = -float('inf')
    it = 0

    for start, end in intervals:
        it += 1
        if start > last_end_time:
            selected_intervals.append((start, end))
            last_end_time = end

    return selected_intervals, it

s = [4, 6, 13, 4, 2, 6, 7, 9, 1, 3, 9]
f = [8, 7, 14, 5, 4, 9, 10, 11, 6, 13, 12]
n = len(s)
result, it = sdm(s, f, n)
print(f"Resultado: {result}, Iterações: {it}")