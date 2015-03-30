// Return true if palindrome number
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        vector<int> list;
        bool is_Palindrome;
        if(x<0) 
        {
            is_Palindrome = false;
        }
        else 
        {
            is_Palindrome = true;
        }
        while(x/10 >= 1)
        {
            list.push_back(x%10);
            x = x/10;
        }
        list.push_back(x%10);
        for (int i=0; i<list.size()/2+1; i++)
        {
            //cout << "digit "<<i<<" is "<< list[i] << ", digit "<<list.size()-i-1<<" is "<< list[list.size()-i-1] << endl;
            if(list[i] == list[list.size()-i-1])
            {
                continue;
            }
            else
            {
                is_Palindrome = false;
                break;
            }
        }
    return is_Palindrome;
    }
};

int main() {
    Solution sol;
    int input;
    cout << "Please enter a number" <<endl;
    cin>>input;
    cout<<"1 for palindrome number" <<endl;
    std::cout << sol.isPalindrome(input) << std::endl;
    return 0;
}

