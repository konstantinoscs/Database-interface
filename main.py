#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import get, post, request, run, route
from home_page import *
from search_songs import*
from artists import *

@get('/update_n_search')
def update():
    return '''
        <div>
        <div style="font-size:200%;"><strong>Presentation of Artists</strong></div>
        <br>

        <form method="POST" action="/update_n_search">
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
    ptype=request.forms.getunicode('type')
    birth_year_from=int(birth_year_from)
    birth_year_to=int(birth_year_to)
    data = find_artists(name, surname, birth_year_from, birth_year_to, ptype)
    st = render_artists_table(data)
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

run(host='localhost', port=8080, debug=True)
#data=find_song('ΦΡΑΓΚΟΣΥΡΙΑΝΗ', 1938, 'COLUMBIA')
#st=create_table(data)
#print st