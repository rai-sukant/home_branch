#include <iostream> // Standard input-output stream objects
#include <vector>   // Standard vector container
using namespace std ; 



int gcd(int a, int b ) {

    vector <int> a_v ;
    vector <int> b_v ;
    vector <int> c_d ;



    for (int i = 0, i <= a; i++ ){

        if (a % i == 0) {

            a_v.push_back(i) ;


        }
    }
    for (int j = 0, j <= b; i++ ){ 

        b_v.push_back(j) ;
    }

    for (int i : a_v ){
        for (int j : b_v ){

            if ( i==j ) {

                c_d.push_back(i);

            }
        }

    }

    return (c_d[-1]);



}



int main () {


}