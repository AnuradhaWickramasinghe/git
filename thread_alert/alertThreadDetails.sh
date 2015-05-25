#!/bin/sh

#Change the environment variables below to suit your target environment
#The WLST_OUTPUT_PATH and WLST_OUTPUT_FILE environment variables in this script 
#determine the output directory and file of the script
#The WLST_OUTPUT_PATH directory value must have a trailing slash. If there is no trailing slash 
#script will error and not continue.

#***************************Author Anuradha.wickramasinghe@bt.com ,anwickramasinghe@virtusa.com*********#

WL_HOME=/software/bea/Middleware/wls/10.3.6/wlserver_10.3
DOMAIN_HOME=/wls_domains/<domain name>; export DOMAIN_HOME
WLST_OUTPUT_PATH=/wls_domains/<domain name>/anuradha/; export WLST_OUTPUT_PATH
WLST_OUTPUT_FILE=WLST_Thread_Alert.html; export WLST_OUTPUT_FILE
WLST_OUTPUT_PATH2=/wls_domains/<domain name>/anuradha; export WLST_OUTPUT_PATH2
${WL_HOME}/common/bin/wlst.sh $WLST_OUTPUT_PATH2/test5.py

#sh $WLST_OUTPUT_PATH2/writeThrotling.sh

#cat $WLST_OUTPUT_PATH2/WLST_MBean_Config_Summary.html $WLST_OUTPUT_PATH2/throtling.txt > $WLST_OUTPUT_PATH2/Final.html

#SUBJECT="Monitoring Dash Board for Weblogic Domain 1"
#### Sending mail ####################
#export MAILTO="akw8888@gmail.com"
#export MAILTO="akw8888@gmail.com"
#export MAILFROM="donotreply@bt.com"
#export CONTENT="$WLST_OUTPUT_PATH2/WLST_MBean_Config_Summary.html"
#export CONTENT="$WLST_OUTPUT_PATH/Final.html"
#export SUBJECT="$SUBJECT - $DATE BST"
#(
#        echo "From:$MAILFROM"
#        echo "To:$MAILTO"
#        echo "Subject: $SUBJECT"
#        echo "MIME-Version: 1.0"
#        echo "Content-Type: text/html"
#        cat ${CONTENT}
#        echo $signature 
#)| /usr/sbin/sendmail $MAILTO

#sleep 20
#cat /dev/null > $WLST_OUTPUT_PATH2/throtling.txt 
#cat /dev/null > $WLST_OUTPUT_PATH2/WLST_MBean_Config_Summary.html
#cat /dev/null > $WLST_OUTPUT_PATH2/Final.html


