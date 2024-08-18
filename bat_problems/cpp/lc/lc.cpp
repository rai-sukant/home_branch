#include <iostream>
using namespace std ;
#include <stack>
#include <vector>


/* prices[i] -> price of ith element 
   prices[j] -> discount for element in prices[i]

   ( all that such that j is minimum index such that j > i  , prices[j] <= prices[i], else no discount )
    
*/

stack<int> finalPrices(vector<int>& prices) {

        stack <int> stack ;
        vector <int> answer ;

        



    }


int main () {

    std::vector<int> prices = {8, 4, 6, 2, 3};
    finalPrices ( prices );

    return 0 ;
}