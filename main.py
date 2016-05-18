#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import get, post, request, run, route
from home_page import *
from search_songs import*
from update_n_search import *
from insert_artist import *
from edit_artist import *
from insert_artist import *


@route('/results')
def post_songs(data):
    return data


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
    counter=0

run(host='localhost', port=8080, debug=True)
#data=find_song('ΦΡΑΓΚΟΣΥΡΙΑΝΗ', 1938, 'COLUMBIA')
#data = find_artists('ΓΙΑΝΝΗΣ', 'ΣΠΑΝΟΣ', 0, 2000 ,0)
#st = render_artists_table(data)
#st=create_table(data)
#print st