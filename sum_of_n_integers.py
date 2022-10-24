import numpy as np



def sum_of_n_integers_pure_python(n):
    res = 0
    for i in range(1, n + 1):
        res += i
    return res


def sum_of_n_integers_smart_python(n):
    return sum(
            [i for i in range(1, n + 1)]
    )



def main():
    res1 = sum_of_n_integers_pure_python(n=100)
    res2 = sum_of_n_integers_smart_python(n=100)

    print(f"res1 = {res1}")
    print(f"res2 = {res2}")



if __name__ == "__main__":
    main()
