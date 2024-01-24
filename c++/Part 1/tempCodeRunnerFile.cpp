#include <iostream>

[[nodiscard]] int func()
{
	return 42;
}

int main()
{
	int result = func();

    return 0;
}