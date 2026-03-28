from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, time, date



class Address(SQLModel, table = True):
    """Schema for storing address."""
    id : int | None = Field(default = None, primary_key = True)
    name : str  | None  = Field(default = None)
    city : str  | None  = Field(default = None)
    district : str | None = Field(default = None)
    state  : str | None = Field(default = None)
    pincode  : int  | None = Field(default = None)
    latitude : float | None = Field(default = None)
    longtitude : float | None = Field(default = None)


class Company(SQLModel, table = True):
    """Schema for storing company."""
    id : int  | None = Field(default = None, primary_key = True)
    name : str | None = Field(default = None)
    email : str | None = Field(index = True, unique = True)
    address_id : int | None = Field(default = None, foreign_key = "address.id")
    address : Address | None = Relationship()
    phone : str | None = Field(default = None)
    type : str | None  = Field(default = None)
    total_hiring : int | None = Field(default = None)
    opening_time : time | None = Field(default = None)
    closing_time : time | None = Field(default = None)


class Employee(SQLModel, table = True):
    """Schema for storing employees."""
    id : int  | None = Field(default = None, primary_key = True)
    name : str | None = Field(default = None)
    email : str | None = Field(index = True, unique = True)
    password : str | None = Field(index = True, unique = True)
    address_id : int | None = Field(default = None, foreign_key = "address.id")
    address : Address | None = Relationship()
    phone : str | None = Field(default = None)
    qualification : str | None = Field(default = None)
    bgv : str | None = Field(default = None)
    experience : int | None =  Field(default = None)
    specialization : str | None = Field(default = None)
    designation : str | None = Field(default = None)
    work_location : str | None = Field(default = None)
    company_id : int | None  = Field(default = None, foreign_key = "company.id")
    company : Company | None = Relationship()
    

class Salary(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    employees_id: int | None = Field(default=None, foreign_key="employees.id")
    employees: Employee | None = Relationship()
    amount: int | None = Field(default=None)


class Tax(SQLModel, table = True):
    """Schema for storing tax."""
    id : int | None = Field(default = None, primary_key = True)
    pf : int | None = Field(default = None)
    house_allowance : int | None = Field(default = None)
    slab : int | None = Field(default = None)


class Course(SQLModel, table = True):
    """Schema for storing course."""
    id : int | None = Field(default = None, primary_key = True)
    name : str | None = Field(default = None)
    duration  : str | None = Field(default = None)
    type : str | None = Field(default = None)
    status : bool | None = Field(default = None)
    company_id : int | None  = Field(default = None, foreign_key = "company.id")
    company : Company | None = Relationship()


class Seat(SQLModel, table  = True):
    """Schema for storing seat."""
    id : int | None = Field(default = None, primary_key = True)
    course_id  : int | None = Field(default = None, foreign_key  = "course.id")
    course : Course | None = Relationship()
    total_seat  : int | None = Field(default = None)
    available_seat : int  | None = Field(default = None)


class Student(SQLModel, table = True):
    """Schema for storing student."""
    id : int | None = Field(default = None, primary_key = True)
    name : str | None = Field(default = None)
    email : str = Field(index = True, unique = True)
    address_id : int | None = Field(default = None, foreign_key = "address.id")
    address : Address | None = Relationship()
    phone : str | None = Field(default = None)
    qualification : str | None = Field(default = None)
    aadhar_no : str | None = Field(default = None)
    pan_no : str | None = Field(default = None)
    dob : str | None = Field(default  = None)
    course_id  : int | None = Field(default = None, foreign_key  = "course.id")
    course : Course | None = Relationship()


class Registration(SQLModel, table = True):
    """Schema for storing registration."""
    id : int | None = Field(default = None, primary_key = True)
    number : int | None = Field(unique = True)
    student_id : int  | None = Field(default = None, foreign_key = "student.id")
    student : Student | None = Relationship()
    course_id  : int | None = Field(default = None, foreign_key  = "course.id")
    course : Course | None = Relationship()
    company_id : int | None  = Field(default = None, foreign_key = "company.id")
    company : Company | None = Relationship()
    amount : int | None  = Field(default = True)


class Discount(SQLModel, table = True):
    """Schema for storing Discount."""
    id : int | None = Field(default = None, primary_key = True)
    student_id : int  | None = Field(default = None, foreign_key = "student.id")
    student : Student | None = Relationship()
    course_id  : int | None = Field(default = None, foreign_key  = "course.id")
    course : Course | None = Relationship()
    employees_id  : int | None = Field(default = None, foreign_key = "employees.id")
    employess : Employee | None = Relationship()
    percentage : float | None = Field(default = None)


class Penalty(SQLModel, table = True):
    """Schema for storing penalty."""
    id : int | None = Field(default = None, primary_key = True)
    student_id : int  | None = Field(default = None, foreign_key = "student.id")
    student : Student | None = Relationship()
    amount : int | None = Field(default = None)
    status : bool | None = Field(default = None)


class Fee(SQLModel, table = True):
    """Schema for storing fee."""
    id : int | None = Field(default = None, primary_key = True)
    course_id  : int | None = Field(default = None, foreign_key  = "course.id")
    course : Course | None = Relationship()
    type : str | None = Field(default = None)
    penalty_id : int | None = Field(default = None, foreign_key = "penalty.id")
    penalty : Penalty | None = Relationship()
    discount_id  : int | None = Field(default = None, foreign_key = "discount.id")
    discount  : Discount | None = Relationship()
    due : str | None  = Field(default = None)
    amount : int | None = Field(default = None)


class Payment(SQLModel, table = True):
    """Schema for storing payment."""
    id : int | None = Field(default = None, primary_key = True)
    refrence_id : int | None = Field(default = None)
    student_id : int  | None = Field(default = None, foreign_key = "student.id")
    student : Student | None = Relationship()
    type : str  | None = Field(default = None)
    methodes : str | None = Field(default = None)
    payment_time : time | None = Field(default = None)
    status : bool | None = Field(default = None)


class Certification(SQLModel, table = True):
    """Schema for storing Certification."""
    id : int | None = Field(default = None, primary_key = True)
    number : int | None = Field(unique = True)
    student_id : int  | None = Field(default = None, foreign_key = "student.id")
    student : Student | None = Relationship()
    course_id  : int | None = Field(default = None, foreign_key  = "course.id")
    course : Course | None = Relationship()
    company_id : int | None  = Field(default = None, foreign_key = "company.id")
    company : Company | None = Relationship()


class Placement(SQLModel, table = True):
    """Schema for storing Placement."""
    id : int | None = Field(default = None, primary_key = True)
    student_id : int  | None = Field(default = None, foreign_key = "student.id")
    student : Student | None = Relationship()
    course_id  : int | None = Field(default = None, foreign_key  = "course.id")
    course : Course | None = Relationship()
    company_id : int | None  = Field(default = None, foreign_key = "company.id")
    company : Company | None = Relationship()
    total_hiring : int | None = Field(default = None)
    designation : str | None = Field(default = None)


class Package(SQLModel, table = True):
    """Schema for storing Package."""
    id : int | None = Field(default = None, primary_key = True)
    student_id : int  | None = Field(default = None, foreign_key = "student.id")
    student : Student | None = Relationship()
    placement_id : int  | None = Field(default = None, foreign_key = "placement.id")
    placement : Placement | None = Relationship()
    amount : int | None = Field(default = None)
    is_joined : str  | None = Field(default = None)


class Batch(SQLModel, table=True):
    """Schema for storing batch."""
    id: int | None = Field(default=None, primary_key=True)
    course_id  : int | None = Field(default = None, foreign_key  = "course.id")
    course : Course | None = Relationship()
    employees_id  : int | None = Field(default = None, foreign_key = "employees.id")
    employess : Employee | None = Relationship()
    start_date: date | None = Field(default=None)
    end_date: date | None = Field(default=None)
    timing: time | None = Field(default=None)
    capacity: int | None = Field(default=None)


class Attendance(SQLModel, table=True):
    """Schema for storing Attendance."""
    id: int | None = Field(default=None, primary_key=True)
    student_id : int  | None = Field(default = None, foreign_key = "student.id")
    student : Student | None = Relationship()
    batch_id: int | None = Field(default = None, foreign_key="batch.id")
    batch : Batch | None = Relationship()
    a_date: date | None = Field(default=None)
    status: bool | None = Field(default=None) 

class Assignment(SQLModel, table=True):
    """Schema for storing Assignment."""
    id: int | None = Field(default=None, primary_key=True)
    course_id  : int | None = Field(default = None, foreign_key  = "course.id")
    course : Course | None = Relationship()
    title: str | None = Field(default=None)
    max_marks: int | None = Field(default=None)

class Result(SQLModel, table=True):
    """Schema for storing result."""
    id: int | None = Field(default=None, primary_key=True)
    student_id : int  | None = Field(default = None, foreign_key = "student.id")
    student : Student | None = Relationship()
    assignment_id: int | None = Field(default = None, foreign_key="assignment.id")
    assignment : Assignment | None = Relationship()
    marks: int | None = Field(default=None)

class Inquiry(SQLModel, table=True):
    """Schema for storing Inquiry."""
    id: int | None = Field(default=None, primary_key=True)
    name: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    course_interest: str | None = Field(default=None)
    status: bool | None = Field(default=None)


class Feedback(SQLModel, table=True):
    """Schema for storing feedback."""
    id: int | None = Field(default=None, primary_key=True)
    student_id : int  | None = Field(default = None, foreign_key = "student.id")
    student : Student | None = Relationship()
    course_id  : int | None = Field(default = None, foreign_key  = "course.id")
    course : Course | None = Relationship()
    company_id : int | None  = Field(default = None, foreign_key = "company.id")
    company : Company | None = Relationship()
    text: str | None = Field(default=None)
    rating: int | None = Field(default=None)
    created_at : datetime | None = Field(default = None)
    






