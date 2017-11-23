import socket,time,SocketServer,struct,os
host = '10.0.0.3'
port = 12307
ADDR = (host,port)

class MyRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print('connected from:',self.client_address)
        while True:
            fileinfo_size = struct.calcsize('128sI')
            self.buf = self.request.recv(fileinfo_size)
            if self.buf:
                self.filename,self.filesize = struct.unpack('128sI',self.buf)
                print 'filesize is:',self.filesize,'filename size is :',len(self.filename)
                self.filenewname = os.path.join("/code",('new_'+self.filename).strip('\00'))
                print self.filenewname,type(self.filenewname)
                recvd_size = 0
                file = open(self.filenewname,'wb')
                print 'stat receiving...'
                while not recvd_size == self.filesize:
                    if self.filesize - recvd_size > 1024:
                        rdata = self.request.recv(1024)
                        recvd_size += len(rdata)
                    else:
                        rdata = self.request.recv(self.filesize - recvd_size)
                        recvd_size = self.filesize
                    file.write(rdata)
                file.close()
                print 'receive done'
                self.request.close()
tcpServ = SocketServer.ThreadingTCPServer(ADDR,MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()  
