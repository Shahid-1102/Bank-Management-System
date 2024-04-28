import sqlite3

# Function to create a SQLite database and table
def create_database():
    try:
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS customers
                     (id TEXT PRIMARY KEY, password TEXT, balance REAL, joining_date TEXT, name TEXT,
                      account_type TEXT, dob TEXT, mobile_no TEXT, gender TEXT, nationality TEXT, kyc TEXT)''')
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
            for i in range(0, len(lines), 12):
                try:
                    id_num = lines[i].strip()
                    password = lines[i+1].strip()
                    balance = float(lines[i+2].strip())
                    joining_date = lines[i+3].strip()
                    name = lines[i+4].strip()
                    account_type = lines[i+5].strip()
                    dob = lines[i+6].strip()
                    mobile_no = lines[i+7].strip()
                    gender = lines[i+8].strip()
                    nationality = lines[i+9].strip()
                    kyc = lines[i+10].strip()
                    
                    # Check if customer id already exists in the database
                    c.execute("SELECT * FROM customers WHERE id=?", (id_num,))
                    existing_customer = c.fetchone()
                    if existing_customer is None:
                        # If customer id doesn't exist, insert the new entry
                        c.execute("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                  (id_num, password, balance, joining_date, name, account_type,
                                   dob, mobile_no, gender, nationality, kyc))
                except (IndexError, ValueError) as e:
                    print("Error: Incomplete or invalid data in the file.")
                    break

        conn.commit()
        conn.close()
        print("Data inserted successfully!")
    except sqlite3.Error as e:
        print("Error inserting data:", e)

# Function to update customer balance
def update_customer_balance(id_num, new_balance):
    try:
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()
        c.execute("UPDATE customers SET balance = ? WHERE id = ?", (new_balance, id_num))
        conn.commit()
        conn.close()
        print("Customer balance updated successfully!")
    except sqlite3.Error as e:
        print("Error updating customer balance:", e)

# Function to update customer PIN
def update_customer_pin(id_num, new_pin):
    try:
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()
        c.execute("UPDATE customers SET password = ? WHERE id = ?", (new_pin, id_num))
        conn.commit()
        conn.close()
        print("Customer PIN updated successfully!")
    except sqlite3.Error as e:
        print("Error updating customer PIN:", e)


# Function to delete customer record
def delete_customer_record(id_num):
    try:
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()
        c.execute("DELETE FROM customers WHERE id = ?", (id_num,))
        conn.commit()
        conn.close()
        print("Customer record deleted successfully!")
    except sqlite3.Error as e:
        print("Error deleting customer record:", e)

# Main function
def main():
    create_database()
    filename = './database/customerDatabase.txt'  # Change this to the path of your text file
    insert_new_data_from_file(filename)

if __name__ == "__main__":
    main()
