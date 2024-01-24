#include <iostream>
#include <vector>

using namespace std;

int main()
{
    std::vector<int> myVector { 11, 22 };

    myVector.push_back(33); 
    myVector.push_back(44);  

    cout << "1st elem : " << myVector[0] << endl;
}