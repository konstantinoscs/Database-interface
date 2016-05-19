#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import get, post, request, run, route
from home_page import *
from search_songs import*
from update_n_search import *
from insert_artist import *
from edit_artist import *
from insert_artist import *
from insert_song import *



run(host='localhost', port=8080, debug=True)
#data=find_song('ΦΡΑΓΚΟΣΥΡΙΑΝΗ', 1938, 'COLUMBIA')
#data = find_artists('ΓΙΑΝΝΗΣ', 'ΣΠΑΝΟΣ', 0, 2000 ,0)
#st = render_artists_table(data)
#st=create_table(data)
#print st