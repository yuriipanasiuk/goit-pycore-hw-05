def caching_fibonacci():
    # Create an empty dictionary to store (cache) previously computed Fibonacci numbers
    cache = {}

    def fibonacci(n):
        # Base case: if n <= 0, the Fibonacci number is 0
        if n <= 0:
            return 0
        # Base case: if n == 1, the Fibonacci number is 1
        elif n == 1:
            return 1
        # If the value is already in the cache, return it immediately
        if n in cache:
            return cache[n]
        # Otherwise, compute it recursively and store the result in the cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        # Return the computed and cached value
        return cache[n]
    # Return the fibonacci function itself, with the cache preserved inside its closure
    return fibonacci

fib = caching_fibonacci()
        