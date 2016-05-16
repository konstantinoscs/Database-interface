# -*- coding: utf-8 -*-

from connection import connection


def find_artists(name, surname, byear_from, byear_to, ptype):
    con = connection()

    try:
        with con.cursor() as cursor:
            sql = "select `ar_taut`, `onoma`, `epitheto`, `etos_gen` from `kalitexnis`" \
                  "where `onoma` = %s and `epitheto` = %s and " \
                  "`etos_gen` > %s and `etos_gen` < %s"
            cursor.execute(sql, (name, surname, byear_from, byear_to))
            data = cursor.fetchall()
    finally:
        con.close()

    return data


def render_artists_table(data):
    st = '<meta charset = "utf-8"/>'
    st += "<h1>View Artist Results</h1><hr>" \
          "<table style=" ">" \
          "<tr><td><strong>National Id</strong></td>" \
          "<td><strong>Name</strong></td>" \
          "<td><strong>Surname</strong></td>" \
          "<td><strong>Birth Year</strong></td>" \
          "<td><strong>Edit?</strong></td></tr>"
    for row in data:
        st += "<tr>"
        for i in row:
            st += "<td>"
            if isinstance(i, int):
                st += str(i)
            else:
                st += i.encode('utf-8')
            st += "</td>"
        st += "<td>button</td>"
        st += "</tr>"
    st += "</table><hr>"

    return st