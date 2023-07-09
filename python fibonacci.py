def generate_fibonacci(limit):
    fibonacci_seq = [0, 1]  
    while fibonacci_seq[-1] + fibonacci_seq[-2] <= limit:
        next_num = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(next_num)

    return fibonacci_seq



limit = 100
fibonacci_numbers = generate_fibonacci(limit)


for number in fibonacci_numbers:
    print(number)
