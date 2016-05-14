import pymysql.cursors
from bottle import route
from connection import *


def find_song(title, year, company):

    con = connection()
    try:
        with con.cursor() as cursor:
            sql = "select `*` from `tragoudi`, `singer_prod`, `cd_production` " \
                  "where `titlos` = `title` and `title` = %s and `etos_par` = %s and `etaireia` = %s"
            cursor.execute(sql, (title, year, company))
            data = cursor.fetchall()

    finally:
        con.close()

    return data


def create_table(data):
    str="<table style=" ">"
    for row in data:
        str+="<tr>"
        for i in row[0]:
            str+="<td>" + str(i) + "</td>"
        str +="</tr>"
    str += "</table>"

    return str

def qq(tuples):
    header = '<tr><th>' + '</th><th>'.join([str(x) for x in tuples[0]]) + '</th></tr>'

    printResult += header + "</table>"
    return printResult