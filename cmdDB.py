#!/usr/bin/env python

cmd_remote = ""

user = {root: [cmdR1, cmdR2, cmdR3, cmdR_list_rpms],
				cloud_user: [cmd1, cmd2, cmd3, cmd_list_rpms]}



cmdR_list_rpms = "ssh root@192.168.122.105 \
	'ls -l ~/rpmbuild/RPMS/'"

cmd_list_rpms = "ssh cloud-user@192.168.122.105 \
	'ls -l ~/rpmbuild/RPMS/'"
	
# regular user -- system policy
cmd1 = "ssh cloud-user@192.168.122.105 \
	'rpm -q pkgconfig \
	2> ~/Documents/Logs/pkg-inst/pkg-config-err.log \
	|tee ~Documents/Logs/pkg-inst/pkg-config-out.log;'"

cmd2 = "ssh cloud-user@192.168.122.105 \
	'ls ~/Documents/Logs/pkg-inst/'"

cmd3 = "ssh cloud-user@192.168.122.105 \
	'ls -R ~/rpmbuild/'|less -S"

cmd4 = "ssh cloud-user@192.168.122.105 \
	'cd ~/rpmbuild/SPECS/ && \
	rpmbuild --short-circuit -v -bp \
	--target=`uname -m` ckb-next.spec \
	2> ~/Documents/Logs/ckb-prepare-err.log \
	|tee ~/Documents/Logs/ckb-prepare-out.log';"
	
cmd_proto = (cmd_connect, cmd_string)

cmd_string = 
["'ls ~/Documents/Logs/pkg-inst/'", 
 "list of remote commands"]
