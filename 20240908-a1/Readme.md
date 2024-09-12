# Python Programming Assignment 07

### **Instructions:**
Implement a Python program using **Google Colab** to accomplish the following task.

---

## **Problem Statement: Library Management System**

### **Objective:**
Design a Library Management System using Object-Oriented Programming (OOP) concepts and Python's typing features. The system should support basic CRUD operations (Create, Read, Update, Delete) for books, manage different types of users (Librarians and Members), and handle book borrowing transactions with file-based data persistence. Appropriate error handling for file operations is required.

---

### **Requirements:**

#### **1. Classes and Inheritance:**
- Create a base class `User` with common attributes such as `user_id`, `name`, and `email`.
- Create two child classes:
  - `Librarian`: Should be able to manage (add, update, delete) books in the system.
  - `Member`: Should be able to borrow and return books.

#### **2. Books:**
- Create a `Book` class with attributes such as `book_id`, `title`, `author`, and `availability` (a boolean indicating if the book is available or not).
- Provide methods to display book information.

#### **3. Library Management:**
- Create a `LibraryManager` class to handle CRUD operations for books and users. The class should:
  - Add, update, and delete books.
  - Borrow and return books for members.
  - Read and write book and user data to files.

#### **4. File Handling:**
- Store book and user data in separate files (`books.txt` and `users.txt`).
- Implement error handling for file operations (e.g., file not found, I/O errors).

#### **5. Transactions:**
- Implement a method for members to borrow a book. When a book is borrowed, it should no longer be available for other users until it is returned.
- Implement a method for members to return a book.

#### **6. Encapsulation and Polymorphism:**
- Ensure that class attributes are properly encapsulated (use private attributes where necessary).
- Use polymorphism where appropriate (e.g., methods that behave differently for `Librarian` and `Member`).

#### **7. Static and Class Methods:**
- Use class methods to track the total number of books and users in the system.
- Use static methods where appropriate for utility functions (e.g., validating user emails or checking book availability).

---

### **Expected Features:**

#### **1. User Registration:**
- Users (`Librarian` or `Member`) can be registered to the system and saved in the `users.txt` file.

#### **2. Book Management:**
- Librarians can add, update, and delete books from the system. Changes should be reflected in `books.txt`.

#### **3. Borrowing and Returning:**
- Members can borrow books if they are available. Borrowed books should no longer be listed as available until returned.
- Members can return books, making them available again in the system.

---

### **Example Usage:**

#### **Add a New Book:**
- The librarian adds a new book, "The Great Gatsby" by F. Scott Fitzgerald, and sets its availability to `True`.

#### **Borrow a Book:**
- A member borrows "The Great Gatsby." The system marks the book as unavailable.

#### **Return a Book:**
- The member returns "The Great Gatsby," and the system updates its availability to `True`.

#### **List All Books:**
- The system can display all available books, including their title, author, and availability.

---

### **Instructions for Submission:**
Your implementation should include:
- Class definitions for `User`, `Librarian`, `Member`, `Book`, and `LibraryManager`.
- CRUD operations for managing books and users.
- Proper file handling and error management.

Submit your code (.ipynb file) and sample data files (`books.txt`, `users.txt`).

---

### **Evaluation Criteria:**
- Correct usage of OOP principles (inheritance, encapsulation, polymorphism).
- Correct implementation of file handling for persistent data storage.
- Error handling for file I/O operations.
- Code clarity, readability, and proper usage of Python's typing features.
- Implementation of CRUD operations for books and users.