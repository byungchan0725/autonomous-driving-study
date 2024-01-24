#include <iostream>

// employee.cppm 파일을 사용하려고 하였으나 계속 에러가 나서 구조체 직접 정의
struct Employee {
    char firstInitial;
    char lastInitial;
    int employeeNumber;
    int salary;
}; 

int main() {
    // 직원 레코드 생성 및 값 채우기 
    Employee anEmployee; 
    anEmployee.firstInitial = 'K';
    anEmployee.lastInitial = 'B';
    anEmployee.employeeNumber = 7; 
    anEmployee.salary = 80000; 

    // 직원 레코드 값 출력 
    std::cout << "First Initial: " << anEmployee.firstInitial << std::endl;
    std::cout << "Last Initial: " << anEmployee.lastInitial << std::endl;
    std::cout << "Employee Number: " << anEmployee.employeeNumber << std::endl;
    std::cout << "Salary: " << anEmployee.salary << std::endl;
}