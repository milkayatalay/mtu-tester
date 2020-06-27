# mtu-tester
A tool for testing networks UDP MTU capabilities

## **Usage**
If you test UDP transport with existed server running mtu-tester.py alone enough for you. Otherwise you have to run listener.py at target machine.

you can use "--help" argument with modules for seeing example usage

### **mtu-tester:**
`mtu-tester.py <arg1:server ip:192.168.1.6> <arg2:server port:4444 > <arg3: message size:4500>`<br/><br/>
example:<br/>
`mtu-tester.py 192.168.1.6 4444 4500>`

### **listener:**
`listener.py <arg1:server ip:this system IP 192.168.1.6> <arg2:server port:4444 >`<br/><br/>
example:<br/>
`listener.py 192.168.1.6 4444`



