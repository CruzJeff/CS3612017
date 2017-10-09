
public class TailRecursion {

//ONLY TAIL RECURSIVE IF RUNNING_TOTAL = 0
//Code written by hand, but based on Python implementation from top answer on
// https://stackoverflow.com/questions/33923/what-is-tail-recursion
	 public static int tailrecsum(int x, int running_total) {  
		 if (x == 0) {
			 return running_total;
		 }
		 
		 else {
			 return tailrecsum(x - 1, running_total + x);
		 }
		 
} 


public static void main(String[] args) {
	
	
	System.out.println(tailrecsum(5,0));

} }

