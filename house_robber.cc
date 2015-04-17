class Solution {
public:
    int rob(vector<int> &num) {
        vector<int> dp(num.size()+1, 0);
        if (num.size() > 0)
            dp[1] = num[0];
        for (int i = 2; i < dp.size(); i++) {
            dp[i] = std::max (dp[i-1], dp[i-2] + num[i-1]);
        }
        return dp[num.size()];
    }
};


