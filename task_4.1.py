# Задача task_4.1

import sqlite3
# # подключение к базе данных для создания и заполнения таблицы
# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()

# # запрос на создание таблицы Students
# query = """CREATE TABLE Students (
# Student_Id INTEGER NOT NULL,
# Student_Name TEXT NOT NULL,
# School_Id INTEGER NOT NULL PRIMARY KEY);
# """

# # запрос на заполнение таблицы Students
# query = """INSERT INTO Students (
# student_id, student_name, school_id)
# VALUES
# (201, 'Иван', 1),
# (202, 'Петр', 2),
# (203, 'Анастасия', 3),
# (204, 'Игорь', 4);
# """
# cursor.execute(query)
# connection.commit()
# connection.close()

# # запрос на вывод данных из таблиц Students и School
# query = """SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, School.School_Name
# FROM Students
# JOIN School ON Students.School_Id = School.School_Id;
# """

# cursor.execute(query)
# connection.commit()
# connection.close()

# использование функции
def get_connection():
    connection = sqlite3.connect('teatchers.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def fetchall_result(id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, School.School_Name 
        FROM Students JOIN School ON Students.School_Id = School.School_Id
        WHERE Student_Id = ?;"""
        cursor.execute(query, (id,))
        result_fetchone = cursor.fetchone()
        # for i in result_fetchone:
        print('ID Студента: ', result_fetchone[0])
        print('Имя студента: ', result_fetchone[1])
        print('ID школы: ', result_fetchone[2])
        print('Название школы: ', result_fetchone[3])
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print('Ошибка в получении данных', error)

id = int(input('Введите ID студента (201, 202, 203, 204): '))
fetchall_result(id)