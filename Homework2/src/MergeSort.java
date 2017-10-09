
public class MergeSort {
	
	
	public static int[] mergeSort(int[]a, int[]b) {
		int size = a.length + b.length;
		int Finalarray[] = new int[size];
				
		 
		 if (a.length != 1 ) { //Base Case
			 // This simulates the splitting from slide 18
		 int k = 0; //Needed for a's splitting if block
		 int[] a_half1 = new int[(int) Math.ceil(a.length/2.0)];
		 int[] a_half2 = new int[(int) Math.floor(a.length/2.0)];
		  for (int i = 0; i < a_half1.length; i++)
		       	a_half1[i] = a[i];
		  for (int j = a_half1.length; j < a.length; j++) {
			  	a_half2[k] = a[j];
			  	k++; } 
		  a = mergeSort(a_half1, a_half2); //Recursive Call
		 }
		 
		 if (b.length != 1 ) { //Base Case
			 // This simulates the splitting from slide 18
			 int l = 0; //Needed for b's splitting if block
			 int[] b_half1 = new int[(int) Math.ceil(b.length/2.0)];
			 int[] b_half2 = new int[(int) Math.floor(b.length/2.0)];
			  for (int i = 0; i < b_half1.length; i++)
			       	b_half1[i] = b[i];
			  for (int j = b_half1.length; j < b.length; j++) {
				  	b_half2[l] = b[j];
				  	l++; } 
			  
			  b = mergeSort(b_half1, b_half2); //Recursive Call
		 }
		 
		 //Next we need to look through the elements of a and b, compare them, and add the smaller one
		 // to the Finalarray
		 
		 int ac = 0; //A-Counter
		 int bc = 0; //B-Counter
		 
	
		 
		 for (int m = 0; m < size; m++) { 
			 if (bc < b.length && ac < a.length) {
				 if(a[ac] <= b[bc]) { //Includes failsafe for if both are equal
					 Finalarray[m] = a[ac];
					 ac++;
			 }
				 else if(b[bc] < a[ac]) {
					 Finalarray[m] = b[bc];
					 bc++; } }
			 else if (bc >= b.length) {
				 Finalarray[m] = a[ac];
			 	 ac++; }
			 else if (ac >= a.length) {
				 Finalarray[m] = b[bc];
			 	 bc++; } }
			 
					 
			 
			 
		 
		 
		 return Finalarray; } 
		 
		 
		 

		



public static void main(String[] args) {
	
	int a[] = {1};
	int b[] = {2};
	int c[] = new int[a.length + b.length];
	c = mergeSort(a,b);
	for (int i = 0; i < c.length; i++)
		System.out.println(c[i]);
} }