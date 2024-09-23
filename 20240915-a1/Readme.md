# Python Programming Assignment 08

### **Instructions:**

Implement a Python program using **Google Colab** to accomplish the following task.

---

## **Water Bucket Puzzle**

### **Problem Statement:**

In this puzzle game, you must use three buckets (three-liter, five-liter, and eight-liter buckets) to collect exactly four liters of water in one of the buckets. Buckets can only be emptied, completely filled, or poured into another bucket. For example, you can fill the five-liter bucket and then pour its contents into the three-liter bucket, leaving you with a full three-liter bucket and two liters of water in the five-liter bucket.

With some effort, you should be able to solve the puzzle. But can you figure out how to solve it with the minimal number of moves?

---

### **The Program in Action:**

Water Bucket Puzzle, by Hassan Ali Khan h.a.khan1992@gmail.com

Try to get 4L of water into one of these buckets:

<pre>
8|      |
7|      |
6|      |
5|      |        5|      |
4|      |        4|      |
3|      |        3|      |        3|      |
2|      |        2|      |        2|      |
1|      |        1|      |        1|      |
 +------+         +------+         +------+
    8L               5L               3L

 You can:
  (F)ill the bucket
  (E)mpty the bucket
  (P)our one bucket into another
  (Q)uit
> f

Select a bucket 8, 5, 3, or QUIT:
> 5  

Try to get 4L of water into one of these buckets:

8|      |
7|      |
6|      |
5|      |        5|WWWWWW|
4|      |        4|WWWWWW|
3|      |        3|WWWWWW|        3|      |
2|      |        2|WWWWWW|        2|      |
1|      |        1|WWWWWW|        1|      |
 +------+         +------+         +------+
    8L               5L               3L
<pre>