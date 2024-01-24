#include <iostream>
#include <compare>

using namespace std; 

// 이것또한 코드로만 남긴다. 

int main()
{
    int i { 11 };
    strong_orderning result { i <=> 0 };
    if (is_lt(result)) { cout << "less" << endl;};
    if (is_gt(result)) { cout << "less" << endl;};
    if (is_eq(result)) { cout << "less" << endl;};
}