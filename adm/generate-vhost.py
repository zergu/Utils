#!/usr/bin/python

import sys, getopt

VHOST_DIR = "/etc/apache2/sites-enabled/"

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv,"h",[])
    except getopt.GetoptError:
        print 'generate-vhost.py <domainname> <path> <directoryindex>'
        sys.exit(2)

    for arg in args:
        if arg == '-h':
            print 'generate-vhost.py <domainname> <path> <directoryindex>'
            sys.exit()

    name = args[1]
    path = args[2]
    index = args[3]

    vhost = "<VirtualHost *:80>\n"
    vhost += "  ServerName {}\n".format(name)
    vhost += "  DocumentRoot \"{}\"\n".format(path)
    vhost += "  LogFormat \"%h %l %u %t %r %>s %b\" common\n"
    vhost += "  CustomLog /tmp/{}-access.log common\n".format(name)
    vhost += "  ErrorLog /tmp/{}-errors.log\n".format(name)
    vhost += "\n"
    vhost += "  <Directory \"{}\">\n".format(path)
    vhost += "	Options -Indexes +FollowSymLinks +ExecCGI\n"
    vhost += "	DirectoryIndex {}\n".format(index)
    vhost += "	AllowOverride all\n"
    vhost += "	Require all granted\n"
    vhost += "  </Directory>\n"
    vhost += "</VirtualHost>\n"

    with open(VHOST_DIR+name+".conf", "w") as text_file:
        text_file.write(vhost)

