import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ParserDemo {

	private static String file1 = "C:\\Users\\User\\Desktop\\prog1.jay";
	
	public static void main(String args[]) throws IOException  {
		
		
		TokenStream tStream = new TokenStream(file1);
		
		System.out.println("test1");
		ConcreteSyntax cSyntax = new ConcreteSyntax(tStream);
		System.out.println("test2");
		Program p = cSyntax.program();
		System.out.println(p.display());
		System.out.println("test"); 
	} 

}
