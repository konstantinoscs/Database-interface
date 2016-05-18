# -*- coding: utf-8 -*-

from bottle import get, post, request
from find_song import *

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
                            <td> <span>Company</span></td>
                            <td> <input type="text" name="Company" value=""> </td>
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
    #if not (year is None):
    #   year = int(year)
    data = find_song(title, year, company)
    st = create_table(data)
    return st