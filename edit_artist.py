# -*- coding: utf-8 -*-

from connection import *
from bottle import get

@get('/edit_artist/<nid>')
def edit(nid):
    st = find_and_fill(nid)
    return st


def find_and_fill(nid):

    con = connection()

    try:
        with con.cursor() as cursor:
            sql = '''select `onoma`, `epitheto`, `etos_gen` from kalitexnis
                where `ar_taut` = %s'''
            cursor.execute(sql, (nid))
            data = cursor.fetchone()
    finally:
        con.close()
        st = render_table(data, nid)
    return st


def render_table(data, nid):
    st = '''<meta charset = "utf-8"/>
    <h1>Update Artist Information</h1><hr>
    <form method="POST" action="/edit_artist'''
    st += nid
    st += '''
    "><table style=" ">
    <tr><td>Name</td>
    <td><input type="text" name="Name" value="'''
    st += data[0].encode('utf-8')
    st += '''
    "</td></tr>
    <tr><td>Name</td>
    <td><input type="text" name="Surame" value="'''
    st += data[1].encode('utf-8')
    st += '''
        "</td></tr>
        <tr><td>Name</td>
        <td><input type="text" name="Surname" value="'''
    st += str(data[2])
    st +='''
    "</td></tr>
    <tr><td></td>
    <td><input type="submit" value="Update Information"> </td>
    </table></form>'''

    return st

