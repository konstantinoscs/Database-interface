# -*- coding: utf-8 -*-

from connection import *
from bottle import get, post, request

@get('/edit_artist/<nid>')
def edit(nid):
    st = find_and_fill(nid)
    return st

@post('/edit_artist/<nid>')
def submit(nid):
    nat_id = nid
    name = request.forms.getunicode('Name')
    surname = request.forms.getunicode('Surname')
    byear = request.forms.getunicode('Byear')
    update_artist(nat_id, name, surname, byear)
    st = render_success()
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
    <form method="POST" action="/edit_artist/'''
    st += nid
    st += '''"><table style=" ">
    <tr><td>Name</td>
    <td><input type="text" name="Name" value="'''
    st += data[0].encode('utf-8')
    st += '''"</td></tr>
    <tr><td>Surname</td>
    <td><input type="text" name="Surname" value="'''
    st += data[1].encode('utf-8')
    st += '''"</td></tr>
        <tr><td>Birth Year</td>
        <td><input type="text" name="Byear" value="'''
    st += str(data[2])
    st += '''"</td></tr>
    <tr><td></td>
    <td><input type="submit" value="Update Information"> </td>
    </table></form>'''

    return st


def update_artist(nat_id, name, surname, byear):

    con = connection()

    try:
        with con.cursor() as cursor:
            sql = '''update `kalitexnis`
            set `onoma` = %s, `epitheto` = %s, `etos_gen` = %s
            where `ar_taut` = %s'''
            cursor.execute(sql, (name, surname, byear, nat_id))
            con.commit()
    finally:
        con.close()

    return True


def render_success():
    st = '''<meta charset = "utf-8"/>
            <h1>Database updated successfully!</h1>
            <form action="/update_n_search">
            <input type="submit" value="Search and update new artist">
            </form>
            <form action="/">
            <input type="submit" value="Main menu">
            </form>
            '''
    return st
