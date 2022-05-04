Located on a line are N segments, numbered from 0 to N − 1, whose positions are given in arrays A and B. For each I (0 ≤ I < N) the position of segment I is from A[I] to B[I] (inclusive). The segments are sorted by their ends, which means that B[K] ≤ B[K + 1] for K such that 0 ≤ K < N − 1.

Two segments I and J, such that I ≠ J, are overlapping if they share at least one common point. In other words, A[I] ≤ A[J] ≤ B[I] or A[J] ≤ A[I] ≤ B[J].

We say that the set of segments is non-overlapping if it contains no two overlapping segments. The goal is to find the size of a non-overlapping set containing the maximal number of segments.

For example, consider arrays A, B such that:

    A[0] = 1    B[0] = 5
    A[1] = 3    B[1] = 6
    A[2] = 7    B[2] = 8
    A[3] = 9    B[3] = 9
    A[4] = 9    B[4] = 10
The segments are shown in the figure below.



The size of a non-overlapping set containing a maximal number of segments is 3. For example, possible sets are {0, 2, 3}, {0, 2, 4}, {1, 2, 3} or {1, 2, 4}. There is no non-overlapping set with four segments.

Write a function:

class Solution { public int solution(int[] A, int[] B); }

that, given two arrays A and B consisting of N integers, returns the size of a non-overlapping set containing a maximal number of segments.

For example, given arrays A, B shown above, the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..30,000];
each element of arrays A and B is an integer within the range [0..1,000,000,000];
A[I] ≤ B[I], for each I (0 ≤ I < N);
B[K] ≤ B[K + 1], for each K (0 ≤ K < N − 1).

---

 라인에 위치한 N개의 세그먼트는 0에서 N − 1까지 번호가 매겨져 있으며 배열 A와 B에 위치가 지정되어 있습니다. 각 I(0 ≤ I < N)에 대해 세그먼트 I의 위치는 A[I]에서 B[I] (포함). 세그먼트는 끝을 기준으로 정렬됩니다. 즉, 0 ≤ K < N − 1이 되도록 K에 대해 B[K] ≤ B[K + 1]입니다.

I ≠ J와 같은 두 개의 세그먼트 I 및 J는 적어도 하나의 공통점을 공유하는 경우 겹칩니다. 즉, A[I] ≤ A[J] ≤ B[I] 또는 A[J] ≤ A[I] ≤ B[J]입니다.

두 개의 겹치는 세그먼트가 포함되어 있지 않으면 세그먼트 집합이 겹치지 않는다고 말합니다. 목표는 최대 세그먼트 수를 포함하는 겹치지 않는 집합의 크기를 찾는 것입니다.

예를 들어, 다음과 같은 배열 A, B를 고려하십시오.
```
A[0] = 1 B[0] = 5
A[1] = 3 B[1] = 6
A[2] = 7 B[2] = 8
A[3] = 9 B[3] = 9
A[4] = 9 B[4] = 10
```

세그먼트는 아래 그림에 나와 있습니다.

최대 세그먼트 수를 포함하는 겹치지 않는 집합의 크기는 3입니다. 예를 들어 가능한 집합은 {0, 2, 3}, {0, 2, 4}, {1, 2, 3} 또는 {1, 2, 4}. 4개의 세그먼트가 있는 비중첩 세트가 없습니다.

함수 작성:

클래스 솔루션 { 공개 int 솔루션(int[] A, int[] B); }

N개의 정수로 구성된 두 개의 배열 A와 B가 주어지면 최대 세그먼트 수를 포함하는 겹치지 않는 집합의 크기를 반환합니다.

예를 들어, 위에 표시된 배열 A, B가 주어지면 함수는 위에서 설명한 대로 3을 반환해야 합니다.

다음 가정에 대한 효율적인 알고리즘을 작성하십시오.

N은 [0..30,000] 범위 내의 정수입니다. 배열 A와 B의 각 요소는 [0..1,000,000,000] 범위 내의 정수입니다. A[I] ≤ B[I], 각 I에 대해 (0 ≤ I < N); B[K] ≤ B[K + 1], 각 K에 대해(0 ≤ K < N − 1).