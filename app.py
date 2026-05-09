import streamlit as st
import html
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="PIC Programs", layout="wide")

# Hide the main area watermark and menu
st.markdown("""
    <style>
        
    </style>
""", unsafe_allow_html=True)

# Image paths for interfacing diagrams
image_paths = ["2exp.jpg", "3exp.jpg", "PIC_page-0003.jpg", "PIC_page-0004.jpg", "PIC_page-0005.jpg", "PIC_page-0006.jpg", "PIC_page-0007.jpg", "PIC_page-0008.jpg"]

PIC_PROGRAMS = {
    
    "EXP1KEYLISTENER": r"""
steps :
file new proj then java with maven then new app
source package right click java class
and put code

import java.awt.*;
import java.awt.event.*;

public class Ex1 extends Frame implements KeyListener {

    Label l;
    TextArea area;

    Ex1() {

        l = new Label();
        l.setBounds(20, 50, 100, 20);

        area = new TextArea();
        area.setBounds(20, 80, 300, 300);

        area.addKeyListener(this);

        add(l);
        add(area);

        setSize(400, 400);
        setLayout(null);
        setVisible(true);
    }

    public void keyPressed(KeyEvent e) {
        l.setText("Key Pressed");
    }

    public void keyReleased(KeyEvent e) {
        l.setText("Key Released");
    }

    public void keyTyped(KeyEvent e) {
        l.setText("Key Typed");
    }

    public static void main(String[] args) {
        new Ex1();
    }
}
""",
    "EXP2MOUSECLICK ": r"""
import java.awt.*;
import java.awt.event.*;

public class MouseDemo extends Frame implements MouseListener {

    Label l;

    MouseDemo() {

        addMouseListener(this);

        l = new Label();
        l.setBounds(20, 50, 100, 20);
        add(l);

        setSize(300, 300);
        setLayout(null);
        setVisible(true);
    }

    public void mouseClicked(MouseEvent e) {
        l.setText("Mouse Clicked");
    }

    public void mouseEntered(MouseEvent e) {
        l.setText("Mouse Entered");
    }

    public void mouseExited(MouseEvent e) {
        l.setText("Mouse Exited");
    }

    public void mousePressed(MouseEvent e) {
        l.setText("Mouse Pressed");
    }

    public void mouseReleased(MouseEvent e) {
        l.setText("Mouse Released");
    }

    public static void main(String[] args) {
        new MouseDemo();
    }
}

""",
"3marks": r"""
import javax.swing.JOptionPane;

private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {                                         
double maths, english, bio, total, avg;
String grade;

maths = Integer.parseInt(jTextField2.getText());
english = Integer.parseInt(jTextField3.getText());
bio = Integer.parseInt(jTextField4.getText());

total = maths + english + bio;

avg = total / 3;

if(avg >= 85)
{
    grade = "A";
}
else if(avg >= 75)
{
    grade = "B";
}
else if(avg >= 65)
{
    grade = "C";
}
else if(avg >= 45)
{
    grade = "S";
}
else
{
    grade = "F";
}

JOptionPane.showMessageDialog(this,
        "Total = " + total +
        "\nAverage = " + avg +
        "\nGrade = " + grade);        
}
""",
    "4JDBCNETBEANS": r"""

mysql then code this
then netbeans file new proj java with maven java app
add JAR in lib
right clock source package add java class whose code is :


package exp4;

import java.sql.Connection;
import java.sql.Date;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;

public class Exp4 {

    public static void main(String args[]) {

        try {

            String mysqlUrl =
            "jdbc:mysql://localhost:3306/test?useSSL=false&serverTimezone=UTC";

            Connection con = DriverManager.getConnection(
                    mysqlUrl,
                    "root",
                    "password"
            );

            System.out.println("Connection established......");

            Statement stmt = con.createStatement();

            PreparedStatement pstmt = con.prepareStatement(
                    "INSERT INTO Players values (?, ?, ?, ?, ?, ?)"
            );

            pstmt.setInt(1, 9);
            pstmt.setString(2, "R");
            pstmt.setString(3, "Mc");
            pstmt.setDate(4, new Date(513596800000L));
            pstmt.setString(5, "Ku");
            pstmt.setString(6, "India");

            pstmt.executeUpdate();

            String query = "Select * from Players";

            ResultSet rs = stmt.executeQuery(query);

            while (rs.next()) {

                int id = rs.getInt("ID");
                String first_name = rs.getString("First_Name");
                String last_name = rs.getString("Last_Name");
                Date dob = rs.getDate("Date_Of_Birth");
                String place = rs.getString("Place_Of_Birth");
                String country = rs.getString("Country");

                System.out.print("Id: " + id + ", ");
                System.out.print("First Name: " + first_name + ", ");
                System.out.print("Last Name: " + last_name + ", ");
                System.out.print("DOB: " + dob + ", ");
                System.out.print("Place: " + place + ", ");
                System.out.print("Country: " + country);

                System.out.println();
            }

            con.close();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}

    """,

    

    "4MYSQL": r"""
CREATE DATABASE test;
USE test;

CREATE TABLE Players(
    ID INT,
    First_Name VARCHAR(255),
    Last_Name VARCHAR(255),
    Date_Of_Birth DATE,
    Place_Of_Birth VARCHAR(255),
    Country VARCHAR(255),
    PRIMARY KEY (ID)
);

INSERT INTO Players VALUES
(1, 'Shikhar', 'Dhawan', '1981-12-05', 'Delhi', 'India'),
(2, 'Jonathan', 'Trott', '1981-04-22', 'CapeTown', 'SouthAfrica'),
(3, 'Kumara', 'Sangakkara', '1977-10-27', 'Matale', 'Srilanka'),
(4, 'Virat', 'Kohli', '1988-11-05', 'Delhi', 'India'),
(5, 'Rohit', 'Sharma', '1987-04-30', 'Nagpur', 'India'),
(6, 'Ravindra', 'Jadeja', '1988-12-06', 'Nagpur', 'India'),
(7, 'James', 'Anderson', '1982-06-30', 'Burnley', 'England');

SELECT * FROM Players;

""",

    "5Palindrome": r"""
File → New Project
→ Java with Ant
→ Java Application
→ Project Name: Exp5_RMI
→ Finish

Right Click Project Name
→ New
→ Java Interface
→ Name: PalindromeChecker
→ Finish

import java.rmi.Remote;
import java.rmi.RemoteException;
public interface PalindromeChecker extends Remote {
public boolean checkPalindrome(String s) throws RemoteException;
}

Right Click Project Name
→ New
→ Java Class
→ Name: PalindromeServer
→ Finish

import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
public class PalindromeServer extends UnicastRemoteObject implements PalindromeChecker {
public PalindromeServer() throws RemoteException{
super();
}
@Override
public boolean checkPalindrome(String s) throws RemoteException {

// remove all non-alphanumeric characters and convert to lowercase
String cleanString = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
// check if the string is equal to its reverse
String reversedString = new StringBuilder(cleanString).reverse().toString();
return cleanString.equals(reversedString);
}
public static void main(String[] args) {
try {
// create and export the server object
// bind the object to an RMI registry
Registry registry = LocateRegistry.createRegistry(9999);
registry.rebind("PalindromeChecker", new PalindromeServer());
System.out.println("PalindromeChecker server ready.");
}
catch (RemoteException e) {
System.out.println("exception"+e);
}
}
}


Right Click Project Name
→ New
→ Java Class
→ Name: PalindromeClient
→ Finish

import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class PalindromeClient {

    public static void main(String[] args) throws RemoteException {
        PalindromeClient c = new PalindromeClient();
        c.connectRemote();
    }

    public void connectRemote() throws RemoteException {
        try {
            // Connect to the RMI registry running on localhost at port 9999
            Registry registry = LocateRegistry.getRegistry("localhost", 9999);

            // Look up the remote object by name
            PalindromeChecker checker =
                    (PalindromeChecker) registry.lookup("PalindromeChecker");

            // Test strings
            String[] strings = {
                "racecar",
                "hello",
                "A man a plan a canal Panama",
                "12321"
            };

            // Call remote method and print result
            for (String s : strings) {
                System.out.println(
                    s + " is " +
                    (checker.checkPalindrome(s) ? "" : "not ") +
                    "a palindrome."
                );
            }

        } catch (NotBoundException | RemoteException e) {
            System.err.println(
                "PalindromeChecker client exception: " + e.toString()
            );
        }
    }
}

""",
    "6IP": r"""
    java with ant
Right Click Project
→ New
→ Java Class
→ Name: InetADRESS
→ Finish

package InetADRESS;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.Scanner;

public class InetADRESS {

public static void main(String[] args) {
Scanner sc=new Scanner(System.in);
System.out.println("enter");
String host=sc.next();
try
{
InetAddress ip=InetAddress.getByName(host);
System.out.println("IP "+ip.getHostAddress());
}
catch(UnknownHostException e)
{
System.out.println(e);

}
}
}""",
    "7valid.java":r"""
java with ant then java app
right click on source package then servlet:

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/valid")
public class valid extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest request,
                          HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html");

        PrintWriter out = response.getWriter();

        String uname = request.getParameter("uname");
        String pass = request.getParameter("upass");

        // Correct credentials
        if (uname.equals("suu") && pass.equals("pass")) {

            RequestDispatcher rd =
                    request.getRequestDispatcher("/welcome.html");

            rd.forward(request, response);

        } else {

            out.println("<h3>Invalid Username or Password</h3>");

            RequestDispatcher rd =
                    request.getRequestDispatcher("/index.html");

            rd.include(request, response);
        }
    }
}

    """,
    "7index.html":r"""<!DOCTYPE html>
<html>
<head>
    <title>Login Form</title>
</head>

<body>

<form action="valid" method="post">

    Username:
    <input type="text" name="uname">

    <br><br>

    Password:
    <input type="password" name="upass">

    <br><br>

    <input type="submit" value="Submit">

</form>

</body>
</html>
    
    """,
    "7welcome.html":r"""
    <!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
    <meta charset="UTF-8">
</head>
<body>

<h1>Welcome to the page</h1>
Login Confirmed!!

</body>
</html>
    
    """,
    "8RMI-ADDITION":r"""
    java with ant
    java app
    then 
    project name interface: Calculator

import java.rmi.Remote;
import java.rmi.RemoteException;
public interface Calculator extends Remote {
int add(int x, int y) throws RemoteException;
int subtract(int x, int y) throws RemoteException;
}

    then new class CalculatorImpl

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
public class CalculatorImpl extends UnicastRemoteObject implements
Calculator {
public CalculatorImpl() throws RemoteException {
super();
}
public int add(int x, int y) throws RemoteException {
return x + y;
}
public int subtract(int x, int y) throws RemoteException {

return x - y;
}
}

    then new class CalculatorServer

import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
public class CalculatorServer {
public static void main(String[] args) {
try {
// Create an instance of the remote object
Calculator calculator = new CalculatorImpl();
// Get a reference to the RMI registry
Registry registry = LocateRegistry.createRegistry(1099);
// Bind the remote object to the registry
registry.rebind("Calculator", calculator);
System.out.println("CalculatorServer ready.");
} catch (RemoteException e) {
System.err.println("CalculatorServer exception:");
}
}
}

    then new class CalculatorClient

import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class CalculatorClient {

    public static void main(String[] args) {

        try {
            // Get reference to the RMI registry running on localhost
            Registry registry = LocateRegistry.getRegistry("localhost");

            // Look up the remote Calculator object
            Calculator calculator =
                    (Calculator) registry.lookup("Calculator");

            // Call remote add() method
            int result = calculator.add(1, 2);
            System.out.println("1 + 2 = " + result);

            // Call remote subtract() method
            result = calculator.subtract(5, 3);
            System.out.println("5 - 3 = " + result);

        } catch (NotBoundException | RemoteException e) {
            System.err.println("CalculatorClient exception: " + e);
        }
    }
}

then run derver client
    """,
    "9JSP":r"""
    java with ant
    web app
    server tomcat
    change index.html to index.jsp using properties

    code:
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="java.util.Date"%>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Current Date and Time</title>
</head>
<body>

    <h1>Current Date and Time</h1>

    <%
        Date d = new Date();
        out.println(d);
    %>

</body>
</html>
    
    """,
    "10IP":r"""
    LOL
    """,

}

st.sidebar.title("Shhhhhhhh!!")
sel = st.sidebar.radio("Select", list(PIC_PROGRAMS.keys()))

# Show code for selections
code = PIC_PROGRAMS[sel]

# Create a JS-safe version of the raw code to copy via clipboard (escape backticks and backslashes)
js_safe = code.replace('\\','\\\\').replace('`','\\`')

# Persistent copy button in the sidebar — always available and will copy the raw code even if the
# main code panel is not visible.
with st.sidebar:
    components.html(f"""
    <div style='padding:6px;display:flex;justify-content:flex-end;'>
        <button style='padding:6px 10px;border-radius:4px;border:none;background:#28a745;color:#fff;cursor:pointer;font-weight:600;' onclick="navigator.clipboard.writeText(`{js_safe}`)">Copy</button>
    </div>
    """, height=60)

pre_id = f"code_{abs(hash(sel))}"
esc = html.escape(code)
components.html(f"""
<div style='background:#f1f1f1;padding:10px;border-radius:6px;position:relative;'>
    <button style='position:absolute;top:8px;left:8px;padding:6px 10px;border-radius:4px;border:none;background:#007bff;color:#fff;cursor:pointer;z-index:2;font-weight:600;display:inline-flex;align-items:center;gap:4px;' 
        onclick="(() => {{
            const btn = event.target;
            const text = document.getElementById('{pre_id}').innerText;
            navigator.clipboard.writeText(text)
                .then(() => {{
                    btn.innerHTML = '✓ Copied';
                    setTimeout(() => btn.innerHTML = 'Copy', 1000);
                }})
                .catch(err => alert('Failed to copy: ' + err));
        }})()">Copy</button>
    <pre id='{pre_id}' style='white-space:pre-wrap;font-family:monospace;margin-top:36px;max-height:500px;overflow-y:auto;'>{esc}</pre>
</div>
""",height=700)

# Keep the download button but hide code display
if sel:
    st.download_button("Download", code, file_name=sel+".c")
