#include <iostream>
#include <vector>
using namespace std;

int gcd(int a, int b) {
    vector<int> a_v;
    vector<int> b_v;
    vector<int> c_d;

    // Collect divisors of a
    for (int i = 1; i <= a; i++) {
        if (a % i == 0) {
            a_v.push_back(i);
        }
    }

    // Collect divisors of b
    for (int j = 1; j <= b; j++) {
        if (b % j == 0) {
            b_v.push_back(j);
        }
    }

    // Find common divisors
    for (int i : a_v) {
        for (int j : b_v) {
            if (i == j) {
                c_d.push_back(i);
            }
        }
    }

    // Return the largest common divisor
    if (!c_d.empty()) {
        return c_d.back(); // Correctly access the last element
    } else {
        return 0; // Handle case when no common divisors found
    }
}

int main() {
    int result = gcd(6, 12);
    cout << "GCD of 6 and 12 is: " << result << endl;
    return 0;
}
