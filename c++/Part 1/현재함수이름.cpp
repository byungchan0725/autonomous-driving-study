#include <iostream>

using namespace std; 

int addNumbers(int a, int b)
{
    cout << "Entering function " << __func__ << endl;
    return a + b;
}

int main()
{
    addNumbers(static_cast<int>(5), static_cast<int>(7));
}