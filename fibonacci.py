

def fibonacciRegular(n):
    """regular way to compute fibonacci numbers.

    Args:
        n: nth fibnacci number we want to compute.

    Returns:
        nth fibonacci number.

    """
    fcur = 0
    fnext = 1
    if n == 1:
        return fcur
    elif n == 2:
        return fnext
    else:
        for i in range(0, n-2):
            temp = fcur
            fcur = fnext
            fnext = temp + fnext
    return fnext

def fibonacciRecursive(n):
    """Recursively compute fibonacci numbers.

    Args:
        n: nth fibnacci number we want to compute.

    Returns:
        nth fibonacci number.

    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)


fib_dic = {1:0, 2:1}
def fibonacciMemorization(n):
    """Compute fibonacci numbers using memorization.

    Args:
        n: nth fibnacci number we want to compute.

    Returns:
        nth fibonacci number.

    """
    if n == 1:
        return fib_dic[1]
    elif n == 2:
        return fib_dic[2]
    else:
        if n in fib_dic:
            return fib_dic[n]
        else:
            fib_dic[n] = fibonacciMemorization(n-1)+fibonacciMemorization(n-2)
            return fibonacciMemorization(n-1) + fibonacciMemorization(n-2)
