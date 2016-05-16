# -*- coding: utf-8 -*-
import pymysql.cursors
from bottle import route
from connection import *


def find_song(title, year, company):

    con = connection()
    try:
        with con.cursor() as cursor:
            if (title is not None)and (year is not None) and (company is not None):
                sql = "select `titlos`, `sinthetis`, `etos_par`, `stixourgos` " \
                      "from `tragoudi`, `singer_prod`, `cd_production` " \
                      "where `titlos` = `title` and `title` = %s and `etos_par` = %s and" \
                      " `etaireia` = %s and `cd` = `code_cd`" \
                      "group by `titlos`"
                cursor.execute(sql, (title, year, company))
            elif (title is not None) and (year is not None) and (company is None):
                sql= "select `titlos`, `sinthetis`, `etos_par`, `stixourgos` " \
                      "from `tragoudi` " \
                      "where `titlos` = %s and `etos_par` = %s " \
                      "group by `titlos`"
                cursor.execute(sql, (title, year))
            elif (title is not None)and (year is None) and (company is not None):
                sql = "select `titlos`, `sinthetis`, `etos_par`, `stixourgos` " \
                      "from `tragoudi`, `singer_prod`, `cd_production` " \
                      "where `titlos` = `title` and `title` = %s and" \
                      " `etaireia` = %s and `cd` = `code_cd`" \
                      "group by `titlos`"
                cursor.execute(sql, (title, company))
            elif (title is not None)and (year is None) and (company is None):
                sql = "select `titlos`, `sinthetis`, `etos_par`, `stixourgos` " \
                      "from `tragoudi` " \
                      "where `titlos` = %s " \
                      "group by `titlos`"
                cursor.execute(sql, (title))
            elif (title is None)and (year is not None) and (company is not None):
                sql = "select `titlos`, `sinthetis`, `etos_par`, `stixourgos` " \
                      "from `tragoudi`, `singer_prod`, `cd_production` " \
                      "where `titlos` = `title` and `etos_par` = %s and" \
                      " `etaireia` = %s and `cd` = `code_cd`" \
                      "group by `titlos`"
                cursor.execute(sql, (year, company))
            elif (title is None)and (year is not None) and (company is None):
                sql = "select `titlos`, `sinthetis`, `etos_par`, `stixourgos` " \
                      "from `tragoudi` " \
                      "where `etos_par` = %s and" \
                      "group by `titlos`"
                cursor.execute(sql, (year))
            elif (title is None)and (year is None) and (company is not None):
                sql = "select `titlos`, `sinthetis`, `etos_par`, `stixourgos` " \
                      "from `tragoudi`, `singer_prod`, `cd_production` " \
                      "where `titlos` = `title` and" \
                      " `etaireia` = %s and `cd` = `code_cd`" \
                      "group by `titlos`"
                cursor.execute(sql, (company))
            elif (title is None)and (year is None) and (company is None):
                sql = "select `titlos`, `sinthetis`, `etos_par`, `stixourgos` " \
                      "from `tragoudi` " \
                      "group by `titlos`"
                cursor.execute(sql)

            data = cursor.fetchall()

    finally:
        con.close()

    return data


def create_table(data):
    st='<meta charset = "utf-8"/>'
    st+='''<div>
    <div style="font-size:200%;"><strong>Presentation of Songs-Results</strong></div>
    <br>
    <fieldset>
    <table style="">
    <tr>
    <td><strong>Τίτλος</strong></td>
    <td><strong>Συνθέτης</strong></td>
    <td><strong>Ετος παραγωγής</strong></td>
    <td><strong>Στιχουργός</strong></td>
    </tr>'''
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
    st += "</fieldset>"
    st += "</div>"

    return st

