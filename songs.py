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
            sql = "select `ar_taut` from `kalitexnis`, `singer_prod` where `tragoudistis` = `ar_taut`"
            cursor.execute(sql)
            data = cursor.fetchall()

    finally:
        con.close()

    return data


def fetch_data_composers():

    con = connection()

    try:
        with con.cursor() as cursor:
            sql = "select `ar_taut` from `kalitexnis`, `tragoudi` where `sinthetis` = `ar_taut`"
            cursor.execute(sql)
            data = cursor.fetchall()

    finally:
        con.close()

    return data


def fetch_data_songwriters():

    con = connection()

    try:
        with con.cursor() as cursor:
            sql = "select `ar_taut` from `kalitexnis`, `tragoudi` where `stixourgos` = `ar_taut`"
            cursor.execute(sql)
            data = cursor.fetchall()

    finally:
        con.close()

    return data
