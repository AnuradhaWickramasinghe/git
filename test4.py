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
        print >>f, "font-size: 13px;"
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
        print >>f, "background-color: #C0C0FF;"
	print >>f, "padding: 2px 5px 2px 5px;"
        print >>f, "}"

        print >>f, "table.demo td"
        print >>f, "{"
        print >>f, "font-size: 12px;"
        print >>f, "padding: 2px 5px 2px 5px;"
	print >>f, "border-top: 0px  #151515;"
	print >>f, "background-color: #FFFFFF;"
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



propInputStream = FileInputStream("/wls_domains/cbptlorp01/anuradha/domains.properties")
configProps = Properties()
configProps.load(propInputStream)

adminUrl = configProps.get("admin.url")
adminUser = configProps.get("admin.username")
adminPassword = configProps.get("admin.password")

############  This method would send the Alert Email  #################
def sendMailString():

        os.system('/bin/mailx -s  "ALERT : Running Domain Thread Status  !!!  " anuradha.wickramasinghe@bt.com < WLST_MBean_Config_Summary.html')
        print '*********  ALERT MAIL HAS BEEN SENT  ***********'
        print ''

def alertIdleThreads(executeTTC , hoggerTC , idleTC , healthState , name):

         message =  'Server Name = ' + name + ' ExecuteThreads Count= ' + str(executeTTC) + '   HoggingThreads= '+ str(hoggerTC) + ' IdleThreads= '+ str(idleTC) + ' Health= '+ str(healthState)
         message2 = name +':'+ str(executeTTC)
         print message
         cmd = "echo " + message +" >> rw_file_thread_state"
         os.system(cmd)



# The recommendation is to stick this script off from a wrapper os script e.g cmd (Windows) or .sh (Unix)
v_domainHome = os.environ["DOMAIN_HOME"];
v_outputFilePath = os.environ["WLST_OUTPUT_PATH"];
v_outputFile = os.environ["WLST_OUTPUT_FILE"];

#print adminUser;
#print adminPassword;
#print adminUrl;


connect(adminUser,adminPassword,adminUrl)
f = open(v_outputFilePath  + v_outputFile, 'w');
print >>f, "<html>"
print >>f, "<head>"
writeCss()
print >>f, "<link href=\"tabledemo.css\" type=\"text/css\" rel=\"stylesheet\">"
print >>f, "</head>"
print >>f, "<body bgcolor=#FFFFF>"


print >>f, "<br><h3>Application Deployment Behavior</h3></br>"
print >>f, "<div class=\"left\">"
print >>f, "<table id=\"my_TopLevelApplication_Table\" border=\"1\" class=\"demo\">"
print >>f, "<thead align=\"left\">"
print >>f, "<tr>"
print >>f, "<th>Apllication Name</th>"
print >>f, "<th>currentState</th>"
print >>f, "</tr>"
print >>f,"</thead>"
print >>f, "<tbody>"

def test():
	cd ('AppDeployments')
	myapps=cmo.getAppDeployments()
	for appName in myapps:
		domainConfig()
		cd('/AppDeployments/'+appName.getName()+'/Targets')
		mytargets = ls(returnMap='true')
		domainRuntime()
		cd('AppRuntimeStateRuntime')
		cd('AppRuntimeStateRuntime')
		for targetinst in mytargets:
		        curstate4=cmo.getCurrentState(appName.getName(),targetinst)
			print >>f, "<tr>"
            		print >>f, "<td>"
			print >>f, str(appName.getName());
            		print >>f, "</td>"
			
			print >>f, "<td>"
			print >>f, str(curstate4);
            		print >>f, "</td>"
			print >>f, "</tr>"

def getThreadDetails():

         #domainRuntime()
         #cd('ServerRuntimes')
         servers=domainRuntimeService.getServerRuntimes()
         for server in servers:
                try:
                        cd('/ServerRuntimes/' + server.getName())
                        #print '##### Server State           #####', server.getState()
                        currentState = get('HealthState').getState()
                        #print '++++++ sever is : ' ,currentState
                        #print 'Now checking '+ server.getName()
                        cd('ThreadPoolRuntime/ThreadPoolRuntime')
                        executeTTC=cmo.getExecuteThreadTotalCount();
                        hoggerTC=cmo.getHoggingThreadCount();
                        idleTC=cmo.getExecuteThreadIdleCount();
                        healthState=cmo.getHealthState();
                        if "HEALTH" in str(healthState):
                               # alertIdleThreads(executeTTC,hoggerTC,idleTC,healthState,str(server.getName()));
                                print >>f, "<tr>"
                                print >>f, "<td>"
                                print >>f, str(server.getName());
                                print >>f, "</td>"

                                print >>f, "<td>"
                                print >>f, str(executeTTC);
                                print >>f, "</td>"

                                print >>f, "<td>"
                                print >>f, str(hoggerTC);
                                print >>f, "</td>"

                                print >>f, "<td>"
                                print >>f, str(idleTC);
                                print >>f, "</td>"

                                print >>f, "<td>"
                                print >>f, server.getState();
                                print >>f, "</td>"
                                print >>f, "</tr>"

                        else:
                        #       print "hello man"
                                break


                except WLSTException,e:
                # this typically means the server is not active, just ignore
                        print e
                        #pass


def getJmsDetails():
        #domainRuntime()
        servers=domainRuntimeService.getServerRuntimes()
        for server in servers:
                try:
                        jmsRuntime = server.getJMSRuntime();
                        jmsServers = jmsRuntime.getJMSServers();
                        for jmsServer in jmsServers:
                                destinations = jmsServer.getDestinations();
                                for destination in destinations:
                                        if destination.getMessagesCurrentCount() > 0:
                                                count=destination.getMessagesCurrentCount()
                                                dest = destination.getName()
                                                print >>f, "<tr>"
                                                print >>f, "<td>"
                                                print >>f, dest;
                                                print >>f, "</td>"

                                                print >>f, "<td>"
                                                print >>f, count;
                                                print >>f, "</td>"
                                                print >>f, "</tr>"

                except WLSTException,e:
                        # this typically means the server is not active, just ignore
                        print e
                        #passa

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
					
					print >>f, "<td>"
                    			print >>f, activeConnectionsCurrentCount;
                    			print >>f, "</td>"
					
					print >>f, "<td>"
                    			print >>f, activeConnectionsHighCount;
                    			print >>f, "</td>"
                    			print >>f, "</tr>"
					
		except WLSTException,e:
                	# this typically means the server is not active, just ignore
                	print e
                	#pass
			

if __name__== "main":
	test()
	print >>f, "</tbody></table>"
        print >>f, "</div>"
	print >>f, "<br>"

	print >>f, "<br><h3>Current Thread Behavior For The Running Managed Servers</h3></br>"
	print >>f, "<div class=\"right\">"
	print >>f, "<table id=\"my_TopLevelDomain_Table\" border=\"1\" class=\"demo\">"
	print >>f, "<thead align=\"left\">"
	print >>f, "<tr>"
	print >>f, "<th>Managed Server</th>"
	print >>f, "<th>Total TC</th>"
	print >>f, "<th>Hogger TC</th>"
	print >>f, "<th>Idle TC</th>"
	print >>f, "<th>Health State</th>"
	print >>f, "</tr>"
	print >>f,"</thead>"
	print >>f, "<tbody>"
	

        getThreadDetails()
        print >>f, "</tbody></table>"
	print >>f, "</div>"
        print >>f, "<br>"

        print >>f, "<br><h3>Current Jms Behavior</h3></br>"
        print >>f, "<table id=\"my_TopLevelDomain_Table\" border=\"1\" class=\"demo\">"
        print >>f, "<thead align=\"left\">"
        print >>f, "<tr>"
        print >>f, "<th>Jms Destination</th>"
        print >>f, "<th>Current Message Count</th>"
        print >>f, "</tr>"
        print >>f,"</thead>"
        print >>f, "<tbody>"

        getJmsDetails()
        print >>f, "</tbody></table>"
		
	print >>f, "<br>"

        print >>f, "<br><h3>JDBC DataSource Behavior</h3></br>"
        print >>f, "<table id=\"my_TopLevelDomain_Table\" border=\"1\" class=\"demo\">"
        print >>f, "<thead align=\"left\">"
        print >>f, "<tr>"
	print >>f, "<th>Mianaged Server</th>"
        print >>f, "<th>Data Source Name</th>"
        print >>f, "<th>activeConnectionsAverageCount</th>"
	print >>f, "<th>activeConnectionsCurrentCount</th>"
	print >>f, "<th>activeConnectionsHighCount</th>"
        print >>f, "</tr>"
        print >>f,"</thead>"
        print >>f, "<tbody>"
	getDataSourceupdate()
	print >>f, "</tbody></table>"
		
        f.close();


