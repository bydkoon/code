
public class TieRopes {
    public int solution(int K, int[] A){
        
        int count = 0;
        int sumA = 0;
        for (int i = 0; i < A.length; i++) {
            sumA += A[i];
            if(sumA >= K){
                count++;
                sumA = 0;
            }


        }
        return count;

    }
    
    public static void main(String[] args) {
        int K = 4;
        int[] A = {1,2,3,4,1,1,3};
        TieRopes tieRopes = new TieRopes();
        int count = tieRopes.solution(K, A);
        System.out.println(count);
    }
}