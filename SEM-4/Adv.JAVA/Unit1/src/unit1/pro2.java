
package unit1;
import java.sql.*;

public class pro2 {
    public static void main(String args[]){
        try {
            Class.forName("com.mysql.jdbc.Driver");
        Connection con = DriverManager.getConnection("jdbc:mysql:///keval","root","");
        
        Statement st = con.createStatement();
        int Rollno =1;
        String name = "keval";
        
        String qry = "INSERT into pro1 (Rollno,Name) values ('"+Rollno+"','"+name+"')";
        int ans = st.executeUpdate(qry);
        System.out.println(ans+"Added");
        } catch (Exception e) {
            System.out.println("Error"+e);
        }
    }
}
