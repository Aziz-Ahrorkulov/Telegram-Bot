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
        

    def user_age(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT age FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
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
        
    def set_gender(self, user_id, gender):
        with self.connection:
            try:
                self.cursor.execute("UPDATE users SET gender = ? WHERE user_id = ?", (gender, user_id))
                return True
            except sqlite3.Error as e:
                print(f"Error setting gender: {e}")
                return False

    def get_gender(self, user_id):
        with self.connection:
            try:
                self.cursor.execute("SELECT gender FROM users WHERE user_id = ?", (user_id,))
                result = self.cursor.fetchone()
                if result:
                    return result[0]
                else:
                    return None
            except sqlite3.Error as e:
                print(f"Error getting gender: {e}")
                return None
            
    def get_user_info(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `nickname`, `age`, gender FROM `users` WHERE `user_id` = ?", (user_id,)).fetchone()
            if result:
                nickname, age, gender = result  # Разделение результата запроса на nickname и age
                return f"Никнейм: {nickname} \nВозраст: {age} \nПол: {gender}"
            else:
                return "Информация о пользователе не найдена"
        

    def delete_user(self, user_id):
        try:
            with self.connection:
                self.cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
                self.connection.commit()
                print(f"Пользователь с ID {user_id} удален")
                return True
        except sqlite3.Error as error:
            print(error)
            return False
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
