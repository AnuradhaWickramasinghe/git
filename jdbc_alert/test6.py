#***************************Author Anuradha.wickramasinghe@bt.com ,anwickramasinghe@virtusa.com*********#
from java.io import FileInputStream
import string
import java.lang
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import os

def writeCss():

        print >>f, "<style type=\"text/css\">"
        print >>f, "table.demo"
        print >>f, "{"
        print >>f, "font-size: 16px;"
        print >>f, "border: 1px solid #0000C0;"
        print >>f, "}"

	print >>f, ".right"
	print >>f, "{"
	print >>f, "position: absolute;"
	print >>f, "right: 0px;"
	print >>f, "width: 500px;"
	print >>f, "background-color: #b0e0e6;"
	print >>f, "}"

        print >>f, "table.demo th"
        print >>f, "{"
        print >>f, "font-weight: bold;"
        print >>f, "background-color: #6A5ACD;"
	print >>f, "padding: 2px 5px 2px 5px;"
        print >>f, "}"

        print >>f, "table.demo td"
        print >>f, "{"
        print >>f, "font-size: 15px;"
        print >>f, "padding: 2px 5px 2px 5px;"
	print >>f, "border-top: 0px  #151515;"
	print >>f, "background-color: #FFFFF;"
        print >>f, "}"

        print >>f, "tr.row1"
        print >>f, "{"
        print >>f, "background-color: #E0E0FF;"
        print >>f, "}"

        print >>f, "tr.row2"
        print >>f, "{"
        print >>f, "background-color: #E0E0FF;"
        print >>f, "}"

        print >>f, "tr.hl"
        print >>f, "{"
        print >>f, "color: #808080;"
        print >>f, "font-weight: bold;"
        print >>f, "}"
        print >>f, "</style>"



propInputStream = FileInputStream("/wls_domains/ptlorr01/anuradha/domains.properties")
configProps = Properties()
configProps.load(propInputStream)

adminUrl = configProps.get("admin.url")
adminUser = configProps.get("admin.username")
adminPassword = configProps.get("admin.password")

# The recommendation is to stick this script off from a wrapper os script e.g cmd (Windows) or .sh (Unix)
v_domainHome = os.environ["DOMAIN_HOME"];
v_outputFilePath = os.environ["WLST_OUTPUT_PATH"];
v_outputFile = os.environ["WLST_OUTPUT_FILE"];


connect(adminUser,adminPassword,adminUrl)
f = open(v_outputFilePath  + v_outputFile, 'w');
print >>f, "<html>"
print >>f, "<head>"
writeCss()
print >>f, "<link href=\"tabledemo.css\" type=\"text/css\" rel=\"stylesheet\">"
print >>f, "</head>"
print >>f, "<body bgcolor=#FFFFF>"

print >>f, "<br><h3 bgcolor=#FF0000>JDBC Numbers of Connections near to reach threshold</h3></br>"
print >>f, "<div class=\"right\">"
print >>f, "<table id=\"my_TopLevelDomain_Table\" border=\"1\" class=\"demo\">"
print >>f, "<thead align=\"left\">"
print >>f, "<tr>"
print >>f, "<th>Server Name</th>"
print >>f, "<th>Data Ssource Name</th>"
print >>f, "<th>Active Connection AVG</th>"
print >>f, "<th>Active Connection Current</th>"
print >>f, "<th>Active Connection High</th>"
print >>f, "</tr>"
print >>f,"</thead>"
print >>f, "<tbody>"


############  This method would send the Alert Email  #################
def sendMailString():

	os.system("mailx -s \"$(echo -e \"Threads Got Stuck \nContent-Type: text/html\")\" anuradha.wickramasinghe@bt.com < /wls_domains/ptlorr01/anuradha/JDBC_ALERT.html")
def getSize(filename):
    st = os.stat(filename)
    return st.st_size

def getDataSourceupdate():
        servers=domainRuntimeService.getServerRuntimes()
        for server in servers:
                try:
                        jdbcServiceRT = server.getJDBCServiceRuntime();
                        dataSources = jdbcServiceRT.getJDBCDataSourceRuntimeMBeans();
                        if (len(dataSources) > 0):
                                for dataSource in dataSources:
                                        activeConnectionsAverageCount=dataSource.getActiveConnectionsAverageCount();
                                        activeConnectionsCurrentCount=dataSource.getActiveConnectionsCurrentCount();
                                        activeConnectionsHighCount=dataSource.getActiveConnectionsHighCount();
                                        name=dataSource.getName();
                                        serverName=server.getName();
					
					if(activeConnectionsCurrentCount <= activeConnectionsHighCount-2 or activeConnectionsCurrentCount == 0):	

                                        	print "Noerror"
					else:
						print >>f, "<tr>"
                                        	print >>f, "<td>"
                                        	print >>f, serverName;
                                        	print >>f, "</td>"

                                        	print >>f, "<td>"
                                        	print >>f, name;
                                        	print >>f, "</td>"

                                        	print >>f, "<td>"
                                        	print >>f, activeConnectionsAverageCount;
                                        	print >>f, "</td>"

                                        	print >>f, "<td bgcolor=#DA70D6 font-weight: bold><center>"
                                        	print >>f, activeConnectionsCurrentCount;
                                       	 	print >>f, "</center></td>"

                                        	print >>f, "<td>"
                                        	print >>f, activeConnectionsHighCount;
                                        	print >>f, "</td>"
                                        	print >>f, "</tr>"


                except WLSTException,e:
                        # this typically means the server is not active, just ignore
                       print e
                        #pass

        print >>f, "</tbody></table>"
	print >>f, "</div>"
	print >>f, "<br>"
	print >>f, "</body></html>"

if __name__== "main":
        
        getDataSourceupdate()
	size=getSize("/wls_domains/ptlorr01/anuradha/JDBC_ALERT.html");
        print size
        if size > 1020 :
                sendMailString()
	#print >>f, "</tbody></table>"
	#print >>f, "</div>"
        #print >>f, "<br>"
	#print >>f, "</body></html>"
        f.close();


