# -*- coding: utf-8 -*-

import pymysql
from bottle import get, post, request
from connection import *


@get('/insert_artist')
def insert_artist_form():
    return '''
    <div>
        <div style="font-size:200%;"><strong>Insert Artist</strong></div>
        <br>
        <form method="POST" action="/insert_artist">
            <fieldset>
                <table style="">
                    <tr>
                        <td> <span align="left">National Id </span></td>
                        <td> <input align="right" type="text" name="National_id" required value=""> </td>
                    </tr>


                    <tr>
                        <td> <span align="left">Name</span></td>
                        <td> <input align="right" type="text" name="Name" required value=""> </td>
                    </tr>


                    <tr>
                        <td> <span align="letf">Surname</span></td>
                        <td> <input align="right" type="text" name="Surname" required value=""> </td>
                    </tr>


                    <tr>
                        <td> <span align="left">Birth Year</span></td>
                        <td> <input align="right" type="number" name="Birth_year" required min="1900" max="2016"> </td>
                    </tr>

                    <tr>
                        <td></td>
                        <td> <input type="submit" value="Update Information"> </td>
                    </tr>


                </table>
            </fieldset>
        </form>
    </div>
    '''


@post('/insert_artist')
def get_insert_artist():
    national_id = request.forms.getunicode('National_id')
    name = request.forms.getunicode('Name')
    surname = request.forms.getunicode('Surname')
    birth_year = request.forms.getunicode('Birth_year')
    birth_year = int(birth_year)
    insert_artist(national_id, name, surname, birth_year)

    st = render_success()
    return st


def insert_artist(nid, name, surname, byear):

    con = connection()

    try:
        with con.cursor() as cursor:
            sql ='''insert into `kalitexnis` (`ar_taut`, `onoma`, `epitheto`, `etos_gen`)
                  values (%s, %s, %s, %s)'''
            cursor.execute(sql, (nid, name, surname, byear))
            con.commit()

    finally:
        con.close()


def render_success():
    st = '''<meta charset = "utf-8"/>
            <h1>Database updated successfully!</h1>
            <form action="/insert_artist">
            <input type="submit" value="Insert new artist">
            </form>
            <form action="/">
            <input type="submit" value="Main menu">
            </form>
            '''
    return st
