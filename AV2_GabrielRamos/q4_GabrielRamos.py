import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="gabs",
    password="12345678",
    database="minhaConexao"
)

cursor = db_connection.cursor()

usuarios_table = "USUARIOS"
usuarios_columns = ["id", "nome", "console"]

jogos_table = "JOGOS"
jogos_columns = ["id", "nome", "data_lancamento"]

insert_record = lambda table, columns, values: cursor.execute(f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})", values)

remove_record_by_id = lambda table, id: cursor.execute(f"DELETE FROM {table} WHERE id = %s", (id,))

get_all_records = lambda table: cursor.execute(f"SELECT * FROM {table}"), cursor.fetchall()

insert_record(usuarios_table, usuarios_columns, (1, "Usuario1", "Console1"))

insert_record(jogos_table, jogos_columns, (1, "Jogo1", "2023-10-18"))

remove_record_by_id(usuarios_table, 1)

get_all_records(jogos_table)

cursor.close()
db_connection.close()
