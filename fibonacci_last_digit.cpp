#include <iostream>
int get_fibonacci_last_digit_naive(int n) {
    if (n <= 1)
        return n;

    int a = 0;
    int b = 1;

    for (int i = 0; i < n - 1; ++i) {
      int c = a%10 + b%10;
      a = b%10;
      b = c%10;
        //int tmp_previous = previous%10;
        //previous = current%10;
        //current = tmp_previous + current;
    }

    return b;
}

int main() {
    int n;
    std::cin >> n;
    int c = get_fibonacci_last_digit_naive(n);
    std::cout << c << '\n';
    }