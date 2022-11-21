# Zoho-Mail-Sender

Zoho Mail Sender Using Python (SMTP Server)

You can download full guide and code from here: <a href="https://drive.google.com/file/d/1OhZQmRLY5xvj3j7iRqYZDig10plGeZ43/view?usp=share_link">Download</a>

# Sending mail from Zoho Mail (Forever Free Plan) using Python
1.	Import the required libraries

 ![image](https://user-images.githubusercontent.com/107746959/203063326-401fe99e-9f42-4448-be05-1d476d9c9cb6.png)

2.	Initialize the MIMEText and Write the message of the email (between the quotation marks " ")

![image](https://user-images.githubusercontent.com/107746959/203063424-fd48d7bb-eaff-4d42-886f-e526d697732e.png)

3.	Write the subject of email (between the quotation marks " ") 

![image](https://user-images.githubusercontent.com/107746959/203063508-bbf35bb7-86f9-4c38-a34f-36fd2390e331.png)

4.	Write the sender Email ID (between the quotation marks " ") 

![image](https://user-images.githubusercontent.com/107746959/203063542-ec1bf8d5-7cbc-444a-87b0-75c7f3dd3dfd.png)

5.	Write the receiver Email ID (between the quotation marks " ") 

![image](https://user-images.githubusercontent.com/107746959/203063588-db08d957-6658-4fd1-968c-39429a7329e9.png)

6.	Initialize the SMTP Server 
(Outgoing Server Name: smtppro.zoho.in
Port: 465 with SSL or
Port: 587 with TLS
Require Authentication: Yes 
for more info visit: https://www.zoho.com/mail/help/zoho-smtp.html) 

![image](https://user-images.githubusercontent.com/107746959/203063772-b2ce4bbd-0aa5-4bbf-811c-2e442dacf2cb.png)

7.	Write SMTP Server Login Credentials (SMTP Login Password is not same as the Zoho Mail Password)

![image](https://user-images.githubusercontent.com/107746959/203063807-cf591bf9-642a-4ba6-8509-44dbf4e0a08e.png)

8.	How to get SMTP Server Login Credentials Password?
a.	Go to mail.zoho.in

![image](https://user-images.githubusercontent.com/107746959/203063843-b12e418f-00ad-4aeb-96fa-193ceaea8f7b.png)

b.	Click on icon as show in image below

![image](https://user-images.githubusercontent.com/107746959/203063890-ca9042ba-84f3-48ac-8c0b-f5f45b38e619.png)

c.	Click on My Accounts as shown in image below

![image](https://user-images.githubusercontent.com/107746959/203063906-ec0cbed2-2242-49a6-b8fc-fc450f8a13e5.png)

d.	Enter the password of zoho mail

![image](https://user-images.githubusercontent.com/107746959/203063935-48506468-9a2b-4e17-9cc8-6cd80356177c.png)

e.	Click on Security > App Password on the left navigation bar

![image](https://user-images.githubusercontent.com/107746959/203063957-0caca220-40db-4a34-a69f-70862f6a015c.png)

f.	Click on Generate New Password

![image](https://user-images.githubusercontent.com/107746959/203063974-e21ed50f-f7ce-471d-99c7-1c77572b34f2.png)

g.	Enter the App Name then click on Generate

![image](https://user-images.githubusercontent.com/107746959/203063988-ca567a2f-d419-4e01-9eda-64ce36fa70b5.png)

h. You will get the Application-Specific Password that is SMTP server Login Password

![image](https://user-images.githubusercontent.com/107746959/203064011-b52fc365-d0e6-49c2-b4bf-d2382fbcebc5.png)
 
9.	Give request to Zoho SMTP Server

![image](https://user-images.githubusercontent.com/107746959/203064034-17b95eb8-e9f5-48a3-aad3-cf5e6860a489.png)

10.	Quit from Zoho SMTP Server 
 
![image](https://user-images.githubusercontent.com/107746959/203064049-1f606edf-9fc8-493a-9f66-8a13769ad12e.png)
