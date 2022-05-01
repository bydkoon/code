import java.util.Arrays;

public class MaxProductOfThree {
    public int solution(int[] A){
        Arrays.sort(A);
        int length = A.length -1;
        int maxnum = A[length];

        int rightMax = maxnum * A[length-1] * A[length-2];
        int leftMax = maxnum * A[0] * A[1];
        
        return Math.max(rightMax, leftMax);
    }
    
    
    public static void main(String[] args) {
        int[] A = {-3, 1, 2, -2, 5, 6};
        MaxProductOfThree mpot = new MaxProductOfThree();
        int max = mpot.solution(A);
        System.out.println(max);
    }
}