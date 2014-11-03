import java.io.*;
import java.util.*;


public class InputTest {
    public static void main(String[] args) {
	int c;
	
	try {
	    InputStream in = new LowerCaseInputStream(new BufferedInputStream(new FileInputStream("/tmp/test.txt")));
	    while ((c = in.read()) >= 0) {
		System.out.print((char)c);
	    }
	    in.close();
	}
	catch (Exception e) {
	    System.out.println("Error " + e.getMessage());
	    e.printStackTrace();
	}
    }
}
