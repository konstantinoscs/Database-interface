# -*- coding: utf-8 -*-
import pymysql.cursors
from bottle import route
from connection import *


def find_song(title, year, company):

    con = connection()
    try:
        with con.cursor() as cursor:
            sql = "select `title` from `tragoudi`, `singer_prod`, `cd_production` " \
                  "where `titlos` = `title` and `title` = %s and `etos_par` = %s and `etaireia` = %s and `cd` = `code_cd`"
            cursor.execute(sql, (title, year, company))
            data = cursor.fetchall()
            for row in data:
                print (str(row))

    finally:
        con.close()

    return data


def create_table(data):
    st='<meta charset = "utf-8"/> <table style=" ">'
    for row in data:
        st += "<tr>"
        st += "<td>" + str(row) + "</td>"
        st += "</tr>"
    st += "</table>"

    return st

def qq(tuples):
    header = '<tr><th>' + '</th><th>'.join([str(x) for x in tuples[0]]) + '</th></tr>'

    printResult = header + "</table>"
    return printResult