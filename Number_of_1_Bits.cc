class Solution {
public:
    int hammingWeight(uint32_t n) {
        register uint32_t a = n;
        a = (a & 0x55555555) + ((a>>1) & 0x55555555);
        a = (a & 0x33333333) + ((a>>2) & 0x33333333);
        a = (a & 0x0f0f0f0f) + ((a>>4) & 0x0f0f0f0f);
        a = (a & 0x00ff00ff) + ((a>>8) & 0x00ff00ff);
        a = (a & 0x0000ffff) + ((a>>16) & 0x0000ffff);
        return a;
    }
};
