class Solution {
public:
    long long minOperationsToMakeMedianK(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();        
        int med = n / 2;
        long long op = 0;
        
        int i = med;
        
        while(i < n && nums[i] < k) {
            op += (k - nums[i++]);
        }
        
        i = med;
        
        while(i >= 0 && nums[i] > k) {
            op += (nums[i--] - k);
        }
        
        
        return op;
    }
};