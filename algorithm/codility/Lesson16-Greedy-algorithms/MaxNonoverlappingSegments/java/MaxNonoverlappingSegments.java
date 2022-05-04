
class MaxNonoverlappingSegments {
    public int solution(int[] A, int[] B){

        int end = B[0];
        int segment = 1;
        if (A.length <= 1){
            return A.length;
        }
        
        for (int i = 1; i < A.length; i++) {
            if(A[i] > end){
                segment++;
                end = B[i];


                
            }
            
        }


        return segment;
    }
    
    public static void main(String[] args) {

        int[] A = {1,3,7,9,9};
        int[] B = {5,6,8,9,10};

        MaxNonoverlappingSegments maxNonoverlappingSegments = new MaxNonoverlappingSegments();
        maxNonoverlappingSegments.solution(A,B);

    }
}