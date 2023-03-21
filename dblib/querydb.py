import os
import json
from databricks import sql

#ESTABLISH THE CONNECTION TO THE DATABASE
def querydb(query="SELECT * FROM hive_metastore.default.covid_19 LIMIT 2"):
    with sql.connect(
        server_hostname="adb-4595415223479783.3.azuredatabricks.net",
        http_path="sql/protocolv1/o/4595415223479783/0207-153520-2sxkrahk",
        access_token="dapib61430e28b3bb12ad55ccf40068f45d2-3",
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result

#QUERY THE AVERAGE DEATHS BY LOCATION
def queryDeathsByLocation(location):
    querysentence= "SELECT Deaths FROM hive_metastore.default.covid_19 where Country=\'"+location+"\';"
    queryres=querydb(querysentence)
    average=calAvg(queryres)
    return average

#QUERY THE AVERAGE CONFIRMED BY LOCATION
def queryConfirmedByLocation(location):
    querysentence= "SELECT Confirmed FROM hive_metastore.default.covid_19 where Country=\'"+location+"\';"
    queryres=querydb(querysentence)
    average=calAvg(queryres)
    return average

#QUERY THE AVERAGE RECOVERED BY LOCATION
def queryRecoveredByLocation(location):
    querysentence= "SELECT Recovered FROM hive_metastore.default.covid_19 where Country=\'"+location+"\';"
    queryres=querydb(querysentence)
    average=calAvg(queryres)
    return average

#QUERY THE
def calAvg(list):
    sum = 0
    for row in list:
        sum += int(row["Deaths"])
    return round(sum / len(list), 2)