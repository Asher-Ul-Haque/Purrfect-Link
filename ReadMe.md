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

<H3>How To Install Customtkinter</H3>
Customtkinter: https://github.com/TomSchimansky/CustomTkinter<br>
<H4>MAC</H4>
1. Method 1: simple and short:<br>
a) open pip3 in terminal<br>
b) pip3 install customtkinter<br><br>
2. Method 2: complex and sure: <br>
a) use customtkinter link to download customtkinter <br>
b) open terminal <br>
c) pip3 install customtkinter <br>

<H4>WINDOWS</H4>
1. Method 1: simple and short:<br>
a) open pip in terminal<br>
b) pip install customtkinter<br><br>
2. Method 2: complex and sure: <br>
a) use customtkinter link to download customtkinter <br>
b) open terminal <br>
c) pip install customtkinter <br>

<H3>How to Install QrCode </H3>
<H4>MAC</H4>
1. open terminal<br>
2. pip3 install qrcode <br>
<H4>WINDOWS</H4>
1. open terminal<br>
2. pip install qrcode <br>

<H3>How to Install Pillow</H3>
<H4>MAC</H4>
1. open terminal <br>
2. pip3 install Pillow <br>
<H4>WINDOWS</H4>
1. open terminal <br>
2. pip install Pillow <br>

<H2> THE MAIN PROGRAM</H2>

<H3> Why did I make this program </H3>
<p>So Basically, I came across a question on leetcode that asked me to create a class with two methods; one of them takes a normal long URL like wwww.google.com and returns a small URL, and another one takes this short URL and converts it back to the original. So Basically, tinyURL. I tried to make it but couldn't. I made a long URL repeatedly; I was trying to encrypt the URL to make it shorter. I failed to; when I found out how to make it, it pissed me off so much that I decided to make a whole app for it.</p>
<br>
<H3>How the program works-</H3>
1. The program has two functions: one to shorten a URL and takes into input a longURL<br>
a. Any long URL needs to satisfy two conditions to be acceptable- <br>
  i. It must have a valid beginning like http://, https://, www. etc <br>
  ii. If it already exists in the database, it should be no more than 30 days old<br>
b. If the conditions are satisfied and the link exists in database it is retrieved and shown <br>
c. If the conditions are satisfied and the link doesnt exist in the database it is created and a record of the longURL, shortURL, and the date created is added in the database<br>
d. If the conditions are not satisfied an error message is shown saying that the URL is invalid. <br>
<br>
2. The long URL function takes a short URL as input, it returns the original URL after retrieving it from the database if these two conditions are satisfied. If it is not satisfied then an error message is showsn saying that link was not found <br>
<br>

