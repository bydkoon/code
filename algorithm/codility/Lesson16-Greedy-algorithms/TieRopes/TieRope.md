There are N ropes numbered from 0 to N − 1, whose lengths are given in an array A, lying on the floor in a line. For each I (0 ≤ I < N), the length of rope I on the line is A[I].

We say that two ropes I and I + 1 are adjacent. Two adjacent ropes can be tied together with a knot, and the length of the tied rope is the sum of lengths of both ropes. The resulting new rope can then be tied again.

For a given integer K, the goal is to tie the ropes in such a way that the number of ropes whose length is greater than or equal to K is maximal.

For example, consider K = 4 and array A such that:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 1
    A[5] = 1
    A[6] = 3
The ropes are shown in the figure below.


We can tie:

rope 1 with rope 2 to produce a rope of length A[1] + A[2] = 5;
rope 4 with rope 5 with rope 6 to produce a rope of length A[4] + A[5] + A[6] = 5.
After that, there will be three ropes whose lengths are greater than or equal to K = 4. It is not possible to produce four such ropes.

Write a function:

class Solution { public int solution(int K, int[] A); }

that, given an integer K and a non-empty array A of N integers, returns the maximum number of ropes of length greater than or equal to K that can be created.

For example, given K = 4 and array A such that:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 1
    A[5] = 1
    A[6] = 3
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
K is an integer within the range [1..1,000,000,000];
each element of array A is an integer within the range [1..1,000,000,000].

---

0에서 N − 1까지 번호가 매겨진 N개의 로프가 있고, 그 길이는 A 배열로 되어 있고 바닥에 일렬로 놓여 있습니다. 각 I(0 ≤ I < N)에 대해 줄에 있는 로프 I의 길이는 A[I]입니다.

우리는 두 개의 로프 I와 I + 1이 인접해 있다고 말합니다. 두 개의 인접한 로프를 매듭으로 묶을 수 있으며 묶인 로프의 길이는 두 로프의 길이의 합입니다. 결과로 생긴 새 로프는 다시 묶일 수 있습니다.

주어진 정수 K에 대해 목표는 길이가 K보다 크거나 같은 로프의 수가 최대가 되도록 로프를 묶는 것입니다.

예를 들어, 다음과 같은 K = 4 및 배열 A를 고려하십시오.

A[0] = 1
A[1] = 2
A[2] = 3
A[3] = 4
A[4] = 1
A[5] = 1
A[6] = 3
로프는 아래 그림과 같습니다.

우리는 묶을 수 있습니다:

길이 A[1] + A[2] = 5인 로프를 생성하기 위해 로프 1과 로프 2; 로프 4와 로프 5와 로프 6을 연결하여 길이 A[4] + A[5] + A[6] = 5의 로프를 생성합니다. 그 후, 길이가 K = 4보다 크거나 같은 3개의 로프가 있습니다. 4개의 로프를 생산하는 것은 불가능합니다.

함수 작성:

class Solution { public int solution(int K, int[] A); }

정수 K와 N 정수의 비어 있지 않은 배열 A가 주어지면 생성할 수 있는 K보다 크거나 같은 길이의 로프의 최대 수를 반환합니다.

예를 들어, 주어진 K = 4 및 배열 A는 다음과 같습니다.

A[0] = 1
A[1] = 2
A[2] = 3
A[3] = 4
A[4] = 1
A[5] = 1
A[6] = 3
함수는 위에서 설명한 대로 3을 반환해야 합니다.

다음 가정에 대한 효율적인 알고리즘을 작성하십시오.

N은 [1..100,000] 범위 내의 정수입니다. K는 [1..1,000,000,000] 범위의 정수입니다. 배열 A의 각 요소는 [1..1,000,000,000] 범위 내의 정수입니다.