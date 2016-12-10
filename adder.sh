#! /bin/bash

mysql --host=localhost --user=root --password=idam --execute="INSERT INTO testFarm (date, numBugs) VALUES ('$1',$2);" pestdata
