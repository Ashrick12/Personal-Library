# Personal Library App

This is a Python library application that helps you manage your book collection. It allows you to add, view, edit, and delete books, categorize them based on read status and reading progress, and track important details like author, title, and page number.

![Library App](https://i.imgur.com/duRVEdO.png)

## Features

* **Add new books:** Enter book details like title, author, and reading status.
* **View all books:** Display a list of all books in your collection, sorted by author.
* **Filter books:** View only read books, unread books, or currently reading books.
* **Update book information:** Edit details like title, author, reading status, and page number.
* **Delete books:** Remove unwanted books from your collection.
* **Track reading progress:** Mark books as read or currently reading, and update page numbers.

## Requirements

* Python 3.7 or later
* PySimpleGUI library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/ashrick12/personal-library.git
```
2. Open personal-library folder in python
```
cd personal-library
```
3. Install required libraries:
```
pip install -r requirements.txt
```
4. Run the main script:
```
python library.py
```

## Usage

The application opens with the main menu, providing options to:

* **View all books:** See a list of all books in your collection, sorted by author.
* **View specific categories:**
    * **Read books:** Display only books marked as "Read".
    * **Unread books:** Display only books marked as "Unread".
    * **Currently reading books:** Display only books marked as "Reading".
* **Add new books:** Enter details like title, author, reading status, and page number to add a new book to your collection.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT License](LICENSE)
