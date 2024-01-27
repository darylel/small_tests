from functools import cache

@cache
def fib(n: int) -> int:
    '''
    Using the @cache decorator memoizes the function
    '''
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def main():
    for i in range(0, 100):
        print(f'{i}: {fib(i)}')

if __name__ == '__main__':
    main()