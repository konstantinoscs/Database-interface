#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import get, post, request, run, route, redirect
from find_song import *
import insert_artist


@route('/')
@route('/home')
def home_page():
    return '''
    <div>

    <form action="/update_n_search">
    <input type="submit" value="UPDATE & SEARCH ARTISTS">
    </form>

    <form action="/search_songs">
    <input type="submit" value="SEARCH SONGS">
    </form>

    <form action="/insert_artist">
    <input type="submit" value="INSERT ARTIST">
    </form>
    <form action="/insert_song">
    <input type="submit" value="INSERT SONG">
    </form>
    </div>
    '''

@get('/update_n_search')
def update():
    return '''
        <div>
        <div style="font-size:200%;"><strong>Presentation of Artists</strong></div>
        <br>

        <form>
        <fieldset>
            <table style="">
                <tr>
                    <td> <span align="left">Name </span></td>
                    <td> <input align="right" type="text" name="Name" value=""></td>
                </tr>

                <tr>
                    <td> <span align="left"> Surname </span></td>
                    <td> <input align="right" type="text" name="Surname" value=""> </td>
                </tr>

                <tr>
                    <td>Birth Year - From</td>
                    <td> <input type="text" name="Birth_year_from" value=""> </td>
                </tr>

                <tr>
                    <td> Birth Year - To </td>
                    <td> <input type="text" name="Birth_year_to" value=""> </td>
                </tr>

                <tr>
                    <td>Type</td>
                    <td>
                        <input type="radio" name="type" value="Singer"> Singer <br>
                        <input type="radio" name="type" value="SongWriter"> SongWriter <br>
                        <input type="radio" name="type" value="Composer"> Composer <br>
                    </td>
                </tr>
                <tr>
                <td></td>
                    <td><input type="submit" value="Submit"></td>\
                </tr>
            </table>
        </fieldset>
        </form>
        </div>
        '''

@post('/update_n_search')
def get_data_update():
    name=request.forms.getunicode('Name')
    surname=request.forms.getunicode('Surname')
    birth_year_from=request.forms.getunicode('Birth_year_from')
    birth_year_to=request.forms.getunicode('Birth_year_to')
    type=request.forms.getunicode('type')


@get('/search_songs')
def search_songs():
    return '''
        <meta charset = "utf-8"/>
        <div>
            <div style="font-size:200%;"><strong>Presentation of Songs</strong></div>
            <br>

            <form method="POST" action="/search_songs">
                <fieldset>
                    <table style="">
                        <tr>
                            <td> <span align="left">Song Title </span></td>
                            <td> <input align="right" type="text" name="Song_title" value=""> </td>
                        </tr>


                        <tr>
                            <td> <span align="left">Production Year</span></td>
                            <td> <input align="right" type="text" name="Prod_year" value=""> </td>
                        </tr>


                        <tr>
                            <td> <span align="letf">Company</span></td>
                            <td> <input align="right" type="text" name="Company" value=""> </td>
                        </tr>


                        <tr>
                            <td></td>
                            <td> <input type="submit" value="Submit"> </td>
                        </tr>


                    </table>
                </fieldset>
            </form>
    </div>
'''


@post('/search_songs')
def get_search_songs():
    title = request.forms.getunicode('Song_title')
    year = request.forms.getunicode('Prod_year')
    company = request.forms.getunicode('Company')
    year = int(year)
    data = find_song(title, year, company)
    st = create_table(data)
    return st


@route('/results')
def post_songs(data):
    return data


@get('/insert_artist')
def insert_artist_form():
    return '''
    <div>
        <div style="font-size:200%;"><strong>Insert Artist</strong></div>
        <br>
        <form>
            <fieldset>
                <table style="">
                    <tr>
                        <td> <span align="left">National Id </span></td>
                        <td> <input align="right" type="text" name="National_id" value=""> </td>
                    </tr>


                    <tr>
                        <td> <span align="left">Name</span></td>
                        <td> <input align="right" type="text" name="Name" value=""> </td>
                    </tr>


                    <tr>
                        <td> <span align="letf">Surname</span></td>
                        <td> <input align="right" type="text" name="Surname" value=""> </td>
                    </tr>


                    <tr>
                        <td> <span align="left">Birth Year</span></td>
                        <td> <input align="right" type="number" name="Birth_year" min="1900" max="2016"> </td>
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
    national_id=request.forms.getunicode('National_id')
    name=request.forms.getunicode('Name')
    surname=request.forms.getunicode('Surname')
    birth_year=request.forms.getunicode('Birth_year')
    birth_year = int(birth_year)


@get('/insert_song')
def insert_song():
    return '''
    <div>
        <div style="font-size:200%;"><strong>Insert Song</strong></div>
        <br>

        <form>
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
                        <td> <input type="text" name="CD" value=""> </td>
                    </tr>


                    <tr>
                        <td>Singer</td>
                        <td> <input type="number" name="Birth_year" min="1900" max="2016"> </td>
                    </tr>


                    <tr>
                        <td>Composer</td>
                        <td> <input type="number" name="Birth_year" min="1900" max="2016"> </td>
                    </tr>


                    <tr>
                        <td>Song Writer</td>
                        <td> <input type="number" name="Birth_year" min="1900" max="2016"> </td>
                    </tr>


                    <tr>
                        <td></td>
                        <td> <input type="submit" value="Submit"> </td>
                    </tr>


                </table>
            </fieldset>
        </form>
    </div>
    '''

@post('/insert_song')
def get_insert_songs():
    title=request.forms.get('Title')
    prod_year=request.forms.get('Prod_year')

def test():

    con = connection()
    try:

        with con.cursor() as cursor:
            sql = "SELECT `cd` FROM `singer_prod`"
            cursor.execute(sql)
            #result = cursor.fetchone()
            #print(result)
            for row in cursor:
                print row
    finally:
        con.close()


def test2():
    name = 'ΓΙΑΝΝΗΣ'
    surname = 'ΣΠΑΝΟΣ'

    con = connection()

    try:
        # with connection.cursor() as cursor:
        # Create a new record
        # sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        # connection.commit()

        with con.cursor() as cursor:
            # Read a single record
            sql = "SELECT `onoma`,`epitheto`,`ar_taut`,`etos_gen` FROM `kalitexnis`"
            cursor.execute(sql)
            # result = cursor.fetchone()
            # print(result)
            for row in cursor:
                print row
    finally:
        con.close()

run(host='localhost', port=8080, debug=True)
#test()
#test2()
#data=find_song('ΦΡΑΓΚΟΣΥΡΙΑΝΗ', 1938, 'COLUMBIA')
#st=create_table(data)
#print st