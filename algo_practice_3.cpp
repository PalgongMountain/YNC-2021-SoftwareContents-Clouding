#include <stdio.h>

int main(void)
{
	int X = 1, cnt = 0, sum = 0;

	while (sum <= 500)
	{
		X += 2;
		sum += X;
		cnt++;
	}

	printf("%d %d", X, cnt);
}