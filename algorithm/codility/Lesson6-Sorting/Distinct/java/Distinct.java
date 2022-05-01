
import java.util.Arrays;

public class Distinct {
    public int solution(int[] A){
        System.out.println(Arrays.toString(A));
        Arrays.sort(A);
        int count = 0;

        System.out.println(Arrays.toString(A));
        int N = A.length;

        if (N == 0) {
            return 0;
        }
        for (int i = 1; i < N; i++) {
            if (A[i]-1 != A[i]) {
                count += 1;
                
            }
        }
        return count;
        
    }


    public static void main(String[] args) {
    
        int[] A = {2,1,1,2,3,1};
        Distinct dis = new Distinct();
        int count = dis.solution(A);
        System.out.println(count);
        }
}

