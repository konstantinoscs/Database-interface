# -*- coding: utf-8 -*-
from connection import *


def insert_artist(id, name, surname, byear):

    con = connection()

    try:
        with con.cursor() as cursor:
            sql = ""

    finally:
