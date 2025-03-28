# 560. 和为 K 的子数组
# 提示
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

# 子数组是数组中元素的连续非空序列。

 

# 示例 1：

# 输入：nums = [1,1,1], k = 2
# 输出：2
# 示例 2：

# 输入：nums = [1,2,3], k = 3
# 输出：2

import collections

def subarraySum(nums, k):
    ans = s = 0
    cnt = collections.defaultdict(int)
    cnt[0] = 1
    for x in nums:
        s += x
        ans += cnt[s-k]
        cnt[s] += 1
    return ans


print(subarraySum([1,1,1],2))
print(subarraySum([1,2,3],3))