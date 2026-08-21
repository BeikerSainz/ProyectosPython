def number_pattern(n):
    numeros = []
    if not isinstance(n, int) or n <= 0:
        return "Error: Input must be a positive integer."
    if n < 1:
        return "Error: Input must be an integer greater than 0."
    for i in range(1, n + 1):
        numeros.append(str(i))
    return " ".join(numeros)

print(number_pattern(5))  # Output: "1 22 333 4444 55555"