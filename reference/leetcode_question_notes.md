# Leetcode Question Notes

## Leetcode solutions
https://github.com/wuduhren/leetcode-python/blob/master/README.md

## Arrays

* Remove Duplicates from Sorted Array: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
  * keep 2 pointers, one trailing, one leading => when leading pointer finds a new value, set this value to index of trailing pointer.

* Best Time to Buy and Sell Stock II: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
  * keep 2 pointers, when leading pointer value > trailing pointer value, add to profit.

* Rotate Array: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
  * notice how rotating an array is simply: reversing the entire array => reverse elements from 0->K-1 => reverse elements from K->len(nums)-1.

* Contains Duplicate: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
  * use set to track seen items, return True if seen

* Single Number: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
  * notice that 2*sum(set(nums)) - sum(nums) = single_number

* Intersection of Two Arrays II: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
  * keep 2 pointers, sort both arrays => if both values are current index in both arrays are equal, add value to rtn, else increment whichever counter corresponds to the smaller value at that index
  * if one array is much smaller, store frequency of each value in a dictionary for smaller array, then iterate through larger array => when a value is found in dict, decrement counter (until 0) and add value to rtn

* Product of array except self: https://leetcode.com/problems/product-of-array-except-self/
  * Scan array once forward, tracking the product of all elements before i in output => scan array in reverse, multiplying the product of all elements after i in output

