package unit1;
import java.sql.*;
public class Unit1 {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql:///keval","root","");
            
            Statement st = con.createStatement();
            String qry = "CREATE TABLE pro1(Rollno INT,Name VARCHAR(20))";
            
            st.executeUpdate(qry);
            
            System.out.println("Table created !!!");
        } catch (Exception e) {
            System.out.println("Error"+e);
        }
    }
}