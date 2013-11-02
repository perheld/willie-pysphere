willie-pysphere
===============

This is a plugin for the IRC bot Willie to monitor and control virtual machines using the vSphere python API
Checkout https://code.google.com/p/pysphere/ for information about that
stuff and https://github.com/embolalia/willie/ for Willie

Just putting it here since somebody else might find it usefull as well.
Hopefully I will have the time to add more functions as I need them.

Configuration
===============
Add a section named [pysphere] in your config and add:

server = yourserver

login = yourlogin

password = yoursupersecretpassword

Commands
===============
.vmlist
Lists vms

.vmpoweron
power on a  vm

.vmpoweroff
power off a vm
