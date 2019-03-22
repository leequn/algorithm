
# coding: utf-8

# In[54]:


#给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#示例:
#给定 nums = [2, 7, 11, 15], target = 9
#因为 nums[0] + nums[1] = 2 + 7 = 9
#所以返回 [0, 1]


# In[90]:


nums = [2, 7, 11, 15,4,5,3,6,1,8]
target = 9


# In[91]:


#我自己的答案，给出所有的target=9的组合
def twoSum_0(nums,target):
    result = {}
    for i in range(len(nums)):            
        if target - nums[i] in nums:
            result[i]=str(nums.index(nums[i]))+ str(nums.index(target -nums[i]))
    return result


# In[92]:


twoSum_0(nums,target)


# In[93]:


#参考答案1
def twoSum_1(nums,target):
    num_pos = dict()
    for index, num in enumerate(nums):
        result = target - num
        if result in num_pos.keys():
            return [ num_pos[result], index]
        num_pos[num] = index
    return None


# In[94]:


twoSum_1(nums,target)


# In[96]:


#参考答案2
def twoSum_2(nums,target):
    num_to_index = {}
    for i,num in enumerate(nums):
        if target-num in num_to_index:
            return [i,num_to_index[target-num]]
        num_to_index[num] = i
    return []


# In[97]:


twoSum_2(nums,target)

