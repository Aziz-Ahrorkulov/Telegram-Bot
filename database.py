import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()


    def add_user(self, user_id):
        with self.connection: 
            return self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))

    def user_exist(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))
        
    def set_nickname(self, user_id, nickname):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `nickname` = ? WHERE `user_id` = ?", (nickname, user_id,))
    
    def set_age(self, user_id, age):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `age` = ? WHERE `user_id` = ?", (age, user_id,))
    
    
    def get_signup(self, user_id ):
        with self.connection:
            result =  self.cursor.execute("SELECT `signup` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup

    
    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `signup` = ? WHERE `user_id` = ?", (signup, user_id,))

    def get_user_info(self, user_id):
        with self.connection:
            result =  self.cursor.execute("SELECT `nickname`, `age` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                info = str(row[0])
            return info
# try:
#     # connection to exist database
#     connection = psycopg2.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=db_name
#     )
#     connection.autocommit = True
    
#     with connection.cursor() as cursor:
#         cursor.execute(
#             "SELECT version();"
#         )    

#         print(f'Server cersion: {cursor.fetchone()}')

#     with connection.cursor() as cursor:
#         cursor.execute(
#             """CREATE TABLE users(
#             id serial PRIMARY KEY NOT NULL,
#             first_name varchar(50) NOT NULL,
#             nickname VARCHAR(50) NOT NULL);"""
#         ) 

#         print("[INFO] Table created successully")
#         # connection.commit


# except Exception as ex:
#     print("[INFO] Error while working with PostgreSQL", ex)
# finally:
#     if connection:
#         connection.close()
#         print("[INFO] PostgreSQL connection closed")
