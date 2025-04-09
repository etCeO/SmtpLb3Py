from socket import *
import base64
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.gmail.com"  # You can replace this with your preferred mail server (e.g., Gmail)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 587))  # Port 587 is used for SMTP submission

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send STARTTLS command to initiate encryption
starttls_command = "STARTTLS\r\n"
clientSocket.send(starttls_command.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '220':
    print('220 reply not received from server for STARTTLS.')

# Upgrade the connection to a secure TLS connection using SSLContext
context = ssl.create_default_context()
clientSocket = context.wrap_socket(clientSocket, server_hostname=mailserver)

# Authentication (use base64 encoding for username and password)
username = "examplepythonsmtp@gmail.com"  # Gmail address (sendee)
password = "mfce czal hrnm otfg"  # App Password

# Send AUTH LOGIN command and encode username and password in base64
auth_command = "AUTH LOGIN\r\n"
clientSocket.send(auth_command.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '334':
    print('334 reply not received from server for AUTH LOGIN.')

# Send the base64 encoded username
encoded_username = base64.b64encode(username.encode()).decode() + "\r\n"
clientSocket.send(encoded_username.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '334':
    print('334 reply not received from server for username.')

# Send the base64 encoded password
encoded_password = base64.b64encode(password.encode()).decode() + "\r\n"
clientSocket.send(encoded_password.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '235':
    print('235 reply not received from server for authentication.')

# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM:<examplepythonsmtp@gmail.com>\r\n"  # sender's email address
clientSocket.send(mailFrom.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptTo = "RCPT TO:<karamhosn@gmail.com>\r\n"  # Replace with the recipient's email address
clientSocket.send(rcptTo.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
if recv7[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv8 = clientSocket.recv(1024).decode()
print(recv8)
if recv8[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
message = "Subject: Test Email\r\n" + msg
clientSocket.send(message.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())

# Send QUIT command and get server response.
quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand.encode())
recv9 = clientSocket.recv(1024).decode()
print(recv9)
if recv9[:3] != '221':
    print('221 reply not received from server.')

# Close the socket
clientSocket.close()