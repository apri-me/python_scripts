def fib_gen(n):
    a, b = 0, 1
    yield a
    yield b
    for i in range(n - 2):
        yield a + b
        a, b = b, a + b

def fib(n):
    return ([i for i in fib_gen(10)])
