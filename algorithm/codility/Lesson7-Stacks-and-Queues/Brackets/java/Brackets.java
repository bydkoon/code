
import java.util.Stack;

public class Brackets {
    public int solution(String S){

        Stack<Integer> stack = new Stack<>();
        
        for (char c: S.toCharArray()){
            /// charactor 문자열을 하나씩 forloop문 처리
            switch(c) {
                /// 순서에맞게 캐릭터값 조회 
                /// 소 , 중 , 대 괄호 순으로 1,2,3으로 대칭처리 
                /// [{( 은 push()   , )}]은 pop()으로 열리는 괄호는 중첩이되려는 괄호가 여부확인

                case '(': stack.push(1); 
                    break;

                case '{': stack.push(2);
                    break;
                
                case '[': stack.push(3);
                    break;
                case ']': 
                    if (stack.size() <= 0) return 0;
                    /// stack에 size가 0인경우는 stack이 없으므로 0 중첩이되지않아서 0
                    if (stack.pop() != 3) return 0;
                    /// ](대괄호) 인데 중첩된 데이터가 없으니 0 아래도 같다.
                    break;
                case '}':
                    if (stack.size() <= 0) return 0;
                    if (stack.pop() != 2) return 0;
                    break;
                case ')':
                    if (stack.size() <= 0) return 0;
                    if (stack.pop() != 1) return 0;
                    break;
            }
        }
        /// S에 문자는 있지만 중첩이 되지않는경우가 있다. 
        if (stack.size() >0 ) return 0;

        return 1;
    }
    
    
    public static void main(String[] args) {
        String S = "{[()()]}";
        
        Brackets brackets = new Brackets();
        int result = brackets.solution(S);
        System.out.println(result);
    }
}