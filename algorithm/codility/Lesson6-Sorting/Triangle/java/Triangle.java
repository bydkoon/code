import java.util.*;
public class Triangle {
    public int solution(int[] A){
        
        Arrays.sort(A);
        System.out.println(Arrays.toString(A));
        for (int i = 0; i < A.length-2; i++) {
            System.out.println(i);
            if(A[i] > A[i+2] - A[i+1]){
                return 1;
            }
            }

        return 0;
    }
    
    public static void main(String[] args) {
        int[] A = {-3, 1, 2, -2, 5, 6};
        Triangle triangle = new Triangle();
        int result = triangle.solution(A);
        System.out.println(result);
    }
}