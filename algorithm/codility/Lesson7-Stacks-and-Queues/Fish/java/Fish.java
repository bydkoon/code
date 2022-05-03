import java.util.Stack;

class Fish {
    public int solution(int[] A, int[] B){
        
        int count = 0;
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < A.length; i++) {
            int fish = A[i];

            if (B[i] == 0){
                if (stack.isEmpty()){
                    count++;

                }else if(stack.peek() < fish){
                    stack.pop();
                    i--;
                }
                
            }else{
                stack.push(fish);
            }
        }
        return count+ stack.size();
    }
    
    public static void main(String[] args) {

        int[] A = {4,3,2,1,5};
        int[] B = {0,1,0,0,0};

        Fish fish = new Fish();
        int count = fish.solution(A, B);

        System.out.println(count);
    }
}