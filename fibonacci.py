def fibonacci(num):

    seq = [0, 1]
    while seq[-1] < num:
        seq.append(seq[-1] + seq[-2])
    if num in seq:
        print(f"{num} pertence à sequência de Fibonacci!")
    else:
        print(f"{num} não pertence à sequência de Fibonacci.")
    return seq


fibonacci(21)




