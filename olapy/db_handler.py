# -*- coding: utf-8 -*-
"""
Created on Tue Sep 1 09:22:26 2014

generic db handler for postgresql


@author: ptorre
"""
import pandas.io.sql as psql
import psycopg2 

    
class database_link():
    def __init__(self, db_name, db_user, db_password, db_host='localhost'):
        """
            this method saves the user's credentials when the 
            object is initialized. 
        
        """
        self.db_name = db_name
        self.db_user=db_user
        self.db_password=db_password
        self.db_host=db_host
    

    def start_conn(self):
        """
        This method returns a fresh connection to the database. 
        
        """
        return psycopg2.connect(
                    database=self.db_name, 
                    user=self.db_user,
                    password=self.db_password, 
                    host=self.db_host)
                    
    def write_db(self, insert_sql, data=None):
        '''
            generic function to connect to the db and write
        '''
        try:
            dbconn = self.start_conn()
            cursor = dbconn.cursor()
            if data==None:
                cursor.execute(insert_sql)
            else:
                cursor.executemany(insert_sql, data)
            dbconn.commit()
            dbconn.close()
        except Exception as error:
            print (error)
            raise Exception("ERROR: write to DB failed")

    def read_db(self,sql, pandas=True):
        '''
        This is a generic function to read the database
        read_comm: an SQL command for the data that is being retrieved from psycopg2.
        output: a pandas dataframe or a list of tuples. 
        '''
        try:
            dbconn = self.start_conn()
            if pandas:
                return psql.read_sql(sql, dbconn)
            else: 
                cursor = dbconn.cursor()
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as error:
            print (error)
            raise Exception("ERROR: read to DB failed")

if __name__=="__main__":
    # temporary! hard coded credentials. these must come from the user input later. 
    db_name = "tarsus"
    db_user = 'pabtorre'
    db_password = 'im singing in the rain what a glorious feeling'
    #%%
    db = database_link(db_name, db_user, db_password)
