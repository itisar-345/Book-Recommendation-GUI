import tkinter as tk
from tkinter import ttk, messagebox
import MySQLdb
import matplotlib.pyplot as plt
import seaborn as sns

# Database connection
db = MySQLdb.connect(host="localhost", user="root", password="", database="book")
cursor = db.cursor()

# Table creation
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(255),
        password VARCHAR(255)
    )
''')
# Commit table creation query
db.commit()

result_label = None
genre_vars = None
tree = None


def open_registration_window():
    registration_window = tk.Toplevel(main_window)
    registration_window.title("Registration")

    label_name = tk.Label(registration_window, text="Name:")
    label_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    entry_name = tk.Entry(registration_window)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    label_email = tk.Label(registration_window, text="Email:")
    label_email.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    entry_email = tk.Entry(registration_window)
    entry_email.grid(row=1, column=1, padx=10, pady=5)

    label_username = tk.Label(registration_window, text="Username:")
    label_username.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    entry_username = tk.Entry(registration_window)
    entry_username.grid(row=2, column=1, padx=10, pady=5)

    label_password = tk.Label(registration_window, text="Password:")
    label_password.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
    entry_password = tk.Entry(registration_window, show="*")
    entry_password.grid(row=3, column=1, padx=10, pady=5)

    def register_user():
        name = entry_name.get()
        email = entry_email.get()
        username = entry_username.get()
        password = entry_password.get()

        try:
            cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
            db.commit()
            messagebox.showinfo("Registration", f"User {username} registered successfully!")
            registration_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error during registration: {e}")

    button_register = tk.Button(registration_window, text="Register", command=register_user, bg="#3296FF")
    button_register.grid(row=4, column=1, pady=10)


def authenticate_user(username, password):
    query = "SELECT * FROM user WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user_data = cursor.fetchone()
    return user_data


def login_user():
    username = entry_username_login.get()
    password = entry_password_login.get()

    if not username or not password:
        login_status_label.config(text="Please enter both username and password.", fg="red")
        return

    user_data = authenticate_user(username, password)

    if user_data:
        show_main_page()
        login_status_label.config(text="")
    else:
        login_status_label.config(text="Invalid username or password. Please try again.", fg="red")


def logout():
    main_page_window.destroy()
    show_login_page()


def show_login_page():
    global main_window
    main_window = tk.Tk()
    main_window.title("Login")

    label_username = tk.Label(main_window, text="Username:")
    label_username.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    entry_username_login = tk.Entry(main_window)
    entry_username_login.grid(row=0, column=1, padx=10, pady=5)

    label_password = tk.Label(main_window, text="Password:")
    label_password.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    entry_password_login = tk.Entry(main_window, show="*")
    entry_password_login.grid(row=1, column=1, padx=10, pady=5)

    button_login = tk.Button(main_window, text="Login", command=login_user, bg="#64FF64")
    button_login.grid(row=2, column=0, columnspan=2, pady=10)

    login_status_label = tk.Label(main_window, text="")
    login_status_label.grid(row=3, column=1, pady=10)

    button_register_open = tk.Button(main_window, text="Register", command=open_registration_window, bg="#3296FF")
    button_register_open.grid(row=4, column=0, columnspan=2, pady=10)


# Modify the show_main_page function
def show_main_page():
    global result_label, genre_vars, tree, main_page_window  # Declare global variables
    main_window.withdraw()  # Hide the main window

    main_page_window = tk.Toplevel(main_window)
    main_page_window.title("Book Recommendations")  # Comment out or remove this line

    # Create a custom title bar with a centered label
    title_frame = tk.Frame(main_page_window, bg="lightblue", relief="raised", bd=2)
    title_frame.pack(fill=tk.X)

    title_label = tk.Label(title_frame, text="Book Recommendations", font=("Helvetica",  18), bg="lightblue")
    title_label.pack(side=tk.LEFT, expand=True)

    options = ['Action', 'Adventure', 'Autobiography', 'Biography', 'Comedy', 'Contemporary', 'Crime', 'Dark', 'Detective', 'Drama', 'Dystopian', 'Epic', 'Exploration', 'Fantasy', 'Fiction', 'Historical', 'History', 'Horror', 'Humorous', 'Literary', 'Memoir', 'Middle grade', 'Mystery', 'Paranormal', 'Picture books', 'Play', 'Poetry', 'Psychological', 'Rebirth', 'Reincarnation', 'Revenge', 'Romance', 'Satirical', 'Science', 'Self-help', 'Suspense', 'Thriller', 'Tragedy', 'Transmigration', 'Travel', 'War', 'Young adult (YA)']
    genre_vars = {genre: tk.BooleanVar() for genre in options}

    heading_label = tk.Label(main_page_window, text="Select one or many options:")
    heading_label.pack()

    row1 = tk.Frame(main_page_window)
    row2 = tk.Frame(main_page_window)
    row3 = tk.Frame(main_page_window)
    row1.pack()
    row2.pack()
    row3.pack()

    for idx, genre in enumerate(options):
        chk = tk.Checkbutton(main_page_window, text=genre, variable=genre_vars[genre], onvalue=True, offvalue=False)
        if idx < len(options) // 3:
            chk.pack(in_=row1, side="left", padx=10, pady=5)
        elif idx < 2 * len(options) // 3:
            chk.pack(in_=row2, side="left", padx=10, pady=5)
        else:
            chk.pack(in_=row3, side="left", padx=10, pady=5)

    fetch_button = tk.Button(main_page_window, text="Filter", command=lambda: [clear_message(), fetch_books()], bg="#96C8FF")
    fetch_button.pack()

    tree = ttk.Treeview(main_page_window, columns=("Title", "Author", "Description", "Genres"), show="headings", height=15)
    tree.heading("Title", text="Title")
    tree.heading("Author", text="Author")
    tree.heading("Description", text="Description")
    tree.column("Description", width=400)
    tree.heading("Genres", text="Genres")
    tree.pack()

    tree.bind("<ButtonRelease-1>", show_book_details)

    result_label = tk.Label(main_page_window, text="")
    result_label.pack()

    # Fetch and display all books initially
    fetch_all_books()

    # Add a Logout button
    logout_button = tk.Button(main_page_window, text="Logout", command=logout, bg="#FF4B4B")
    logout_button.pack()


def fetch_all_books():
    global tree  # Declare global variable
    # Updated query to fetch at least  100 books, or as many as available
    query = "SELECT title, author, description, genres, goodreads_rating, amazon_rating, bookish_rating, fantastic_fiction_rating, book_depository_rating FROM books ORDER BY RAND()"
    cursor.execute(query)
    books = cursor.fetchall()
    clear_table()

    if books:
        for book in books:
            tree.insert("", "end", values=book)
        result_label.config(text="")
    else:
        result_label.config(text="No books available!")

    # Make the tree widget fill the entire window
    tree.pack(expand=True, fill=tk.BOTH)


def fetch_books():
    global genre_vars, tree  # Declare global variables
    genres = [genre for genre, var in genre_vars.items() if var.get()]

    if not genres:
        # If no genres are selected, fetch all books
        query = "SELECT title, author, description, genres, goodreads_rating, amazon_rating, bookish_rating, fantastic_fiction_rating, book_depository_rating FROM books ORDER BY RAND() LIMIT 20"
    else:
        # If genres are selected, fetch books based on selected genres
        conditions = " AND ".join([f"genres LIKE '%{genre}%'" for genre in genres])
        query = f"SELECT title, author, description, genres, goodreads_rating, amazon_rating, bookish_rating, fantastic_fiction_rating, book_depository_rating FROM books WHERE {conditions} ORDER BY RAND() LIMIT 20"

    cursor.execute(query)
    books = cursor.fetchall()
    clear_table()

    if books:
        for book in books:
            tree.insert("", "end", values=book)
        result_label.config(text="")
    else:
        result_label.config(text="No books found for selected genres or no books available!")


def clear_table():
    for row in tree.get_children():
        tree.delete(row)

def clear_message():
    result_label.config(text="")


def show_book_details(event):
    global tree
    selected_item = tree.selection()
    if selected_item:
        item_values = tree.item(selected_item)['values']

        # Create a new window for displaying book details
        details_window = tk.Toplevel(main_window)
        details_window.title("Book Details")

        # Display book details
        details_label = tk.Label(details_window,
                                text=f"Title: {item_values[0]}\nAuthor: {item_values[1]}\nDescription: {item_values[2]}\nGenres: {item_values[3]}",
                                anchor="w", justify="left")
        details_label.grid(row=0, column=0, padx=10, pady=10)

        # Plot ratings
        def plot_ratings():
            ratings_labels = ["Goodreads", "Amazon", "Bookish", "Fantastic Fiction", "Book Depository"]
            ratings = [float(item_values[i + 4]) for i in range(5)]  # Convert all ratings to float

            plt.figure(figsize=(8, 4))

            # Set seaborn style for an aesthetically pleasing plot
            sns.set(style="whitegrid")

            # Use a cool color palette
            colors = sns.color_palette("PuRd", len(ratings_labels))

            # Create a bar plot
            bars = plt.bar(ratings_labels, ratings, color=colors)

            # Add data labels to the bars
            for bar, rating in zip(bars, ratings):
                plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05, f'{rating:.2f}', ha='center', va='bottom', fontsize=10, color='black')

            plt.xlabel('Rating Source')
            plt.ylabel('Rating')
            plt.title('Book Ratings')

            plt.show()

        # Create a button to trigger the ratings plot
        button_ratings = tk.Button(details_window, text="Ratings", command=plot_ratings, bg="#FFFF64")
        button_ratings.grid(row=1, column=0, padx=10, pady=10)

        # Define a function to calculate average rating and display emojis
        def calculate_average_rating():
            ratings = [float(item_values[i + 4]) for i in range(5)]  # Convert all ratings to float
            average_rating = sum(ratings) / len(ratings)

            # Map the average rating to emoji
            rating_mapping = {
                1: ("😢", "Bad"),
                2: ("😐", "Ok"),
                3: ("😊", "Good"),
                4: ("😃", "Very Good"),
                5: ("😍", "Extremely Good")
            }

            emoji, written_representation = rating_mapping.get(round(average_rating), ("😐", "Neutral"))  # Default to neutral

            # Display the average rating using emojis and written representation
            messagebox.showinfo("Average Rating", f"Average Rating: {average_rating:.1f} {emoji} ({written_representation})")


        # Create a button to trigger the average rating calculation
        button_average_rating = tk.Button(details_window, text="Average Rating", command=calculate_average_rating, bg="#B4B4B4")
        button_average_rating.grid(row=2, column=0, padx=10, pady=10)


# GUI setup
main_window = tk.Tk()
main_window.title("Login")

label_username = tk.Label(main_window, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_username_login = tk.Entry(main_window)
entry_username_login.grid(row=0, column=1, padx=10, pady=5)

label_password = tk.Label(main_window, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_password_login = tk.Entry(main_window, show="*")
entry_password_login.grid(row=1, column=1, padx=10, pady=5)

button_login = tk.Button(main_window, text="Login", command=login_user, bg="#64FF64")
button_login.grid(row=2, column=0, columnspan=2, pady=10)

login_status_label = tk.Label(main_window, text="")
login_status_label.grid(row=3, column=1, pady=10)

button_register_open = tk.Button(main_window, text="Register", command=open_registration_window, bg="#3296FF")
button_register_open.grid(row=4, column=0, columnspan=2, pady=10)

main_window.mainloop()
