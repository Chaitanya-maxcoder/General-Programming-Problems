# include <stdio.h>

int fac(int n);

int main()
{
    int n;
    scanf("%d", &n);
    printf("%d", fac(n));
}

int fac(int n)
{
    if (n == 1 || 0)
    {
        return 1;
    }

    else
    {
        return (n * fac(n-1));
    }
}