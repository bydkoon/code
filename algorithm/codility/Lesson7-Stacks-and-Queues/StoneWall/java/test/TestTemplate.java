import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class TestTemplate {
    @Test
    public void solution(int[] A){
        StoneWall stoneWall = new StoneWall();
        int result = stoneWall.solution();
        int answer = 0;
        assertEquals(answer, result);
    }
    
    
}