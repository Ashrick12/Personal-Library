import json
import PySimpleGUI as sg

Books = []
library_file = 'library.json'
library_icon = 'libraryicon.png'

# Function to save the book data to the JSON file
def dump_books(books):
   """Saves the provided book data to the JSON file."""
   with open(library_file, 'w') as f:
       json.dump(books, f)

def load_books(books):
    try:
        with open(library_file, 'r') as f:
            Books = json.load(f)
    except:
        pass

def show_books():
   """
   Loads book data from the JSON file, displays it in a PySimpleGUI window,
   and handles user interactions for managing books.
   """
   global Books

   while True:
       # Load books from JSON file
        load_books(Books)

       # Sort books by author and then by read status
        Books = sorted(Books, key=lambda d: d['Author'])
        Books = sorted(Books, key=lambda d: d['Read'])

       # Clear and display book list in the GUI
        showBooksWindow['-OUTPUT-'].update('')
        if Books == []:
           showBooksWindow['-OUTPUT-'].print('No Books Found...\n')
        else:
           for book in Books:
               if book['Reading'] == 'Reading':
                   showBooksWindow['-OUTPUT-'].print(f'{book["Title"]} - {book["Author"]} - {book["Reading"]}, Pg. {book["Page"]}\n')
               elif book['Read'] == 'Read':
                   showBooksWindow['-OUTPUT-'].print(f'{book["Title"]} - {book["Author"]} - {book["Read"]}\n')
               else:
                   showBooksWindow['-OUTPUT-'].print(f'{book["Title"]} - {book["Author"]} - {book["Reading"]}, {book["Read"]}\n')

       # Handle user choices from the GUI
        choice, values = showBooksWindow.read()

        if choice == 'Move to Read':
           title = sg.popup_get_text('Title: ', keep_on_top=True)
           for book in Books:
               if title == book['Title']:
                   book['Read'] = 'Read'
                   book['Reading'] = 'Not Reading'
                   dump_books(Books)

        elif choice == 'Move to Reading':
            title = sg.popup_get_text('Title: ', keep_on_top=True)
            for book in Books:
                if title == book['Title']:
                    book['Read'] = 'Unread'
                    book['Reading'] = 'Reading'
                    dump_books(Books)

        elif choice == 'Move to Unread':
            title = sg.popup_get_text('Title: ', keep_on_top=True)
            for book in Books:
                if title == book['Title']:
                    book['Read'] = 'Unread'
                    dump_books(Books)

        elif choice == 'Move to Not Reading':
            title = sg.popup_get_text('Title: ', keep_on_top=True)
            for book in Books:
                if title == book['Title']:
                    book['Reading'] = 'Not Reading'
                    dump_books(Books)

        elif choice == 'Delete Book':
            title = sg.popup_get_text('Title: ', keep_on_top=True)
            for i in Books:
                if title == i['Title']:
                    Books.remove(i)
                    dump_books(Books)
                    
        elif choice == 'Back':
            showBooksWindow.hide()
            break
        elif choice == sg.WIN_CLOSED:
            showBooksWindow.close()
            exit()
            
def show_read():
    """
    Loads book data from the JSON file, displays only read books in a PySimpleGUI window,
    and handles user interactions for managing read books.
    """
    global Books

    while True:
        # Load books from JSON file
        load_books(Books)

        # Sort books by author
        Books = sorted(Books, key=lambda d: d['Author'])

        # Clear and display list of read books in the GUI
        showReadWindow['-OUTPUT-'].update('')
        if Books == []:
            showReadWindow['-OUTPUT-'].print('No Books Found...\n')
        else:
            for book in Books:
                if book['Read'] == 'Read':
                    showReadWindow['-OUTPUT-'].print(f'{book["Title"]} - {book["Author"]} - {book["Read"]}\n')

        # Handle user choices from the GUI
        choice, values = showReadWindow.read()

        if choice == 'Move to Unread':
            title = sg.popup_get_text('Title: ', keep_on_top=True)
            for book in Books:
                if title == book['Title']:
                    book['Read'] = 'Unread'
                    dump_books(Books)

        elif choice == 'Delete Book':
            title = sg.popup_get_text('Title: ', keep_on_top=True)
            for i in Books:
                if title == i['Title']:
                    Books.remove(i)
                    dump_books(Books)

        elif choice == 'Back':
            break
        elif choice == sg.WIN_CLOSED:
            showReadWindow.close()
            exit()
        
def show_unread():
    """
    Loads book data from the JSON file, displays only unread books in a PySimpleGUI window,
    and handles user interactions for managing unread books.
    """
    global Books

    while True:
        # Load books from JSON file
        load_books(Books)

        # Sort books by author
        Books = sorted(Books, key=lambda d: d['Author'])

        # Clear and display list of unread books in the GUI
        showUnreadWindow['-OUTPUT-'].update('')
        if Books == []:
            showUnreadWindow['-OUTPUT-'].print('No Books Found...\n')
        else:
            for book in Books:
                if book['Read'] == 'Unread':
                    if book['Reading'] == 'Reading':
                        showUnreadWindow['-OUTPUT-'].print(f'{book["Title"]} - {book["Author"]} - {book["Reading"]}, Pg. {book["Page"]}\n')
                    else:
                        showUnreadWindow['-OUTPUT-'].print(f'{book["Title"]} - {book["Author"]} - {book["Reading"]}, {book["Read"]}\n')

        # Handle user choices from the GUI
        choice, values = showUnreadWindow.read()

        if choice == 'Move to Read':
            title = sg.popup_get_text('Title: ', keep_on_top=True)
            for book in Books:
                if title == book['Title']:
                    book['Read'] = 'Read'
                    book['Reading'] = 'Not Reading'
                    dump_books(Books)

        elif choice == 'Delete Book':
            title = sg.popup_get_text('Title: ', keep_on_top=True)
            for i in Books:
                if title == i['Title']:
                    Books.remove(i)
                    dump_books(Books)

        elif choice == 'Back':
            break
        elif choice == sg.WIN_CLOSED:
            showUnreadWindow.close()
            exit()

def show_reading():
    """
    Loads book data from the JSON file, displays only books currently being read in a PySimpleGUI window,
    and handles user interactions for managing these books.
    """
    global Books

    while True:
        # Load books from JSON file
        load_books(Books)

        # Sort books by author
        Books = sorted(Books, key=lambda d: d['Author'])

        # Clear and display list of reading books in the GUI
        showReadingWindow['-OUTPUT-'].update('')
        if Books == []:
            showReadingWindow['-OUTPUT-'].print('No Books Found...\n')
        else:
            for book in Books:
                if book['Reading'] == 'Reading':
                    showReadingWindow['-OUTPUT-'].print(f'{book["Title"]} - {book["Author"]} - Pg. {book["Page"]}\n')

        # Handle user choices from the GUI
        choice, values = showReadingWindow.read()

        if choice == 'Move to Not Reading':
            title = sg.popup_get_text('Title: ', keep_on_top=True)
            for book in Books:
                if title == book['Title']:
                    book['Reading'] = 'Not Reading'
                    dump_books(Books)

        elif choice == 'Change Page':
            title = sg.popup_get_text('Title: ', keep_on_top=True)
            for book in Books:
                if title == book['Title']:
                    pgNum = sg.popup_get_text('Page Number: ', keep_on_top=True)
                    book['Page'] = pgNum
                    dump_books(Books)

        elif choice == 'Delete Book':
            title = sg.popup_get_text('Title: ', keep_on_top=True)
            for i in Books:
                if title == i['Title']:
                    Books.remove(i)
                    dump_books(Books)

        elif choice == 'Back':
            break
        elif choice == sg.WIN_CLOSED:
            showReadingWindow.close()
            exit()

def add_book():
    """
    Prompts the user for book details and adds the book to the book data list.
    """
    global Books

    while True:
        title = sg.popup_get_text('Book Title: ', keep_on_top=True)

        if title is None:
            return  # Exit function if user cancels title input

        read = sg.PopupYesNo(f'Have you read {title}?')
        reading = 'Not Reading'

        if read == 'Yes':
            read = 'Read'
            pg_num = '0'
        else:
            read = 'Unread'
            reading_choice = sg.PopupYesNo(f'Are you currently reading {title}?')
            if reading_choice == 'Yes':
                reading = 'Reading'
                pg_num = sg.popup_get_text('Page Number: ', keep_on_top=True)
                if pg_num is None:
                    pg_num = '0'
            else:
                pg_num = '0'

        author = sg.popup_get_text('Author: ', keep_on_top=True)

        book = {
            'Title': title,
            'Read': read,
            'Reading': reading,
            'Page': pg_num,
            'Author': author
        }

        Books.append(book)
        dump_books(Books)
        break  # Exit the loop after adding the book

def main_menu():
    # Open the main menu window and get user choice
    open_mainmenu()
    choice, values = mainmenuWindow.read()
    mainmenuWindow.close()

    # Handle user choice from the main menu
    if choice == 'All Books':
        open_showbooks()
        show_books()
        showBooksWindow.close()
    elif choice == 'Read':
        open_readbooks()
        show_read()
        showReadWindow.close()
    elif choice == 'Unread':
        open_unreadbooks()
        show_unread()
        showUnreadWindow.close()
    elif choice == 'Reading':
        open_readingbooks()
        show_reading()
        showReadingWindow.close()
    elif choice == 'Add Book':
        add_book()
    elif choice == 'Exit':
        mainmenuWindow.close()
        exit()
    elif choice == sg.WIN_CLOSED:
        mainmenuWindow.close()
        exit()


# GUI Layouts
sg.theme('Dark Amber')
def open_mainmenu():
    global mainmenuWindow
    # Main Menu
    TitleCol = [
        [sg.Text(f'Personal Library', justification='center', font=(1,20))]
    ]
    AllBooksCol = [
        [sg.Button('All Books')]
    ]
    ReadUnreadCol = [
        [sg.Button('Read'), sg.Button('Unread')]
    ]
    ReadingBooksCol = [
        [sg.Button('Reading')]
    ]
    AddBooksCol = [
        [sg.Button('Add Book')]
    ]
    ExitCol = [
        [sg.Button('Exit')]
    ]


    mainmenuLayout = [
        [sg.Column(TitleCol, element_justification='center', expand_x=True)],
        [sg.Column(AllBooksCol, element_justification='left', expand_x=True)],
        [sg.Column(ReadUnreadCol, element_justification='left', expand_x=True)], 
        [sg.Column(ReadingBooksCol, element_justification='left', expand_x=True)],
        [sg.Column(AddBooksCol, element_justification='left', expand_x=True)],
        [sg.Column(ExitCol, element_justification='left', expand_x=True)]
        ]
    mainmenuWindow = sg.Window(title='Personal Library', layout=mainmenuLayout, margins=(80,75), use_custom_titlebar=True, finalize=True, keep_on_top=True, titlebar_icon=library_icon)

def open_showbooks():
    global showBooksWindow
    # Show All Books Menu
    TitleCol = [
        [sg.Text(f'All Books', justification='center', font=(1,20))]
    ]
    MoveReadUnreadCol = [
        [sg.Button('Move to Read'), sg.Button('Move to Unread')]
    ]
    MoveReadingCol = [
        [sg.Button('Move to Reading'), sg.Button('Move to Not Reading')]
    ]
    DeleteCol = [
        [sg.Button('Delete Book')]
    ]
    BackCol = [
        [sg.Button('Back')]
    ]

    showBooksLayout = [
        [sg.Column(TitleCol, element_justification='center', expand_x=True)],
        [sg.Multiline(size=(80, 30), key='-OUTPUT-', background_color='black', text_color='white', disabled=True, autoscroll=True)],
        [sg.Column(MoveReadUnreadCol, element_justification='left', expand_x=True)],
        [sg.Column(MoveReadingCol, element_justification='left', expand_x=True)], 
        [sg.Column(DeleteCol, element_justification='left', expand_x=True)],
        [sg.Column(BackCol, element_justification='left', expand_x=True)],
        ]
    showBooksWindow = sg.Window(title='Personal Library', layout=showBooksLayout, margins=(15,75), use_custom_titlebar=True, finalize=True, keep_on_top=True, titlebar_icon=library_icon)

def open_readbooks():
    global showReadWindow
    # Show Read Books Menu
    TitleCol = [
        [sg.Text(f'Read Books', justification='center', font=(1,20))]
    ]
    MoveUnreadCol = [
        [sg.Button('Move to Unread')]
    ]
    DeleteCol = [
        [sg.Button('Delete Book')]
    ]
    BackCol = [
        [sg.Button('Back')]
    ]

    showReadLayout = [
        [sg.Column(TitleCol, element_justification='center', expand_x=True)],
        [sg.Multiline(size=(80, 30), key='-OUTPUT-', background_color='black', text_color='white', disabled=True, autoscroll=True)],
        [sg.Column(MoveUnreadCol, element_justification='left', expand_x=True)],
        [sg.Column(DeleteCol, element_justification='left', expand_x=True)],
        [sg.Column(BackCol, element_justification='left', expand_x=True)],
        ]
    showReadWindow = sg.Window(title='Personal Library', layout=showReadLayout, margins=(15,75), use_custom_titlebar=True, finalize=True, keep_on_top=True, titlebar_icon=library_icon)

def open_unreadbooks():
    global showUnreadWindow
    # Show Unread Books Menu
    TitleCol = [
        [sg.Text(f'Unread Books', justification='center', font=(1,20))]
    ]
    MoveReadCol = [
        [sg.Button('Move to Read')]
    ]
    DeleteCol = [
        [sg.Button('Delete Book')]
    ]
    BackCol = [
        [sg.Button('Back')]
    ]

    showUnreadLayout = [
        [sg.Column(TitleCol, element_justification='center', expand_x=True)],
        [sg.Multiline(size=(80, 30), key='-OUTPUT-', background_color='black', text_color='white', disabled=True, autoscroll=True)],
        [sg.Column(MoveReadCol, element_justification='left', expand_x=True)],
        [sg.Column(DeleteCol, element_justification='left', expand_x=True)],
        [sg.Column(BackCol, element_justification='left', expand_x=True)],
        ]
    showUnreadWindow = sg.Window(title='Personal Library', layout=showUnreadLayout, margins=(15,75), use_custom_titlebar=True, finalize=True, keep_on_top=True, titlebar_icon=library_icon)

def open_readingbooks():
    global showReadingWindow
    # Show Reading Menu
    TitleCol = [
        [sg.Text(f'Currently Reading', justification='center', font=(1,20))]
    ]
    MoveNotReadingCol = [
        [sg.Button('Move to Not Reading')]
    ]
    PageNumberCol = [
        [sg.Button('Change Page')]
    ]
    DeleteCol = [
        [sg.Button('Delete Book')]
    ]
    BackCol = [
        [sg.Button('Back')]
    ]

    showReadingLayout = [
        [sg.Column(TitleCol, element_justification='center', expand_x=True)],
        [sg.Multiline(size=(80, 30), key='-OUTPUT-', background_color='black', text_color='white', disabled=True, autoscroll=True)],
        [sg.Column(MoveNotReadingCol, element_justification='left', expand_x=True)],
        [sg.Column(PageNumberCol, element_justification='left', expand_x=True)],
        [sg.Column(DeleteCol, element_justification='left', expand_x=True)],
        [sg.Column(BackCol, element_justification='left', expand_x=True)],
        ]
    showReadingWindow = sg.Window(title='Personal Library', layout=showReadingLayout, margins=(15,75), use_custom_titlebar=True, finalize=True, keep_on_top=True, titlebar_icon=library_icon)

def main():
    global Books
    try:
        with open(library_file, 'r') as f:
            Books = json.load(f)
    except:
        pass
    while True:
        main_menu()


main()