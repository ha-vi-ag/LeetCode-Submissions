class Solution {
public:
    long long kSum(vector<int>& nums, int k) {
        long long total = 0;
        for(int &i: nums) {
            if(i >= 0) total += i;
            i = abs(i);
        }
        int n = nums.size();
        sort(nums.begin(), nums.end());
        priority_queue<pair<long long,int>> pq;
        pq.push({-nums[0], 0});
        k -= 1;
        long long last = 0;
        while(k >= 1) {
            auto cur = pq.top();
            pq.pop();
            last = -cur.first;
            k--;
            int ind = cur.second;
            if(ind + 1 < n){
                pq.push({-(-cur.first + nums[ind + 1]), ind + 1});
                pq.push({-(nums[ind + 1] + last - nums[ind]),ind+1});
            }
        }
        
        return total - last;
    }
};