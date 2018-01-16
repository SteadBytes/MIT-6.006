# Models of Computation
* Operations an algorithm is allowed
* Cost of each operation

Mathematical analog of a computer.
* Algorithm is mathematical analog of a program

## Random Access Machine
* Random Access Memory (RAM) modeled by a large array:
```
 +---+
0|   |
 +---+
1|   |
 +---+
2|   |
 +---+
3|   | <-- word
 +---+
```
* **word** = *m* bits
    * *m* >= log(size of memory) -> should be able to specify an index into the RAM array
* **O(1)** time to: 
    * Load O(1) words
    * Do O(1) computations
    * Store O(1) words
* O(1) registers

## Pointer Machine
More abstract, simpler way of thinking about computation - very simple model of OOP
* Dynamically allocated objects
* Object has O(1) **fields**
* **Field** = a word (i.e int) or a **pointer** to and object or null (or None)

## Python Model
Copmutational models implemented in python -> see lecture notes pdf.