import sqlite3

# Function to create a SQLite database and table
def create_database():
    try:
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS admin
                     (username TEXT PRIMARY KEY, password TEXT)''')  # Set username as primary key to prevent duplicates
        conn.commit()
        conn.close()
        print("Database created successfully!")
    except sqlite3.Error as e:
        print("Error creating database:", e)

# Function to read data from the text file and insert new entries into the database
def insert_new_data_from_file(filename):
    try:
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()

        with open(filename, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 3):
                try:
                    username = lines[i].strip()
                    password = lines[i+1].strip()
                    # Check if username already exists in the database
                    c.execute("SELECT * FROM admin WHERE username=?", (username,))
                    existing_user = c.fetchone()
                    if existing_user is None:
                        # If username doesn't exist, insert the new entry
                        c.execute("INSERT INTO admin VALUES (?, ?)", (username, password))
                except IndexError:
                    print("Error: Incomplete data in the file.")
                    break

        conn.commit()
        conn.close()
        print("Data inserted successfully!")
    except sqlite3.Error as e:
        print("Error inserting data:", e)

# Function to update admin password
def update_admin_password(username, new_password):
    try:
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()
        c.execute("UPDATE admin SET password = ? WHERE username = ?", (new_password, username))
        conn.commit()
        conn.close()
        print("Admin password updated successfully!")
    except sqlite3.Error as e:
        print("Error updating admin password:", e)

# Function to delete admin record
def delete_admin_record(username):
    try:
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()
        c.execute("DELETE FROM admin WHERE username = ?", (username,))
        conn.commit()
        conn.close()
        print("Admin record deleted successfully!")
    except sqlite3.Error as e:
        print("Error deleting admin record:", e)

# Main function
def main():
    create_database()
    filename = './database/adminDatabase.txt'  # Change this to the path of your text file
    insert_new_data_from_file(filename)

if __name__ == "__main__":
    main()
