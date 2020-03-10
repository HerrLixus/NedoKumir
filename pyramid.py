n = int(input("введите число: "))
print(("*".center(2*n+1)+"\n"+'\n'.join([''.join(["*", ' ' * (2*i - 1), "*"]).center(2*n+1,) for i in range(1, n)])))
