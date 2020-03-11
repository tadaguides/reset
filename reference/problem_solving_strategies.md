# Problem Solving Strategies



## Arrays

* Matrix rotation to the right 90 degrees == transpose THEN reverse rows
    * [[1,2,3],[4,5,6],[7,8,9]]^T => [[1,4,7],[2,5,8],[3,6,9]] => [[7,4,1],[8,5,2],[9,6,3]]
* Reverse a string: strName[::-1]
    * The slice statement means start at string length, end at position 0, move with the step -1 (or one step backward).
    * strName[::-1] == strName[len(strName):0:-1]

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

## Python Data Structure Tips
* Queue.Queue and collections.deque serve different purposes. 
  * Queue.Queue is intended for allowing different threads to communicate using queued messages/data, whereas collections.deque is simply intended as a datastructure. That's why Queue.Queue has methods like put_nowait(), get_nowait(), and join(), whereas collections.deque doesn't. Queue.Queue isn't intended to be used as a collection, which is why it lacks the likes of the in operator.
  * It boils down to this: if you have multiple threads and you want them to be able to communicate without the need for locks, you're looking for Queue.Queue; if you just want a queue or a double-ended queue as a data structure, use collections.deque.
  * Finally, accessing and manipulating the internal deque of a Queue.Queue is playing with fire - you really don't want to be doing that.
  * If you look at the source of Queue.Queue, it uses deque under the hood. collections.deque is a collection, while Queue.Queue is a communications mechanism. The overhead in Queue.Queue is to make it threadsafe. Using deque for communicating between threads will only lead to painful races. Whenever deque happens to be threadsafe, that's a happy accident of how the interpreter is implemented, and not something to be relied upon. That's why Queue.Queue exists in the first place.

---


## Systems Design
* https://leetcode.com/discuss/general-discussion/531253/people-who-take-system-design-interviews-what-exactly-are-you-looking-for
* https://www.hiredintech.com/courses/system-design
