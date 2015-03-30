#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        vector<int> res;
        unordered_map<int, int> target_map;
        for (int i=0; i<numbers.size(); i++)
        {
          if (target_map.count(numbers[i]))
          {
            res.push_back(((target_map[numbers[i]]<i) ? target_map[numbers[i]] : i) + 1); 
            res.push_back(((target_map[numbers[i]]>i) ? target_map[numbers[i]] : i) +1 ); 
            return res;
          }
          else 
          {
            target_map[target - numbers[i]] = i;
          }
        }
    }
};

int main() {
  Solution sol; 
  //int arr[] = {2,7,11,15,14};
  //vector<int>* in_list(arr);
  vector<int> in_list = {-20, -30, 5, 90, 3, 2}; // {2,7,11,15};
  vector<int> res;
  int in_target;
  //cout << "Please enter a list of numbers, e.g. {2, 7, 11, 15}:" <<endl;
  //cin >> in_list;
  //*in_list = {2, 7, 11, 15};
  in_target = 7;
  //cout << "Please enter a target sum number:" <<endl;
  //cin >> in_target;
  cout<<"indices for a pair of numbers in list that sums to target:" <<endl;
  res = sol.twoSum(in_list, in_target);
  cout << res[0] << ", "<< res[1] << endl;
  return 0;
}

