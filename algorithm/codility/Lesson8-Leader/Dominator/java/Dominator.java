import java.util.Arrays;

class Dominator {
    public void solution(int[] A){
        Arrays.sort(A);
        
    }
    
    public static void main(String[] args) {

        int[] A = {3,4,3,2,3,-1,3,3};

        Dominator dominator = new Dominator();
        int result = dominator.solution(A);        
        System.out.println(result);
    }
}