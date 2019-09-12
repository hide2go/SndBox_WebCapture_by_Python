import mysql.connector
from mysql.connector import Error
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData
def insertBLOB(emp_id, name, photo, biodataFile):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='sandbox',
                                             user='root',
                                             password='admin')
        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO python_employee
                          (id, name, photo, biodata) VALUES (%s,%s,%s,%s)"""
        empPicture = convertToBinaryData(photo)
        file = convertToBinaryData(biodataFile)
        # Convert data into tuple format
        insert_blob_tuple = (emp_id, name, empPicture, file)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)
    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
insertBLOB(2, "Tom", "C:\sample_files\MC900431641.png","C:\sample_files\MC900431644.png")
#insertBLOB(2, "Scott", "D:\Python\Articles\my_SQL\images\scott_photo.png","C:\sample_files\MC900431644.png")