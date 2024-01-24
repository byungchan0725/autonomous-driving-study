#include <iostream>
#include <compare> 

using namespace std;

// 정말 정말 슬프지만 나는 C++20이 아니라서 코드를 돌려보지 못한다.
// 그냥 코드만 적겠다.. ㅠ

int main() {
    int i { 11 };
    strong_ordering result { i <=> 0 };  
    if (result == storng_ordering::less) {cout << "less" << endl;};
    if (result == storng_ordering::greater) {cout << "greater" << endl;};
    if (result == storng_ordering::equal) {cout << "equal" << endl;};

    return 0;
}
