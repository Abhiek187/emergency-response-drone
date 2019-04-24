// Written and Debugged by: Sri Sai Krishna Tottempudi
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;
import java.io.FilterInputStream;
import java.io.DataInputStream;
import java.lang.Double;
public class Veloctiy {
	public static void main(String[] args) throws IOException
	{
		URL url = new URL("https://abhiek187.github.io/emergency-response-drone/1_code/Location/SEtest.html");
		URLConnection con = url.openConnection();
        InputStream is =con.getInputStream();
        BufferedReader br = new BufferedReader(new InputStreamReader(is));
        String line = null;
        while((line = br.readLine()) != null)
        {
        	if(isDouble(line)==true)
        	{
        		System.out.println(line);
        	}
        	else
        	{
        		System.out.println("It can't locate any numbers");
        	}
        }
	}
    static boolean isDouble(String str)
    {
    	try {
    		Double.parseDouble(str);
    		return true;
    	} catch (NumberFormatException e) {
    		return false;
    	}
    }
}
