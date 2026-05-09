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

    "7.Random Process": r"""
Simulation  study of random process . find various  statistical  parameters of the random  process .
clc;
clear;
close all;

% 1. Generate a random process
N = 1000;               % Number of samples
x = randn(1, N);        % Random process (Gaussian)

% 2. Calculate statistical parameters
mean_x      = mean(x);
median_x    = median(x);
variance_x  = var(x);
std_x       = std(x);
range_x     = max(x) - min(x);

% Autocorrelation
[R, lags] = xcorr(x, 'biased');

% Display results
fprintf('Mean = %f\n', mean_x);
fprintf('Median = %f\n', median_x);
fprintf('Variance = %f\n', variance_x);
fprintf('Std Dev = %f\n', std_x);
fprintf('Range = %f\n', range_x);

% 3. Plot random variable
figure;
plot(x);
title('Random Process');
xlabel('Sample Number');
ylabel('Amplitude');
grid on;

% Plot autocorrelation
figure;
plot(lags, R);
title('Autocorrelation of Random Process');
xlabel('Lag');
ylabel('R(\tau)');
grid on;

""",
    "5&6": r"""
    M-ary QAM 

M = input('number of symbols = ');
SNR = input('SNR of QAM system in dB = ');

x1 = randi([0 M-1], 1000, 1);
y2 = qammod (x1, M);
y2n = awgn (y2, SNR, 'measured');
scatterplot (y2n);
y2r = qamdemod (x1, M);
[num_error, er, rate] = symerr(x1, y2r);

M-ary PSK

M = input('number of symbols = ');
SNR = input('SNR of QAM system in dB = ');

x1 = randi([0 M-1], 1000, 1);
y2 = pskmod (x1, M, pi/M);
y2n = awgn (y2, SNR, 'measured');
scatterplot (y2n);
y2r = pskdemod (x1, M, pi/M);
[num_error, er, rate] = symerr(x1, y2r);""",
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
