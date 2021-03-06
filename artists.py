# -*- coding: utf-8 -*-

from connection import connection
from edit_artist import *


def find_artists(name, surname, byear_from, byear_to, ptype):
    con = connection()

    if ( byear_from != "") :
        byear_from = int(byear_from)

    if ( byear_to != "") :
        byear_to = int(byear_to)

    try:
        with con.cursor() as cursor:
            sql = "select distinct(`ar_taut`), `onoma`, `epitheto`, `etos_gen` "

            if ( ptype == 'Singer'):
                sql += "from `kalitexnis`, `singer_prod` " \
                       "where `ar_taut` = `tragoudistis` "
            elif ( ptype == 'SongWriter' ):
                sql += "from `kalitexnis`, `tragoudi` " \
                       "where `ar_taut` = `stixourgos` "
            elif ( ptype == 'Composer'):
                sql += "from `kalitexnis`, `tragoudi` " \
                       "where `ar_taut` = `sinthetis` "

            counter = 0
            if (name != ""):
                sql += " and `onoma` = %s "
                counter += 1
            if (surname != ""):
                sql += " and `epitheto` = %s "
                counter += 2
            if (byear_from != ""):
                sql += " and `etos_gen` > %s "
                counter += 4
            if (byear_to != ""):
                sql += " and `etos_gen` < %s "
                counter += 8

            if (counter == 0):
                cursor.execute(sql)
            elif (counter == 15):
                cursor.execute(sql, (name, surname, byear_from, byear_to))
            elif (counter == 1):
                cursor.execute(sql, (name))
            elif (counter == 2):
                cursor.execute(sql, (surname))
            elif (counter == 4):
                cursor.execute(sql, (byear_from))
            elif (counter == 8 ):
                cursor.execute(sql, (byear_to))
            elif (counter == 3):
                cursor.execute(sql, (name, surname))
            elif (counter == 5):
                cursor.execute(sql, (name, byear_from))
            elif (counter == 9):
                cursor.execute(sql, (name, byear_to))
            elif (counter == 6):
                cursor.execute(sql, (surname, byear_from))
            elif (counter == 10):
                cursor.execute(sql, (surname, byear_to))
            elif (counter == 12):
                cursor.execute(sql, (byear_from, byear_to))
            elif (counter == 7):
                cursor.execute(sql, (name, surname, byear_from))
            elif (counter == 11):
                cursor.execute(sql, (name, surname, byear_to))
            elif (counter == 14):
                cursor.execute(sql, (surname, byear_from, byear_to))
            elif (counter == 13):
                cursor.execute(sql, (name, byear_from, byear_to))

            data = cursor.fetchall()
    finally:
        con.close()

    return data


def render_artists_table(data):
    st = '''<!DOCTYPE html>
        <head><meta charset="UTF-8">
        <style>
        td{
        text-align:center;
        }
        </style>
        </head>'''
    st += '''<body><h1>View Artist Results</h1><hr>
          <table>
          <tr><th>National Id</th>
          <th>Name</strong></th>
          <th>Surname</th>
          <th>Birth Year</th>
          <th>Edit?</th></tr>'''
    for row in data:
        st += "<tr>"
        nid = row[0].encode('utf-8')
        for i in row:
            st += "<td>"
            if isinstance(i, int):
                st += str(i)
            else:
                if i == '':
                    st += '-'
                else:
                    st += i.encode('utf-8')
            st += "</td>"
        st += '<td><form method="GET" action="/edit_artist/'
        st += nid
        st += '" vertical-align="middle"><input type="submit" value="Edit Me!"></form></td>'
        st += "</tr>"
    st += "</table><hr></body>"

    return st
