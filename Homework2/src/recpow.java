
public class recpow {

	//This function is not meant to work for negative exponents
	//This function cannot work past n = 30 because it would go over the limit of an integer.
	
	public static int recPow(int n) {
	if (n > 30 || n < 0) {
		System.out.println("This function cannot accept values less than 0 or greater than 30");
		return -1; //-1 being used as a a relatively standard output to signify an error has occurred 
	}
	if (n == 0) {
		return 1; }
	
	else {
		return 2 * recPow(n - 1); }
				
} 


public static void main(String[] args) {
	recPow(-1);
	System.out.println(recPow(0));
	System.out.println(recPow(1));
	System.out.println(recPow(5));
	System.out.println(recPow(10));
	System.out.println(recPow(20));
	System.out.println(recPow(30));
	recPow(31);
} }

