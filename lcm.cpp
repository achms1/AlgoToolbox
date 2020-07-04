#include <iostream>
long long lcm_naive(long a, long b, long p) {
  long j = p;
  long x = a;
  long y = b;
  if (x >= y){
    int z = x % y;
    if (z==0){
      return j/y;
    }
    else {
      return lcm_naive(y,z,p);
    }
  }
  else{
    int q = x;
    x = y;
    y = q;
    return lcm_naive(x,y,p);
  }
}
int main() {
  long a, b;
  std::cin >> a >> b;
  long p = a * b;
  std::cout << lcm_naive(a, b, p) << std::endl;
  return 0;
}