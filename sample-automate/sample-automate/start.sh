#!/bin/bash
cd /home/btasmtest/Desktop/anuradha/sample-automate
source ~/.bash_profile
mvn clean test > test.txt
cat test.txt | grep Running > testName.txt
cat test.txt | grep Tests > status.txt
paste -d"," testName.txt status.txt > finalReport.txt
cat finalReport.txt | awk '{print $2}' | cut -d "." -f4 | cut -d "," -f1  > NameTests.txt
cat finalReport.txt | awk '{print $4,$6,$8,$10,$13$14}' > stats.txt
paste -d"," NameTests.txt stats.txt | head -n -2 > united.csv

while read line
         do
         if [ "${line}" != "" ]; then
                TestCaseName=`echo $line | cut -d "," -f1`
                ran=`echo $line | cut -d "," -f2`
                failiers=`echo $line | cut -d "," -f3`
                errors=`echo $line | cut -d "," -f4`
		skipped=`echo $line | cut -d "," -f5`
                timeElapsed=`echo $line | cut -d "," -f6`
                echo $errors
                if [ $errors -eq 0 ]; then      
                echo "<tr><td>$TestCaseName</td><td align=left>$ran</td><td align=centre>$failiers</td><td>$errors</td><td>$skipped</td><td>$timeElapsed</td><td bgcolor="#00FF00">ok</td></tr>" >>tablebody.txt 
		elif [ $errors -eq 1 ]; then
		echo "<tr><td>$TestCaseName</td><td align=left>$ran</td><td align=centre>$failiers</td><td>$errors</td><td>$skipped</td><td>$timeElapsed</td><td bgcolor="#FF0000">fail</td></tr>" >>tablebody.txt
		fi
         else
                echo "test test"
         fi
         done<united.csv
echo "<html><head></head><body bgcolor='#FFFFCC'><br><h1 style='font-family:calibri;font-size:22;color:#000000'><b><i>Test Running status</i></b></h1><table border=2 bgcolor=#FFFFBC><thead><tr><th>Test Case Name</th><th>Running Status</th><th>Failiers</th><th>Errors</th><th>Skipped</th><th>Time Elapsed</th><th>Status</th></tr></thead><tbody>`cat tablebody.txt `</tbody></table></body></html>" > report.html
cp report.html /opt/apache-tomcat-7.0.29/webapps/upload/
rm tablebody.txt
