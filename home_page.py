# -*- coding: utf-8 -*-

def render_home_page():
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