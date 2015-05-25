#!/bin/sh

#Change the environment variables below to suit your target environment
#The WLST_OUTPUT_PATH and WLST_OUTPUT_FILE environment variables in this script 
#determine the output directory and file of the script
#The WLST_OUTPUT_PATH directory value must have a trailing slash. If there is no trailing slash 
#script will error and not continue.

#***************************Author Anuradha.wickramasinghe@bt.com ,anwickramasinghe@virtusa.com*********#

WL_HOME=/software/bea/Middleware/wls/10.3.6/wlserver_10.3
DOMAIN_HOME=/wls_domains/ptlorr01; export DOMAIN_HOME
WLST_OUTPUT_PATH=/wls_domains/ptlorr01/anuradha/; export WLST_OUTPUT_PATH
WLST_OUTPUT_FILE=JDBC_ALERT.html; export WLST_OUTPUT_FILE
WLST_OUTPUT_PATH2=/wls_domains/ptlorr01/anuradha; export WLST_OUTPUT_PATH2
${WL_HOME}/common/bin/wlst.sh $WLST_OUTPUT_PATH2/test6.py

#sh $WLST_OUTPUT_PATH2/writeThrotling.sh

#cat $WLST_OUTPUT_PATH2/WLST_MBean_Config_Summary.html $WLST_OUTPUT_PATH2/throtling.txt > $WLST_OUTPUT_PATH2/Final.html

#SUBJECT="Monitoring Dash Board for Weblogic Domain 1"
#### Sending mail ####################
#export MAILTO="BT-ASG-ORPGOffshoreteam@virtusa.com,anuradha.wickramasinghe@bt.com"
#export MAILTO="anuradha.wickramasinghe@bt.com"
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


