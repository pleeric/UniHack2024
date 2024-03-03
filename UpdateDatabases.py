import json
import sqlite3


def UpdateDatabase(db,data):
    """ Loop over json file and load into SQL database
    Args:
        db (str): string path to database
        data (str): string path to data
    """

    data=json(data) #convert json to dictionary

    con=sqlite3.connect(db)
    cur=con.cursor()


    for item in data:
        id,type,httpl,imgl=item['id'],item['type'],item['pageurl'],item['imageurl']
        execStr="INSERT INTO INVENTORY (itemsdesc, coltags,httplink,imglink) VALUES({},{},{},{})".format(id,type,httpl,imgl)
        cur.execute(execStr)
    con.commit()