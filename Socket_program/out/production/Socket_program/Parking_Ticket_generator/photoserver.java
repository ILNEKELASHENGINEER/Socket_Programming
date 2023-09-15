package out.production.Socket_program.Parking_Ticket_generator;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import java.io.*;
import java.net.*;
//import org.opencv.*;
class photoserver {
    public static void main(String[] args) throws IOException{
            ServerSocket serverSocket = new ServerSocket(9998);
            System.out.println("Waiting for client to connect...");

            while(true){
            //Read the image
            Socket sock = serverSocket.accept();
            System.out.println("Client is connected Successfully");
            InputStream in = sock.getInputStream();
            OutputStream out = sock.getOutputStream();

            //Receive vehicle number from customer
            byte [] number = new byte[2048];
            in.read(number);
            String vehno = new String(number).trim().toUpperCase();
            System.out.println("Ticket "+vehno+" is generated Successfully");

            //image
                    BufferedImage image = null;
                    try {
                            image = ImageIO.read(new File("Ticktempjpg.jpg"));
                    } catch (IOException e) {
                            e.printStackTrace();
                    }
                    Graphics2D g2d = image.createGraphics();
                    Font font = new Font("Poppins", Font.BOLD, 48);
                    Color color = Color.BLACK;
                    g2d.setFont(font);
                    g2d.setColor(color);

                    // Write the text on the image
                    String text = vehno;
                    int x = 400;
                    int y = 176;
                    g2d.drawString(text, x, y);
                    g2d.dispose();
                    try {
                            ImageIO.write(image, "jpg", new File("output.jpg"));
                    } catch (IOException e) {
                            e.printStackTrace();
                    }
                    File imageFile = new File("output.jpg");
                    FileInputStream fileInputStream = new FileInputStream(imageFile);
                    byte[] imageData = new byte[(int) imageFile.length()];
                    fileInputStream.read(imageData);

            //Send the image to client
                    OutputStream outputStream = sock.getOutputStream();
                    outputStream.write(imageData);
                    fileInputStream.close();
            outputStream.close();
            sock.close();

            }
//            serverSocket.close();

    }
}

