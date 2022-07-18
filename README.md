# Test_Route_SE
It is the script in python, that can process the KML datafile, passed to the script as a parameter, read the coordinates and filter out the incorrect data points.

<p>In the terminal, go to the folder where you want to save files from Github. Next, enter the command<br />"<em><strong>git clone https://github.com/mikhalchukvladislav/Test_Route_SE.git</strong> </em>"</p>
<p>Enter the command in the terminal:"<em><strong>pip install -r requirements.txt</strong> </em>". You will install the necessary libraries for the project.</p>
<p>To run the script, you need to run it using the command "<em><strong>python main.py</strong></em> ".</p>
<p>After launching, the terminal will ask you to insert the path to the file with coordinates. <em><strong>Example of a path: C:/Users/Vladislav/Desktop/PYTHON/Test_Route_SE/Test_Route_SE/task_2_sensor.kml</strong></em> (note that you need to use the right slash '/' in the path).</p>
<p>The script is based on calculating the distance using the haversine formula between coordinates that have been processed and cleared of outliers. The orthodromic distance is used to calculate the shortest distance between two points of latitude and longitude on the earth's surface.</p>
<p>Cleaning from emissions is carried out according to the following principle:</p>
<ul>
<li>calculation of the distance between consecutive points;</li>
<li>search for outliers when the distance between neighboring points is more than 30 meters. This distance is calculated based on the construction of graphs;</li>
<li>removing duplicates, cleaning points with coordinates that have outliers.</li>
</ul>
<p><strong>After clearing the data with coordinates, the script calculates the sum of the distances between all coordinates and builds a graph.</strong></p>
<p></p>
<p>&nbsp;</p>
<p></p>
<p>&nbsp;</p>