import os
import json
from databricks import sql


def querydb(query="SELECT * FROM hive_metastore.default.covid_19_data_1 LIMIT 2"):
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


def queryByLocation(location):
    querysentence= "SELECT Deaths FROM hive_metastore.default.covid_19_data_1 where Country/Region=\'"+location+"\';"
    queryres=querydb(querysentence)
    average_salary=calAvg(queryres)
    return average_salary

def calAvg(list):
    sum = 0
    for row in list:
        sum += int(row["Deaths"])
    return round(sum / len(list), 2)