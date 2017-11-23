import socket,os,struct,argparse,math,sys

parser = argparse.ArgumentParser("start request!")
parser.add_argument("--ip", help="IP to Request", type = str, default = "localhost" )
parser.add_argument("--port", help="port to Request", type = int, default = "5000" )
parser.add_argument("--upload", help="the path of file to upload", type = str )
args , unknown_args = parser.parse_known_args()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((args.ip,args.port))
def progressbar(cur,total):
    percent = '{:.2%}'.format(cur / total)
    sys.stdout.write('\r')
    sys.stdout.write('[%-50s] %s' % ( '=' * int(math.floor(cur * 50 /total)),percent))
    sys.stdout.flush()
    if cur == total:
        sys.stdout.write('\n')
filepath = args.upload
if os.path.isfile(filepath):
    fileinfo_size = struct.calcsize('128sI')
    fhead = struct.pack('128sI',os.path.basename(filepath),os.stat(filepath).st_size)
    s.send(fhead)
    print 'client filepath:',filepath
    fo = open(filepath,'rb')
    total_size = os.stat(filepath).st_size
    sended_size = 0
    while True:
        filedata = fo.read(1024)
        if not filedata:
            break
        s.send(filedata)
        sended_size += 1024
        progressbar(sended_size,total_size)
    fo.close()
    s.close()
    print 'send over'
