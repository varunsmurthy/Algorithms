def factorial_iterative(n):
    fact_val = 1

    for i in range(1,n+1):
        fact_val = fact_val*i

    return (fact_val)


def factorial_recursive(n):
    if(n<=1):
        return(1)
    else:
        return(n*factorial_recursive(n-1))


def main():
    n = 5;
    fact_val_iterative = factorial_iterative(n)
    fact_val_recursive = factorial_recursive(n)

    print("factorial of ",str(n)," computed iteratively = ",str(fact_val_iterative))
    print("factorial of ", str(n), " computed recursively = ", str(fact_val_recursive))


if __name__ == "__main__":
    main()