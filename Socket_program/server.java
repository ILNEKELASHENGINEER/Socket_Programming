import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
//import com.mongodb.MongoClient;
//import com.mongodb.MongoClientURI;
//import com.mongodb.client.MongoDatabase;

public class server {

    public static void main(String []args) throws IOException {
        ServerSocket serSocket = new ServerSocket(9999);
        System.out.println("started listen to 9999");
        quoute prdtname  = new quoute();
        while(true) {
            System.out.println("\nWaiting for the connection...");
            Socket sock = serSocket.accept();
            InputStream in = sock.getInputStream();
            OutputStream out = sock.getOutputStream();

            System.out.println("Waiting for message...");

            byte[] request  = new byte[100];
            in.read(request);
            String message = new String(request).trim();

            System.out.println("Received product name :-> "+message);
            System.out.println("User "+message+" is connected Successfully");

//            String output = prdtname.getproductinfo(message);
//            if(output == null){
//                output = "Invalid";
//            }
            String output = "Server is successfully connected "+message;
            out.write(output.getBytes());
            System.out.println(output);
            sock.close();
        }
    }
}
    class quoute {
        Map<String ,String> product = new HashMap<String,String>();
        public quoute(){
            product.put("a","100");
            product.put("b","200");
        }
        public String getproductinfo(String prdt){

            return product.get(prdt);
        }
    }
