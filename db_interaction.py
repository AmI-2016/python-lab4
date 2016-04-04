'''
Created on Apr 04, 2016
Copyright (c) 2015-2016 Teodoro Montanaro

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
@author: tmontanaro
'''

from sys import argv
import os
import sqlite3


def db_insert_task(text, urgent):
    '''
    :param text: text that we want to insert as task in the db
    :param urgent: 0 if the task is not urgent, 1 otherwise

    This method insert a task in the database
    '''

    # prepare the query text
    sql = """INSERT INTO task(todo, urgent) VALUES (?, ?)"""

    #connect to the db
    conn = sqlite3.connect("task_list.db")
    cursor = conn.cursor()

    try:
        #execute the query passing the needed parameters
        cursor.execute(sql, (text, urgent) )
        #commit all pending executed queries in the connection
        conn.commit()
    except Exception,e:
        print str(e)
        # if something goes wrong: rollback
        conn.rollback()

    #close the connection
    conn.close()


def db_remove_task(text):
    '''
    :param text: text (or part of it) of the task we want to remove from the db

    This method remove from the db all the tasks that contain the specified string
    '''

    # prepare the query text
    sql = """delete from task where todo LIKE ?"""

    # add percent sign (%) wildcard to select all the strings that contain specified text
    # <<the multiple character percent sign (%) wildcardcan be used to represent any number of characters in a value match>>
    text = "%"+text + "%"

    #connect to the db
    conn = sqlite3.connect("task_list.db")
    cursor = conn.cursor()

    try:
        #execute the query passing the needed parameters
        cursor.execute(sql, (text, ) )
        #commit all pending executed queries in the connection
        conn.commit()
    except Exception,e:
        print str(e)
        # if something goes wrong: rollback
        conn.rollback()

    #close the connection
    conn.close()