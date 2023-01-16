import java.io.*;
  
public class solution {
    public static void main(String args[])
    {
  
        // try-catch block to handle exceptions
        try {
  
            // Create a file object
            File f = File("../Project BD-1/Used Things/Chatbot/sylsound/base/*.wav");
            
            // Get the Name of the given file f
            String Name = f.getName();
  
            // Display the file Name of the file object
            System.out.println("File Name : " + Name);
        }
        catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }
}
