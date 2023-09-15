package out.production.Socket_program.Parking_Ticket_generator;

import java.io.*;
import java.net.*;
import java.util.Scanner;

import static java.lang.Thread.sleep;

public class photoclient {
    public static void main(String[] args) {
        try {
            // Connect to the server
            Socket socket = new Socket("localhost", 9998);
            System.out.println("System successfully connect to localhost");
            sleep(700);
            System.out.println("Welcome to Parking Ticket Generator");
            sleep(700);
            InputStream inputStream = socket.getInputStream();
            OutputStream out = socket.getOutputStream();
            while (true) {
                //Entering the vehicle number
                Scanner in = new Scanner(System.in);
                System.out.println("");
                System.out.println("Vehicle number must be like tn8040-4 (4 denotes type of wheeler)");
                sleep(500);
                System.out.print("Enter the Vehicle number ");

                String num = in.next();
                out.write(num.getBytes());
                //receive image from server

                byte[] imagedata = new byte[1024];
                ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
                int bytesRead;
                while ((bytesRead = inputStream.read(imagedata)) != -1) {
                    byteArrayOutputStream.write(imagedata, 0, bytesRead);
                }
                //save the received image
                String location = "G:\\Socket_pgrm\\Tickets\\" + num + ".jpg";
                File imagefile = new File(location);
                FileOutputStream fileOutputStream = new FileOutputStream(imagefile);
                byteArrayOutputStream.writeTo(fileOutputStream);

                String statement = "Your Ticket is successfully generated and saved in G:/Socket_pgrm/Tickets/ Location";
                System.out.println(statement);
                //connection close
                byteArrayOutputStream.close();
                inputStream.close();
                fileOutputStream.close();


                socket.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}
