# -*- coding: utf-8 -*-

import pymysql
from bottle import get, post, request
from connection import *
from songs import *


@get('/insert_song')
def insert_song():
    cd = fetch_data_cd()
    singers = fetch_data_singers()
    composers = fetch_data_composers()
    songwriters = fetch_data_songwriters()
    st = render_insert_page(cd, singers, composers, songwriters)
    return st


def render_insert_page(cd, singers, composers, songwriters):

    st = '''<div>
        <div style="font-size:200%;"><strong>Insert Song</strong></div>
        <br>

        <form method="POST" action="/insert_song">
            <fieldset>
                <table style="">
                    <tr>
                        <td>Title</td>
                        <td> <input type="text" name="Title" value=""> </td>
                    </tr>

                    <tr>
                        <td> Production Year</td>
                        <td> <input type="text" name="Prod_year" value=""> </td>
                    </tr>

                    <tr>
                        <td>CD</td>
                        <td><select>
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
        <td><select>'''

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
        <td><select>'''

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
        <td><select>'''

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
        </div>'''

    return st


@post('/insert_song')
def get_insert_songs():
    title=request.forms.get('Title')
    prod_year=request.forms.get('Prod_year')

