#include <iostream>
#include <vector>
using namespace std;

int MaxPairwiseProduct(const vector<int>& numbers) {
    int max_product = 0;
    int n = numbers.size();

    for (int first = 0; first < n; ++first) {
        for (int second = first + 1; second < n; ++second) {
            if (max_product > numbers[first] * numbers[second]){
            max_product = numbers[first] * numbers[second];
            }
        }
    }
    return max_product;
}

int main() {
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }
    cout << MaxPairwiseProduct(numbers);
    cout << "\n";
    return 0;
}