import mysql.connector


def create_database():
    connection = None
    cursor = None

    try:
        # Connect to MySQL Server (no specific database)
        connection = mysql.connector.connect(
            host="localhost",
            user="yourusername",      # REPLACE WITH YOUR USERNAME
            password="yourpassword"   # REPLACE WITH YOUR PASSWORD
        )

        cursor = connection.cursor()

        # Create database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close cursor
        if cursor is not None:
            cursor.close()

        # Close connection
        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()