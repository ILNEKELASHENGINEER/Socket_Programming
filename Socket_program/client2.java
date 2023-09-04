import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class client2 {
    public static void main(String []args) throws IOException {
        Scanner ins = new Scanner(System.in);
        System.out.println("Enter your name to save in server");
        String product=ins.next();
        Socket sock = new Socket("127.0.0.1",9999);
        System.out.println("Connected to network");
//        String product = "a";
        InputStream in = sock.getInputStream();
        OutputStream out = sock.getOutputStream();

        out.write(product.getBytes());

        byte[] newprod = new byte[100];
        in.read(newprod);

        String input = new String(newprod).trim();
        System.out.println("Obtained message: "+input);
//        sock.close();
    }
}
