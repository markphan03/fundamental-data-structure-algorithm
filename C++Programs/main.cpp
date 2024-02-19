#include <iostream>

void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

int GCD(int a, int b) {  // formula approach - terrible for large number due to recursive call stack.
    if (a < 0) {
        a = -a;
    }
    if (b < 0) {
        b = -b;
    }

    if (a < b) {
        swap(a, b);
    } else {
        if (b == 0) {
            return a;
        } else {
            return GCD(b, a % b);
        }
    }
}

//int GCD(int a, int b) {
//    while (b != 0) {
//
//    }
//    return a;
//}

int main() {
    std::cout << GCD(524, -148) << std::endl;
    return 0;
}

