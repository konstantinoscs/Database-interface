# -*- coding: utf-8 -*-

from bottle import get, post, request
from artists import *


@get('/update_n_search')
def update():
    return '''<!DOCTYPE html>
        <head><meta charset="UTF-8"></head>
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
                    <td> <input type="text" name="Birth_year_from" maxlength="4" value=""> </td>
                </tr>

                <tr>
                    <td> Birth Year - To </td>
                    <td> <input type="text" name="Birth_year_to" maxlength="4" value=""> </td>
                </tr>

                <tr>
                    <td>Type</td>
                    <td>
                        <input type="radio" name="type" value="Singer" checked> Singer <br>
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
    ptype = request.forms.getunicode('type')
    data = find_artists(name, surname, birth_year_from, birth_year_to, ptype)
    st = render_artists_table(data)
    return st
