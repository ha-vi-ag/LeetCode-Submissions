class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int ans = 1;
        
        for(int i = 1, j = 0; i < nums.size(); i++) {
            if(nums[i] > nums[i-1]) ans = max(ans, (i - j + 1));
            else j = i;
        }
        
        for(int i = 1, j = 0; i < nums.size(); i++) {
            if(nums[i] < nums[i-1]) ans = max(ans, (i - j + 1));
            else j = i;
        }
        
        return ans;
    }
};