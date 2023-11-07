<H1><b> THIS IS THE DOCUMENTATION FOR PURRFECT URL </b></H1>

<H2> CREDITS-- </H2>
1. Code: self (https://github.com/Asher-Ul-Haque) <br>
2. Artwork/Resources: self (https://github.com/Asher-Ul-Haque) <br>
3. Artwork inspiration: google search <br>
4. Customtkinter: Tom Schimansky (https://github.com/TomSchimansky) <br>
5. Tkinter Tutorial: Clear Code: (https://www.youtube.com/@ClearCode) <br>

<H2>REQUIREMENTS TO RUN</H2>
1. Python <br>
2. Customtkinter library<br>
3. Pillow (PIL) library<br>
4. Packaging library<br>
5. QRcode library<br>

<H3>HOW TO INSTALL ALL THE LIBRARIES</H3>
<H4>MAC</H4>
1. Open any terminal. Terminal can be found in any IDE or by pressing cmd+spacebar<br>
2. Input the following code and press enter<br>
<b>pip3 install customtkinter packaging qrcode Pillow</b><br>
<H4>WINDOWS</H4>
1. Open any terminal. Termincal can be found in any IDE or by searching for Powershell
2. Input the following code and press enter<br>
<b>pip install customtkinter packaging qrcode Pillow</b><br>

<H2> THE MAIN PROGRAM</H2>

<H3> Why did I make this program </H3>
<p>So Basically, I came across a question on leetcode that asked me to create a class with two methods; one of them takes a normal long URL like wwww.google.com and returns a small URL, and another one takes this short URL and converts it back to the original. So Basically, tinyURL. I tried to make it but couldn't. I made a long URL repeatedly; I was trying to encrypt the URL to make it shorter. I failed to; when I found out how to make it, it pissed me off so much that I decided to make a whole app for it.</p>
<br>
<H3>How the program works-</H3>
1. The program has three functions: one to shorten a URL, one to make a QR code and one to lengthen a shortened URL<br>
a. Any long URL needs to satisfy two conditions to be acceptable- <br>
  i. It must have a valid beginning like http://, https://, www. etc <br>
  ii. If it already exists in the database, it should be no more than 30 days old<br>
b. If the conditions are satisfied and the link exists in the database, it is retrieved and shown <br>
c. If the conditions are satisfied and the link doesn't exist in the database, it is created, and a record of the long URL, short URL, and the date created is added to the database<br>
d. If the conditions are unsatisfied, an error message says the URL is invalid. <br>
e. One can also create a QR code for the URL shortened by pressing the QR code button<br><br>
2. The long URL function takes a short URL as input; it returns the original URL after retrieving it from the database if these two conditions are satisfied. If it is not satisfied, then an error message is shown saying that the link was not found <br>
<br>

