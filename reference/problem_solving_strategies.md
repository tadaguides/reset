# Problem Solving Strategies



## Arrays
* Matrix rotation to the right 90 degrees == transpose THEN reverse rows
    * [[1,2,3],[4,5,6],[7,8,9]]^T => [[1,4,7],[2,5,8],[3,6,9]] => [[7,4,1],[8,5,2],[9,6,3]]
* Reverse a string: strName[::-1]
    * The slice statement means start at string length, end at position 0, move with the step -1 (or one step backward).

## Linked Lists
* Dummy note trick: A dummy node is a node in the list which has no value associated with it; they are usually located at the start and/or end of the list. The reason for using dummy nodes is that it makes certain list algorithms easier to implement by removing the need to have special cases for dealing with the first/last elements or with empty lists; this is because they ensure that there will always be at least at least one node.
* Reversing a singly-linked list (iterative): keep pointers to previous node, current node, and next node => keep shifting to the right and swap direction until current node is None

## String

## Two Pointer Techniques
* Two pointer technique: https://leetcode.com/articles/two-pointer-technique/
* Tortoise and Hare algorithm (for cycle detection): https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare

## Sliding Window Techniques
{TODO} fill out this section


## Recursion Techniques
{TODO} fill out this section

## Divide and Conquer Techniques
{TODO} fill out this section

## Backtracking Techniques
{TODO} fill out this section

## Misc Tips
* 32-bit signed integer range: [−(2^31),  (2^31) − 1]

## Python Tips
* string.isdigit() => returns whether all characters in a string are digits
# string.isalnum() => returns whether all characters in a string is alphanumeric

---


## Systems Design
* https://leetcode.com/discuss/general-discussion/531253/people-who-take-system-design-interviews-what-exactly-are-you-looking-for
* https://www.hiredintech.com/courses/system-design
