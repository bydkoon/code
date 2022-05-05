import java.util.Stack;

public class Nesting {
    public int solution(String S) {
        if (S.length() <= 1) return 0;
 
         Stack<Integer> stack = new Stack<>();
         for (char c: S.toCharArray()) {
             switch(c) {
                 case '(': 
                     stack.push(1);
                         break;
                     
                 case ')':
                     if (stack.size() >= 1) stack.pop(); 
                     else stack.push(1);
                         break;
             }
         }
         
         if (stack.size() < 1) return 1;
     
         return 0;
     }
    
    public static void main(String[] args) {
        String S = "())" ;
        Nesting nesting = new Nesting();
        int result = nesting.solution(S);
        System.out.println(result);
    }
}
