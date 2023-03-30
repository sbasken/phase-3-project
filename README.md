### REVIEWER APP

## Description

This is a CLI application for students and teachers to give reviews. 

We have three models: `Student`, `Teacher`, and `Review`.

- A `Student` has many `Review`s. A `Teacher` has many `Review`s. A `Review` belongs to a `Student` and a `Teacher`.

- `Student` - `Teacher` is a many to many relationship.

- Both `Student`s and `Teacher`s alike have the opportunity to leave a review about programs that they are in or teach. 

- `Student`s can see, edit, delete their own `Review`s.
- `Teacher`s can see all `Review`s, filter them by 'program' or see, edit, and delete their own `Review`s.

- In the `Review` class:
 - you can pull and see the reviews that were made with date/time upon when the review was made.

## Instructions

Clone the repository to your local machine:
```
  $ git clone https://github.com/{your-username}/phase-3-project.git
  ```
  
Navigate to the project directory:
```
  $ cd phase-3-project
  ```
  
Install the required packages:
```
  $ pipenv install && pipenv shell
  ```
  
Navigate to the db directory:
```
  $ cd lib/db
  ```

To create the review.db file and navigate the SQLite tables in your code editor, enter:
```
  $ alembic upgrade head
  ```  

Next, run:
```
  $ python db/seed.py
  ```

You can then open 'review.db' with SQLITE.
Now you should be able to see the populated database files.

Navigate back to the lib directory:
```
   $ cd ..
 
  
Run the program using:
```
  $ python cli.py
  ```

Have fun! Make sure to leave a review! 🐣 🥳

## WIREFRAME

![alt text](https://cdn.discordapp.com/attachments/1070016828484636722/1090006999581872228/Screenshot_2023-03-27_at_1.18.11_PM.png)