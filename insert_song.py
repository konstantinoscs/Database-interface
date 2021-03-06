# -*- coding: utf-8 -*-

import pymysql
from bottle import get, post, request
from connection import *
from songs import *


@get('/insert_song')
def insert_songs_page():
    cd = fetch_data_cd()
    singers = fetch_data_singers()
    composers = fetch_data_composers()
    songwriters = fetch_data_songwriters()
    st = render_insert_page(cd, singers, composers, songwriters)
    return st


def render_insert_page(cd, singers, composers, songwriters):

    st = '''<!DOCTYPE html>
        <head><meta charset="UTF-8"></head>
        <body>
        <div>
        <div style="font-size:200%;"><strong>Insert Song</strong></div>
        <br>

        <form method="POST" action="/insert_song">
            <fieldset>
                <table style="">
                    <tr>
                        <td>Title</td>
                        <td> <input type="text" name="Title" required value=""> </td>
                    </tr>

                    <tr>
                        <td> Production Year</td>
                        <td> <input type="text" name="Prod_year" required maxlength="4" value=""> </td>
                    </tr>

                    <tr>
                        <td>CD</td>
                        <td><select name="cd">
                    '''
    for row in cd:
        for i in row:
            st += '<option value="'
            st += str(i)
            st += '">'
            st += str(i)
            st += '</option>'

    st += '''</select></td></tr>
        <tr>
        <td>Singer</td>
        <td><select name="singer">'''

    for row in singers:
        for i in row:
            st += '<option value="'
            st += i.encode('utf-8')
            st += '">'
            st += i.encode('utf-8')
            st += '</option>'

    st += '''</select></td></tr>
        <tr>
        <td>Composer</td>
        <td><select name="composer">'''

    for row in composers:
        for i in row:
            st += '<option value="'
            st += i.encode('utf-8')
            st += '">'
            st += i.encode('utf-8')
            st += '</option>'

    st += '''</select></td></tr>
        <tr>
        <td>Songwriter</td>
        <td><select name="songwriter">'''

    for row in songwriters:
        for i in row:
            st += '<option value="'
            st += i.encode('utf-8')
            st += '">'
            st += i.encode('utf-8')
            st += '</option>'

    st += '''</select></td></tr>
        <tr><td></td>
        <td><input type="submit" value="Submit"> </td>
        </table>
        </fieldset>
        </form>
        </div>
        </body>'''

    return st


@post('/insert_song')
def get_insert_songs():
    title = request.forms.getunicode('Title')
    prod_year = request.forms.getunicode('Prod_year')
    cd = request.forms.getunicode('cd')
    singer = request.forms.getunicode('singer')
    composer = request.forms.getunicode('composer')
    songwriter = request.forms.getunicode('songwriter')
    st = insert_song(title, composer, prod_year, cd, singer, songwriter)
    return st

