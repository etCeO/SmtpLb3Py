from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 587))

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

# Send MAIL FROM command and print server response.
mailFrom = 'MAIL FROM:<your-email@gmail.com>\r\n'  # Replace with your email
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

if recv2[:3] != '250':
    print('250 reply not received from server.')
    
# Send RCPT TO command and print server response.
rcptTo = 'RCPT TO:<recipient-email@example.com>\r\n'  # Replace with recipient's email
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)

if recv3[:3] != '250':
    print('250 reply not received from server.')
    
# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)

if recv4[:3] != '354':
    print('354 reply not received from server.')
    
# Send message data.
clientSocket.send(msg.encode())
    
# Message ends with a single period.
clientSocket.send(endmsg.encode())
    
# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)

if recv5[:3] != '221':
    print('221 reply not received from server.')
