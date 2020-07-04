#include <iostream>
#include <vector>
using namespace std;

long long MaxPairwiseProduct(const vector<long long>& numbers) {
    long long max_product = 0;
    int n = numbers.size();
    int max1 = -1; 
    int max2 = -1;
    for (int first = max1+1; first < n; ++first) {
      if ((max1 == -1) || (numbers[max1]<numbers[first])){
        max1 = first;
      }
    }
    //cout << max1;
    //cout << "\n";
    for (int second = 0; second < n; ++second) {
        if (((max2 == -1) || (numbers[max2]<numbers[second])) && second != max1){
          max2 = second;
        }
    }
    //cout << max2;
    //cout << "\n";
    max_product = numbers[max1] * numbers[max2];
    return max_product;
}

int main() {
    long n;
    cin >> n;
    vector<long long> numbers(n);
    for (int i = 0; i < n; ++i) {
      cin >> numbers[i];
    }
    //for (int i = 0; i < n; ++i) {
      //cout << numbers[i];
    //}
    
    cout << MaxPairwiseProduct(numbers);
    cout << "\n";
    return 0;
}