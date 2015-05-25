#!/bin/sh
#***************************Author Anuradha.wickramasinghe@bt.com ,anwickramasinghe@virtusa.com*********#
path=/wls_domains/<domain name>/anuradha
. $path/domains.properties

echo "<br><br>" >> $path/throtling.txt
echo "<h2>Throtlling Status For Fault Tracker</h2>" >> $path/throtling.txt
echo "<table border="1" class="demo"><tr><th>Managed Sever</th><th>Throtling Count</th></tr>" >> $path/throtling.txt
echo "<tr><td>MS_01</td><td align=left>`curl $ot_url_1`</td></tr>" >> $path/throtling.txt
echo "<tr><td>MS_02</td><td align=left>`curl $ot_url_2`</td></tr>" >> $path/throtling.txt
echo "<tr><td>MS_03</td><td align=left>`curl $ot_url_3`</td></tr>" >> $path/throtling.txt
echo "<tr><td>MS_04</td><td align=left>`curl $ot_url_4`</td></tr>" >> $path/throtling.txt
echo "<tr><td>MS_05</td><td align=left>`curl $ot_url_5`</td></tr>" >> $path/throtling.txt
echo "<tr><td>MS_06</td><td align=left>`curl $ot_url_6`</td></tr>" >> $path/throtling.txt
echo "<tr><td>MS_07</td><td align=left>`curl $ot_url_7`</td></tr>" >> $path/throtling.txt
echo "<tr><td>MS_08</td><td align=left>`curl $ot_url_8`</td></tr>" >> $path/throtling.txt
echo "<tr><td>MS_09</td><td align=left>`curl $ot_url_9`</td></tr>" >> $path/throtling.txt
echo "</table>" >> $path/throtling.txt

echo "<br><br>" >> $path/throtling.txt 
echo "<h2>Throtlling Status For Order Tracker</h2>" >> $path/throtling.txt
echo "<table border="1" class="demo"><tr><th>Managed Sever</th><th>Throtling Count</th></tr>" >> $path/throtling.txt
echo "<tr><td>MS_01</td><td align=left>`curl $ft_url_1`</td></tr>" >> $path/throtling.txt
echo "<tr><td>MS_02</td><td align=left>`curl $ft_url_2`</td></tr>" >> $path/throtling.txt
echo "<tr><td>MS_03</td><td align=left>`curl $ft_url_3`</td></tr>" >> $path/throtling.txt
echo "<tr><td>MS_04</td><td align=left>`curl $ft_url_4`</td></tr>" >> $path/throtling.txt
echo "<tr><td>MS_05</td><td align=left>`curl $ft_url_5`</td></tr>" >> $path/throtling.txt
echo "<tr><td>MS_06</td><td align=left>`curl $ft_url_6`</td></tr>" >> $path/throtling.txt
echo "<tr><td>MS_07</td><td align=left>`curl $ft_url_7`</td></tr>" >> $path/throtling.txt
echo "<tr><td>MS_08</td><td align=left>`curl $ft_url_8`</td></tr>" >> $path/throtling.txt
echo "<tr><td>MS_09</td><td align=left>`curl $ft_url_9`</td></tr>" >> $path/throtling.txt
echo "</table>" >> $path/throtling.txt

echo "</body>" >> $path/throtling.txt
echo "</html>" >> $path/throtling.txt

