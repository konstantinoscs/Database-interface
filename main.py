#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import get, post, request, run, route
from home_page import *
from search_songs import*
from update_n_search import *
from insert_artist import *
from edit_artist import *

@route('/results')
def post_songs(data):
    return data


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
    national_id = request.forms.getunicode('National_id')
    national_id = int(national_id)
    name = request.forms.getunicode('Name')
    surname = request.forms.getunicode('Surname')
    birth_year = request.forms.getunicode('Birth_year')
    birth_year = int(birth_year)
    insert_artist(national_id,name,surname,birth_year)



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
#data = find_artists('ΓΙΑΝΝΗΣ', 'ΣΠΑΝΟΣ', 0, 2000 ,0)
#st = render_artists_table(data)
#st=create_table(data)
#print st