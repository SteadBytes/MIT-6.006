# Insertion and Merge Sort

## Sorting Motivation
* Find median of array
    * Item at index *n/2*
* Searching for specific item
    * Unsorted = O(n) time -> search through each item in array
    * Sorted =  **Binary Search** = O(log*n*)
* Data compression
    * Sort items to find duplicates -> compress by storing one of each item along with the number of duplicates
* Computer graphics
    * Sorted lists of objects from front-> back (vice versa) in image

## Insertion Sort
Builds sorted array **one item at a time**. Building a subarray which itself *at any point* is sorted.

The *sorted subarray* start from index 0 - only one item in the array therefore it is sorted. Each item in the unsorted portion is then inserted **in turn** into the correct position within the sorted sub array -> **pairwise swaps**.

```
Step 1 − If it is the first element, it is already sorted. return 1;
Step 2 − Pick next element
Step 3 − Compare with all elements in the sorted sub-list
Step 4 − Shift all the elements in the sorted sub-list that is greater than the 
         value to be sorted
Step 5 − Insert the value
Step 6 − Repeat until list is sorted

```
```
For i = 1,2...n
    insert A[i] into sorted array A[0:i-1]
    by pairwise swaps down to the correct position
```

### Analysis
* &theta;(n<sup>2</sup>)
    * &theta;(n) steps
    * Each step could have up to n compares and swaps needed (&theta;(n) swaps)
        * Assume either compare or swap is more complex

If compare is **more** complex than swap:
* Replace **pairwise swaps** with binary search
* Do binary search on A[0:i-1] (already sorted) to find position of item *i* to insert
    * &theta;(logi) time, &theta;(nlogn) compares
    * Swaps are still &theta;(n<sup>2</sup>)
        * Still need to insert item in to A[0:i-1], might need to shift n values

## Merge Sort
Split the list into two halves, recursively sort each half and then *merge* the two sorted sublists.

Subproblem -> sorting the *subarray* starting at index *p* through to index *r*.
* Subarray = `array[p..r]`

For an array of *n* elements the problem is to sort `array[0..n-1]`

Divide and Conquer:
1. **Divide** by finding the midway position *q* between *p* and *r*.
2. **Conquer** by recursively sorting the subarrays in each subproblem.
    * Sort `array[p..q]` and `array[q+1..r]`
3. **Combine** by merging the two sorted subarrays back into the single sorted subarray `array[p..r]`

**Base Case** = subarray with **< 2** elements
* When *p>=r*

* &theta;(nlogn)
### Merge
* Two sorted arrays as input -> the **invariant** for merge
* Two pointers -> one for each array
* Compare element at each pointer, add smallest to merged array
* If all elements from one array added to merged, just add all remaining from other array to merged.
* &theta;(n) complexity for two arrays of size *n/2*
```
* = pointer
A_merged = []

A1 = [20, 13, 7, *2]
A2 = [12, 11, 9, *1]

Compare: min(2,1) = 1
A_merged = [1]

A1 = [20, 13, 7, *2]
A2 = [12, 11, *9]

Compare: min(2,9) = 2
A_merged = [1,2]

A1 = [20, 13, *7]
A2 = [12, 11, *9]

Compare: min(7,9) = 7
A_merged = [1,2,7]

A1 = [20, *13]
A2 = [12, 11, *9]

Compare: min(13,9) = 9
A_merged = [1,2,7,9]

A1 = [20, *13]
A2 = [12, *11]

Compare: min(13,11) = 11
A_merged = [1,2,7,9,11]

A1 = [20, *13]
A2 = [*12]

Compare: min(13,12) = 12
A_merged = [1,2,7,9,11,12]

A1 = [20, *13]
A2 = []

A2 is empty -> add remaining elements from A1
A_merged = [1,2,7,9,11,12,13,20]
```
### Complexity Proof
* T(n) = C<sub>1</sub> + 2T(n/2) + cn
    * Divide + recursion + merge
    * c = constant factor
Recursion:
```
cn = cn
    -> cn/2 + cn/2 = cn
        -> cn/4 + cn/4 + cn/4 + cn/4 = cn
            -> ...
                -> n leaves
```
Each step has same amount of work being done: cn

1 + logn levels (split in half each time)

Therefore: T(N) = (1+logn)*cn = &theta;(nlogn)

## Insertion vs Merge sort
* Insertion sort is **in-place** sorting: requires &theta;(1) auxillary space
* Merge sort not in-place: requires &theta;(n) auxillary space


Run time examples show constant factors quickly get overwhelmed as *n* increases: 
* Merge sort in python = 2.2nlg(n) microseconds
* Insertion sort in python = 0.2n<sup>2</sup> microseconds
* Insertion sort in C = 0.01n<sup>2</sup>