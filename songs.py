# -*- coding: utf-8 -*-

import pymysql
from connection import *


def fetch_data_cd():

    con = connection()

    try:
        with con.cursor() as cursor:
            sql = "select `code_cd` from `cd_production`"
            cursor.execute(sql)
            data = cursor.fetchall()

    finally:
        con.close()

    return data


def fetch_data_singers():

    con = connection()

    try:
        with con.cursor() as cursor:
            sql = "select distinct(`ar_taut`) from `kalitexnis`, `singer_prod` where `tragoudistis` = `ar_taut`"
            cursor.execute(sql)
            data = cursor.fetchall()

    finally:
        con.close()

    return data


def fetch_data_composers():

    con = connection()

    try:
        with con.cursor() as cursor:
            sql = "select distinct(`ar_taut`) from `kalitexnis`, `tragoudi` where `sinthetis` = `ar_taut`"
            cursor.execute(sql)
            data = cursor.fetchall()

    finally:
        con.close()

    return data


def fetch_data_songwriters():

    con = connection()

    try:
        with con.cursor() as cursor:
            sql = "select distinct(`ar_taut`) from `kalitexnis`, `tragoudi` where `stixourgos` = `ar_taut`"
            cursor.execute(sql)
            data = cursor.fetchall()

    finally:
        con.close()

    return data


def insert_song(title, composer, prod_year, cd, singer, songwriter):

    con = connection()

    try:
        with con.cursor() as cursor:
            sql = '''insert into `tragoudi` (`titlos`, `sinthetis`, `etos_par`, `stixourgos`)
                    values (%s, %s, %s, %s)'''
            cursor.execute(sql, (title, composer, prod_year, songwriter))
            con.commit()

        with con.cursor() as cursor:
            sql = '''insert into `singer_prod` (`cd`, `tragoudistis`, `title`)
                    values (%s, %s, %s)'''
            cursor.execute(sql, (cd, singer, title))
            con.commit()

        st = render_insert_success()

    finally:
        con.close()

    return st


def render_insert_success():
    st = '''<!DOCTYPE html>
        <head><meta charset="UTF-8"></head>
        <body>
        <h1>Database updated successfully!</h1>
        <form action="/insert_song">
        <input type="submit" value="Insert new song">
        </form>
        <form action="/">
       <input type="submit" value="Main menu">
        </form>
        </body>
        '''
    return st
