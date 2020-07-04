#include <iostream>

int gcd_naive(int a, int b) {
  if (a >= b){
    int c = a % b;
    if (c==0){
      return b;
    }
    else {
      return gcd_naive(b,c);
    }
  }
  else{
    int d = a;
    a = b;
    b = d;
    return gcd_naive(a,b);
  }
}



//  int current_gcd = 1;
//  for (int d = 2; d <= a && d <= b; d++) {
//    if (a % d == 0 && b % d == 0) {
//      if (d > current_gcd) {
//        current_gcd = d;
//      }
//   }
//  }
//  return current_gcd;
//}

int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << gcd_naive(a, b) << std::endl;
  return 0;
}