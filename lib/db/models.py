from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, Float, DateTime, ForeignKey, func)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

# Student Table

class Student(Base):
    __tablename__ = 'students'
    __table_args__ = (PrimaryKeyConstraint('id', name='pk_students'),)

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    program = Column(String())
    email = Column(String())
    phone_number = Column(Integer())
    
    # teacher_id = Column(Integer(), ForeignKey('teachers.id'))
    
    def __repr__(self):
        return f"< ID: {self.id}, " \
            + f"Name: {self.name}, " \
            + f"Program: {self.program}, "\
            + f"Email: {self.email}, "\
            + f"Phone Number: {self.phone_number} >"
    
# Teacher table

class Teacher(Base):
    __tablename__ = 'teachers'
    __table_args__ = (PrimaryKeyConstraint('id', name='pk_teachers'),)

    id = Column(Integer())
    name = Column(String())
    program = Column(String())
    email = Column(String())

    # student_id = Column(Integer(), ForeignKey('students.id'))

def __repr__(self):
    return f"< ID: {self.id}, " \
    + f"Name: {self.name}, " \
    + f"Program: {self.program}, " \
    + f"Email: {self.email} >"
    
    
# Review Table

class Review(Base):
    __tablename__ = 'reviews'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    student_id = Column(Integer(), ForeignKey('students.id'))
    teacher_id = Column(Integer(), ForeignKey('teachers.id'))
    program = Column(String())
    comment = Column(String())
    rating = Column(Float())
    date = Column(DateTime(), server_default=func.now())

    student = relationship('Student', backref=backref("students"))
    teacher = relationship('Teacher', backref=backref("teachers"))
    
    
    def __repr__(self):
        return f"< Id: {self.id}, " \
            + f"Student_ID:{self.student_id}, " \
            + f"Teacher_ID:{self.teacher_id}, " \
            + f"Program: {self.program}, "\
            + f"Coment: {self.comment}, "\
            + f"Email: {self.email} >"