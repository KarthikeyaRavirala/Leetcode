# Two Sum

## Description

This repository contains a solution for the "Two Sum" problem on LeetCode. The problem involves finding two numbers in an array that add up to a given target. The solution is implemented in Python and utilizes the concepts of arrays and hash tables.

## Problem Statement

Given an array of integers `nums` and an integer `target`, the task is to return the indices of two numbers in the array such that they add up to the target. It is assumed that each input has exactly one solution, and the same element cannot be used twice.

### Example

#### Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, the function returns [0, 1].
```
#### Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
#### Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Constraints

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9

## Algorithm Efficiency

The solution provided in the code is designed to have a time complexity of less than O(n^2). It utilizes hash tables to optimize the process of finding the complementary element efficiently.

## How to Use

To use the solution, follow these steps:

1. Clone the repository to your local machine: 
```
python Two Sum.py
```
## Code Sample
```
python Runtime.py
```

## Contributers
- Karthikeya

