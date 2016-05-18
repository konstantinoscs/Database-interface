# -*- coding: utf-8 -*-
import pymysql.cursors
from bottle import route
from connection import *


def find_song(title, year, company):
    if (year != ""):
        year = int(year)
    con = connection()
    try:
        with con.cursor() as cursor:
            if (title != "") and (year != "") and (company != ""):
                sql = "select `titlos`, `sinthetis`, `etos_par`, `stixourgos` " \
                      "from `tragoudi`, `singer_prod` as `sp`, `group_prod` as `gp`, `cd_production` " \
                      "where ( ( `titlos` = `sp`.`title` and `sp`.`cd` = `code_cd` ) or " \
                      "( `titlos` = `gp`.`title` and `gp`.`cd` = `code_cd` ) ) " \
                      "and `titlos` = %s and `etos_par` = %s and" \
                      " `etaireia` = %s " \
                      "group by `titlos`"
                cursor.execute(sql, (title, year, company))
            elif (title != "") and (year != "") and (company == ""):
                sql = "select `titlos`, `sinthetis`, `etos_par`, `stixourgos` " \
                      "from `tragoudi` " \
                      "where `titlos` = %s and `etos_par` = %s " \
                      "group by `titlos`"
                cursor.execute(sql, (title, year))
            elif (title != "") and (year == "") and (company != ""):
                sql = "select `titlos`, `sinthetis`, `etos_par`, `stixourgos` " \
                      "from `tragoudi`, `singer_prod` as `sp`, `group_prod` as `gp`, `cd_production` " \
                      "where ( ( `titlos` = `sp`.`title` and `sp`.`cd` = `code_cd` ) or " \
                      "( `titlos` = `gp`.`title` and `gp`.`cd` = `code_cd` ) ) " \
                      "and `titlos` = %s and" \
                      " `etaireia` = %s " \
                      "group by `titlos`"
                cursor.execute(sql, (title, company))
            elif (title != "") and (year == "") and (company == ""):
                sql = "select `titlos`, `sinthetis`, `etos_par`, `stixourgos` " \
                      "from `tragoudi` " \
                      "where `titlos` = %s " \
                      "group by `titlos`"
                cursor.execute(sql, (title))
            elif (title == "") and (year != "") and (company != ""):
                sql = "select `titlos`, `sinthetis`, `etos_par`, `stixourgos` " \
                      "from `tragoudi`, `singer_prod` as `sp`, `group_prod` as `gp`, `cd_production` " \
                      "where ( ( `titlos` = `sp`.`title` and `sp`.`cd` = `code_cd` ) or " \
                      "( `titlos` = `gp`.`title` and `gp`.`cd` = `code_cd` ) ) " \
                      "and `etos_par` = %s and" \
                      " `etaireia` = %s " \
                      "group by `titlos`"
                cursor.execute(sql, (year, company))
            elif (title == "") and (year != "") and (company == ""):
                sql = "select `titlos`, `sinthetis`, `etos_par`, `stixourgos` " \
                      "from `tragoudi` " \
                      "where `etos_par` = %s "
                cursor.execute(sql, (year))
            elif (title == "") and (year == "") and (company != ""):
                sql = "select `titlos`, `sinthetis`, `etos_par`, `stixourgos` " \
                      "from `tragoudi`, `singer_prod` as `sp`, `group_prod` as `gp`, `cd_production` " \
                      "where ( ( `titlos` = `sp`.`title` and `sp`.`cd` = `code_cd` ) or " \
                      "( `titlos` = `gp`.`title` and `gp`.`cd` = `code_cd` ) ) " \
                      "and `etaireia` = %s " \
                      "group by `titlos`"
                cursor.execute(sql, (company))
            elif (title == "") and (year == "") and (company == ""):
                sql = "select `titlos`, `sinthetis`, `etos_par`, `stixourgos` " \
                      "from `tragoudi` " \
                      "group by `titlos`"
                cursor.execute(sql)

            data = cursor.fetchall()

    finally:
        con.close()

    return data


def create_table(data):
    st = '<meta charset = "utf-8"/> <table style=" ">'
    st += '''<tr><td><strong>Τίτλος</strong></td>
    <td><strong>Συνθέτης</strong></td>
    <td><strong>Ετος παραγωγής</strong></td>
    <td><strong>Στιχουργός</strong></td></tr>'''
    for row in data:
        st += "<tr>"
        for i in row:
            st += "<td>"
            if isinstance(i, int):
                st += str(i)
            else:
                st += i.encode('utf-8')
            st += "</td>"
        st += "</tr>"
    st += "</table>"

    return st

