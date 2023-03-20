import os
import json
from databricks import sql


def querydb(query="SELECT * FROM hive_metastore.default.ds_salaries LIMIT 2"):
    with sql.connect(
        server_hostname="adb-4595415223479783.3.azuredatabricks.net",
        http_path="sql/protocolv1/o/4595415223479783/0207-153520-2sxkrahk",
        access_token="dapi74919ff0ef75c453467697aa388306af-3",
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result

def querySalaryofLevels(position):
    queryentrylevel = "SELECT salary_in_usd From hive_metastore.default.ds_salaries where job_title=\'"+position+"\' and experience_level=\'EN\' and employment_type=\'FT\' and company_location=\'US\';"
    querymediumlevel = "SELECT salary_in_usd From hive_metastore.default.ds_salaries where job_title=\'"+position+"\' and experience_level=\'MI\' and employment_type=\'FT\' and company_location=\'US\';"
    queryseniorlevel = "SELECT salary_in_usd From hive_metastore.default.ds_salaries where job_title=\'"+position+"\' and experience_level=\'SE\' and employment_type=\'FT\' and company_location=\'US\';"
    entryres = querydb(queryentrylevel)
    mediumres = querydb(querymediumlevel)
    seniorres = querydb(queryseniorlevel)
    entryAvg = calSalaryAvg(entryres)
    mediumAvg = calSalaryAvg(mediumres)
    seniorAvg = calSalaryAvg(seniorres)
    return [entryAvg, mediumAvg, seniorAvg]


def querySalaryByCurrency(currency):
    querysentence= "SELECT salary_in_usd FROM hive_metastore.default.ds_salaries where salary_currency=\'"+currency+"\';"
    queryres=querydb(querysentence)
    average_salary=calSalaryAvg(queryres)
    return average_salary

def calSalaryAvg(salarylist):
    sum = 0
    for salary in salarylist:
        sum += int(salary["salary_in_usd"])
    return round(sum / len(salarylist), 2)