from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from .model import Address, Company, Employees, Salary, Tax, Course, Seat, Student, Registration, Discount, Fee, Payment, Package, Penalty, Placement, Batch, Attendance, Assignment, Result, Inquiry, Certification
from .database import get_session


app = FastAPI()
@app.post("/address")
def create_address(address : Address, session : Session  = Depends(get_session)):
    session.add(address)
    session.commit()
    session.refresh(address)
    return address

@app.get("/address{address_id}")
def get_address(address_id : int, session : Session = Depends(get_session)):
    address = session.get(Address,address_id)
    return address

@app.get("/address")
def get_address(session : Session = Depends(get_session)):
    address = session.exec(select(Address)).all()
    return address

@app.delete("/address",status_code = 204)
def delete_address(session : Session = Depends(get_session)):
    address = session.exec(select(Address)).all()
    for address in address:
        session.delete(address)
        session.commit()
    return  {"details": "all address deleted "}

@app.delete("address{address_id}",status_code  = 204)
def delete_address(address_id : int, session : Session = Depends(get_session)):
    address = session.get(Address,address_id)
    if not address:
        raise HTTPException(status_code = 404, details = " address not found")
    session.delete(address)
    session.commit()
    return address

@app.put("/address")
def update_transfer(data: Address, session: Session = Depends(get_session)):
    address =  session.exec(select(Address)).all()
    if not address:
        raise HTTPException(status_code=404, detail="address not found")
    
    update_data = data.dict(exclude_unset=True)

    for a in address:
        for key, value in update_data.items():
            setattr(a, key, value)

    session.commit()

    # [session.refresh(t) for t in transfer]
    for a in address:
        session.refresh(a)

    return address

@app.put("/address/{id}")
def update_address(id: int, data: Address, session: Session = Depends(get_session)):
    address = session.get(Address, id)
    if not address:
        raise HTTPException(status_code=404, detail="address not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(address, key, value)

    session.commit()
    session.refresh(address)
    
    return address

@app.post("/company")
def create_company(company : Company, session: Session = Depends(get_session)):
    session.add(company)
    session.commit()
    session.refresh(company)
    return company

@app.get("/company/{company_id}")
def get_company (company_id : int, session : Session = Depends(get_session)):
    company = session.get(Company,company_id)
    return company

@app.get("/company")
def get_company(session : Session = Depends(get_session)):
    company = session.exec(select(Company)).all()
    return company

@app.delete("/company",status_code = 204)
def delete_company(session : Session = Depends(get_session)):
    company = session.exec(select(Company)).all()
    for company in company:
        session.delete(company)
        session.commit()
    return  {"details": "all company deleted "}

@app.delete("Company{company_id}",status_code  = 204)
def delete_company(company_id : int, session : Session = Depends(get_session)):
    company = session.get(Company,company_id)
    if not company:
        raise HTTPException(status_code = 404, details = " Company not found")
    session.delete(company)
    session.commit()
    return company

@app.put("/company")
def update_company(data: Company, session: Session = Depends(get_session)):
    company =  session.exec(select(Company)).all()
    if not company:
        raise HTTPException(status_code=404, detail="company not found")
    
    update_data = data.dict(exclude_unset=True)

    for c in company:
        for key, value in update_data.items():
            setattr(c, key, value)

    session.commit()

    # [session.refresh(t) for t in transfer]
    for c in company:
        session.refresh(c)

    return company

@app.put("/company/{id}")
def update_company(id: int, data :  Company, session: Session = Depends(get_session)):
    company = session.get(company, id)
    if not company:
        raise HTTPException(status_code=404, detail="company not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(company, key, value)

    session.commit()
    session.refresh(company)
    
    return company


@app.post("/Employees")
def create_Employees(employees: Employees, session: Session = Depends(get_session)):
    session.add(employees)
    session.commit()
    session.refresh(employees)
    return employees

@app.get("/employees {_id}")
def get_employees(employees_id : int, session : Session = Depends(get_session)):
    employees = session.get(Employees ,employees_id)
    return employees

@app.get("/employees")
def get_employees(session : Session = Depends(get_session)):
    employees = session.exec(select(Employees)).all()
    return employees

@app.delete("/employees",status_code = 204)
def delete_employees(session : Session = Depends(get_session)):
    employees = session.exec(select(Employees)).all()
    for employees in employees:
        session.delete(employees)
        session.commit()
    return  {"details": "all employees deleted "}

@app.delete("employees{employees_id}",status_code  = 204)
def delete_employees_id(employees_id : int, session : Session = Depends(get_session)):
    employees = session.get(Employees,employees_id)
    if not employees:
        raise HTTPException(status_code = 404, details = "employees not found")
    session.delete(employees)
    session.commit()
    return employees

@app.put("/employees")
def update_employees(data: Employees, session: Session = Depends(get_session)):
    employees =  session.exec(select(Employees)).all()
    if not employees:
        raise HTTPException(status_code=404, detail="employees not found")
    
    update_data = data.dict(exclude_unset=True)

    for e in employees:
        for key, value in update_data.items():
            setattr(e, key, value)

    session.commit()

    # [session.refresh(t) for t in transfer]
    for e in employees:
        session.refresh(e)

    return employees

@app.put("/employees/{id}")
def update_employees(id: int, data : Employees, session: Session = Depends(get_session)):
    employees = session.get(Employees, id)
    if not employees:
        raise HTTPException(status_code=404, detail="employees not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(employees, key, value)

    session.commit()
    session.refresh(employees)
    
    return employees 





@app.post("/salary")
def create_salary(salary: Salary, session: Session = Depends(get_session)):
    session.add(salary)
    session.commit()
    session.refresh(salary)
    return salary

@app.get("/salary {_id}")
def get_salary(salary_id : int, session : Session = Depends(get_session)):
    salary = session.get(Salary ,salary_id)
    return salary

@app.get("/salary")
def get_salary(session : Session = Depends(get_session)):
    salary = session.exec(select(Salary)).all()
    return salary

@app.delete("/salary",status_code = 204)
def delete_salary(session : Session = Depends(get_session)):
    salary = session.exec(select(Salary)).all()
    for salary in salary:
        session.delete(salary)
        session.commit()
    return  {"details": "all salary deleted "}

@app.delete("salary{salary_id}",status_code  = 204)
def delete_salary(salary_id : int, session : Session = Depends(get_session)):
    salary = session.get(Salary,salary_id)
    if not salary:
        raise HTTPException(status_code = 404, details = "salary not found")
    session.delete(salary)
    session.commit()
    return salary

@app.put("/salary")
def update_salary(data: Salary, session: Session = Depends(get_session)):
   salary =  session.exec(select(Salary)).all()
   if not salary:
        raise HTTPException(status_code=404, detail="salary not found")
    
   update_data = data.dict(exclude_unset=True)

   for s in salary:
        for key, value in update_data.items():
            setattr(s, key, value)

   session.commit()

    # [session.refresh(t) for t in transfer]
   for s in salary:
        session.refresh(s)

   return salary

@app.put("/salary/{id}")
def update_salary(id: int, data : Salary, session: Session = Depends(get_session)):
    salary = session.get(Salary, id)
    if not salary:
        raise HTTPException(status_code=404, detail="salary not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(salary, key, value)

    session.commit()
    session.refresh(salary)
    
    return salary 




@app.post("/Tax")
def create_Tax(tax: Tax, session: Session = Depends(get_session)):
    session.add(tax)
    session.commit()
    session.refresh(tax)
    return tax

@app.get("/tax {_id}")
def get_tax(tax_id : int, session : Session = Depends(get_session)):
    tax = session.get(Tax,tax_id)
    return tax

@app.get("/tax")
def get_tax(session : Session = Depends(get_session)):
    tax = session.exec(select(Tax)).all()
    return tax

@app.delete("/tax",status_code = 204)
def delete_tax(session : Session = Depends(get_session)):
    tax = session.exec(select(Tax)).all()
    for tax in tax:
        session.delete(tax)
        session.commit()
    return  {"details": "all tax deleted "}

@app.delete("tax{tax_id}",status_code  = 204)
def delete_tax(tax_id : int, session : Session = Depends(get_session)):
    tax = session.get(Tax,tax_id)
    if not tax:
        raise HTTPException(status_code = 404, details = "tax not found")
    session.delete(tax)
    session.commit()
    return tax

@app.put("/tax")
def update_tax(data: Tax, session: Session = Depends(get_session)):
   tax =  session.exec(select(Tax)).all()
   if not tax:
        raise HTTPException(status_code=404, detail="tax not found")
     
   update_data = data.dict(exclude_unset=True)

   for ta in tax:
        for key, value in update_data.items():
            setattr(ta, key, value)

   session.commit()

    # [session.refresh(t) for t in transfer]
   for ta in tax:
        session.refresh(ta)

   return tax

@app.put("/tax/{id}")
def update_tax(id: int, data : Tax, session: Session = Depends(get_session)):
    tax = session.get(Tax, id)
    if not tax:
        raise HTTPException(status_code=404, detail="tax not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(tax, key, value)

    session.commit()
    session.refresh(tax)
    
    return tax




@app.post("/Course")
def create_course(course: Course, session: Session = Depends(get_session)):
    session.add(course)
    session.commit()
    session.refresh(course)
    return course

@app.get("/course{course_id}")
def get_tax(course_id : int, session : Session = Depends(get_session)):
    course = session.get(Course,course_id)
    return course

@app.get("/course")
def get_course(session : Session = Depends(get_session)):
    course = session.exec(select(Course)).all()
    return course

@app.delete("/course",status_code = 204)
def delete_course(session : Session = Depends(get_session)):
    course = session.exec(select(Course)).all()
    for course in course:
        session.delete(course)
        session.commit()
    return  {"details": "all course deleted "}

@app.delete("course{course_id}",status_code  = 204)
def delete_course(course_id : int, session : Session = Depends(get_session)):
    tax = session.get(Course,course_id)
    if not tax:
        raise HTTPException(status_code = 404, details = "course not found")
    session.delete(tax)
    session.commit()
    return tax

@app.put("/course")
def update_tax(data: Course, session: Session = Depends(get_session)):
   course =  session.exec(select(Course)).all()
   if not course:
        raise HTTPException(status_code=404, detail="course not found")
     
   update_data = data.dict(exclude_unset=True)

   for c in course:
        for key, value in update_data.items():
            setattr(c, key, value)

   session.commit()

    # [session.refresh(t) for t in transfer]
   for c in course:
        session.refresh(c)

   return course

@app.put("/course/{course_id}")
def update_course(id: int, data : Course, session: Session = Depends(get_session)):
    course = session.get(Course, id)
    if not course:
        raise HTTPException(status_code=404, detail="course not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(course, key, value)

    session.commit()
    session.refresh(course)
    
    return course





@app.post("/seat")
def create_seat(seat: Seat, session: Session = Depends(get_session)):
    session.add(seat)
    session.commit()
    session.refresh(seat)
    return seat

@app.get("/seat{seat_id}")
def get_seat(seat_id : int, session : Session = Depends(get_session)):
    seat = session.get(Seat,seat_id)
    return Seat

@app.get("/seat")
def get_seat(session : Session = Depends(get_session)):
    seat = session.exec(select(Seat)).all()
    return seat

@app.delete("/seat",status_code = 204)
def delete_seat(session : Session = Depends(get_session)):
    seat = session.exec(select(Seat)).all()
    for seat in seat:
        session.delete(seat)
        session.commit()
    return  {"details": "all seat deleted "}

@app.delete("seat{seat_id}",status_code  = 204)
def delete_seat(seat_id : int, session : Session = Depends(get_session)):
    seat = session.get(Seat,seat_id)
    if not seat:
        raise HTTPException(status_code = 404, details = "seat not found")
    session.delete(seat)
    session.commit()
    return seat

@app.put("/seat")
def update_tax(data: Seat, session: Session = Depends(get_session)):
   seat =  session.exec(select(Seat)).all()
   if not seat:
        raise HTTPException(status_code=404, detail="seat not found")
     
   update_data = data.dict(exclude_unset=True)

   for se in seat:
        for key, value in update_data.items():
            setattr(se, key, value)

   session.commit()

    # [session.refresh(t) for t in transfer]
   for se in seat:
        session.refresh(se)

   return seat

@app.put("/seat/{seat_id}")
def update_seat(seat_id: int, data : Seat, session: Session = Depends(get_session)):
    seat = session.get(Seat,seat_id)
    if not seat:
        raise HTTPException(status_code=404, detail="seat not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(seat, key, value)

    session.commit()
    session.refresh(seat)
    
    return seat


@app.post("/Student")
def create_seat(student: Student, session: Session = Depends(get_session)):
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

@app.get("/Student{student_id}")
def get_Student(student_id : int, session : Session = Depends(get_session)):
    student = session.get(Student,student_id)
    return student

@app.get("/Student")
def get_Student(session : Session = Depends(get_session)):
    student = session.exec(select(Student)).all()
    return student

@app.delete("/Student",status_code = 204)
def delete_Student(session : Session = Depends(get_session)):
    student = session.exec(select(Student)).all()
    for student in student:
        session.delete(student)
        session.commit()
    return  {"details": "all Student deleted "}

@app.delete("Student{Student_id}",status_code  = 204)
def delete_Student(Student_id : int, session : Session = Depends(get_session)):
    student = session.get(Student,Student_id)
    if not student:
        raise HTTPException(status_code = 404, details = "student not found")
    session.delete(student)
    session.commit()
    return student

@app.put("/student")
def update_student(data: Student, session: Session = Depends(get_session)):
   student =  session.exec(select(Student)).all()
   if not student:
        raise HTTPException(status_code=404, detail="student not found")
     
   update_data = data.dict(exclude_unset=True)

   for st in student:
        for key, value in update_data.items():
            setattr(st, key, value)

   session.commit()

    # [session.refresh(t) for t in transfer]
   for st in student:
        session.refresh(st)

   return student

@app.put("/student/{student_id}")
def update_course(student_id: int, data : Student, session: Session = Depends(get_session)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="student not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(student, key, value)

    session.commit()
    session.refresh(student)
    
    return student







@app.post("/registration")
def create_registration(registration: Registration, session: Session = Depends(get_session)):
    session.add(registration)
    session.commit()
    session.refresh(registration)
    return registration

@app.get("/registration{registration_id}")
def get_registration(registration_id : int, session : Session = Depends(get_session)):
    registration = session.get(Registration,registration_id)
    return registration

@app.get("/registration")
def get_registration(session : Session = Depends(get_session)):
    registration = session.exec(select(Registration)).all()
    return registration

@app.delete("/registration",status_code = 204)
def delete_registration(session : Session = Depends(get_session)):
    registration = session.exec(select(Registration)).all()
    for registration in registration:
        session.delete(registration)
        session.commit()
    return  {"details": "all registration deleted "}

@app.delete("registration{registration_id}",status_code  = 204)
def delete_registration(registration_id : int, session : Session = Depends(get_session)):
    registration = session.get(Registration,registration_id)
    if not registration:
        raise HTTPException(status_code = 404, details = "registration not found")
    session.delete(registration)
    session.commit()
    return registration

@app.put("/registration")
def update_registration(data: Registration, session: Session = Depends(get_session)):
   registration =  session.exec(select(Registration)).all()
   if not registration:
        raise HTTPException(status_code=404, detail="registration not found")
     
   update_data = data.dict(exclude_unset=True)

   for r in registration:
        for key, value in update_data.items():
            setattr(r, key, value)

   session.commit()

    # [session.refresh(t) for t in transfer]
   for r in registration:
        session.refresh(r)

   return registration

@app.put("/registration/{registration_id}")
def update_registration(registration_id: int, data : Registration, session: Session = Depends(get_session)):
    registration = session.get(Registration, registration_id)
    if not registration:
        raise HTTPException(status_code=404, detail="registration not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(registration, key, value)

    session.commit()
    session.refresh(registration)
    
    return registration




@app.post("/Discount")
def create_discount(discount: Discount, session: Session = Depends(get_session)):
    session.add(discount)
    session.commit()
    session.refresh(discount)
    return discount

@app.get("/discount{discount_id}")
def get_discount(discount_id : int, session : Session = Depends(get_session)):
    discount =  session.get(Discount,discount_id)
    return discount

@app.get("/discount")
def get_discount(session : Session = Depends(get_session)):
    discount = session.exec(select(Discount)).all()
    return discount

@app.delete("/discount",status_code = 204)
def delete_discount(session : Session = Depends(get_session)):
    discount = session.exec(select(Discount)).all()
    for discount in discount:
        session.delete(discount)
        session.commit()
    return  {"details": "all discount deleted "}

@app.delete("discount{discount_id}",status_code  = 204)
def delete_discount(discount_id : int, session : Session = Depends(get_session)):
    discount = session.get(Discount,discount_id)
    if not discount:
        raise HTTPException(status_code = 404, details = "discount not found")
    session.delete(discount)
    session.commit()
    return discount

@app.put("/discount")
def update_discount(data: Discount, session: Session = Depends(get_session)):
   discount  =  session.exec(select(Discount)).all()
   if not discount:
        raise HTTPException(status_code=404, detail="discount not found")
     
   update_data = data.dict(exclude_unset=True)

   for d in discount:
        for key, value in update_data.items():
            setattr(d, key, value)

   session.commit()

    # [session.refresh(t) for t in transfer]
   for d in discount:
        session.refresh(d)

   return discount


@app.put("/discount/{discount_id}")
def update_discount(discount_id: int, data : Discount, session: Session = Depends(get_session)):
   discount = session.get(Discount, discount_id)
   if not discount:
        raise HTTPException(status_code=404, detail="discount not found")
    
   for key, value in data.dict(exclude_unset=True).items():
        setattr(discount, key, value)
   session.commit()
   session.refresh(discount)
    
   return discount


@app.post("/Penalty")
def create_penalty(penalty: Penalty, session: Session = Depends(get_session)):
    session.add(penalty)
    session.commit()
    session.refresh(penalty)
    return penalty

@app.get("/penalty{penalty_id}")
def get_penalty(penalty_id : int, session : Session = Depends(get_session)):
    penalty =  session.get(Penalty,penalty_id)
    return penalty
@app.get("/penalty")
def get_penalty(session : Session = Depends(get_session)):
    penalty = session.exec(select(Penalty)).all()
    return penalty

@app.delete("/penalty",status_code = 204)
def delete_penalty(session : Session = Depends(get_session)):
    penalty = session.exec(select(Penalty)).all()
    for penalty in penalty:
        session.delete(penalty)
        session.commit()
    return  {"details": "all penalty deleted "}

@app.delete("penalty{penalty_id}",status_code  = 204)
def delete_penalty(penalty_id : int, session : Session = Depends(get_session)):
    penalty = session.get(Penalty,penalty_id)
    if not penalty:
        raise HTTPException(status_code = 404, details = "penalty not found")
    session.delete(penalty)
    session.commit()
    return penalty

@app.put("/penalty")
def update_penalty(data: Penalty, session: Session = Depends(get_session)):
   penalty  =  session.exec(select(Penalty)).all()
   if not  penalty:
        raise HTTPException(status_code=404, detail=" penalty not found")
     
   update_data = data.dict(exclude_unset=True)

   for p in  penalty:
        for key, value in update_data.items():
            setattr(p, key, value)

   session.commit()

    # [session.refresh(t) for t in transfer]
   for p in  penalty:
        session.refresh(p)

   return  penalty


@app.put("/penalty/{penalty_id}")
def update_penalty(penalty_id: int, data :  Penalty, session: Session = Depends(get_session)):
    penalty = session.get(Penalty, penalty_id)
    if not  penalty:
        raise HTTPException(status_code=404, detail="penalty not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(penalty, key, value)
    session.commit()
    session.refresh(penalty)
    
    return  penalty







@app.post("/Fee")
def create_Fee(fee : Fee, session: Session = Depends(get_session)):
    session.add(fee)
    session.commit()
    session.refresh(fee)
    return fee

@app.get("/fee{_id}")
def get_fee(fee_id : int, session : Session = Depends(get_session)):
    fee  =  session.get(Fee,fee_id)
    return fee
@app.get("/fee")
def get_fee(session : Session = Depends(get_session)):
    fee = session.exec(select(Fee)).all()
    return fee

@app.delete("/fee",status_code = 204)
def delete_fee(session : Session = Depends(get_session)):
    fee = session.exec(select(Fee)).all()
    for fee in fee:
        session.delete(fee)
        session.commit()
    return  {"details": "all fee deleted "}

@app.delete("fee{fee_id}",status_code  = 204)
def delete_fee(fee_id : int, session : Session = Depends(get_session)):
    fee = session.get(Fee,fee_id)
    if not fee:
        raise HTTPException(status_code = 404, details = "fee not found")
    session.delete(fee)
    session.commit()
    return fee

@app.put("/fee")
def update_Fee(data: Fee, session: Session = Depends(get_session)):
   fee =  session.exec(select(Fee)).all()
   if not  fee:
        raise HTTPException(status_code=404, detail=" fee not found")
     
   update_data = data.dict(exclude_unset=True)

   for f in  fee:
        for key, value in update_data.items():
            setattr(f, key, value)

   session.commit()

    # [session.refresh(t) for t in transfer]
   for f in  fee:
        session.refresh(f)

   return  fee


@app.put("/fee/{id}")
def update_penalty(id: int, data : Fee, session: Session = Depends(get_session)):
    fee = session.get(Fee, id)
    if not  fee:
        raise HTTPException(status_code=404, detail="fee not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(fee, key, value)
    session.commit()
    session.refresh(fee)
    
    return  fee





@app.post("/Payment")
def create_Payment(payment : Payment, session: Session = Depends(get_session)):
    session.add(payment)
    session.commit()
    session.refresh(payment)
    return payment

@app.get("/payment{_id}")
def get_payment(payment_id : int, session : Session = Depends(get_session)):
    payment  =  session.get(Payment,payment_id)
    return payment
@app.get("/payment")
def get_payment(session : Session = Depends(get_session)):
    payment = session.exec(select(Payment)).all()
    return payment

@app.delete("/payment",status_code = 204)
def delete_payment(session : Session = Depends(get_session)):
    payment = session.exec(select(Payment)).all()
    for payment in payment:
        session.delete(Payment)
        session.commit()
    return  {"details": "all payment deleted "}

@app.delete("payment{payment_id}",status_code  = 204)
def delete_payment(payment_id : int, session : Session = Depends(get_session)):
    payment = session.get(Payment,payment_id)
    if not payment:
        raise HTTPException(status_code = 404, details = "payment not found")
    session.delete(payment)
    session.commit()
    return payment

@app.put("/payment")
def update_payment(data: Payment, session: Session = Depends(get_session)):
   payment =  session.exec(select(Payment)).all()
   if not  payment:
        raise HTTPException(status_code=404, detail=" payment not found")
     
   update_data = data.dict(exclude_unset=True)

   for p in  payment:
        for key, value in update_data.items():
            setattr(p, key, value)

   session.commit()

    # [session.refresh(t) for t in transfer]
   for p in  payment:
        session.refresh(p)

   return  payment


@app.put("/payment/{id}")
def update_payment(id: int, data : Payment, session: Session = Depends(get_session)):
    payment = session.get(Payment, id)
    if not  payment:
        raise HTTPException(status_code=404, detail="payment not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(payment, key, value)
    session.commit()
    session.refresh(payment)
    
    return  payment





@app.post("/Certification")
def create_Certification(certification : Certification, session: Session = Depends(get_session)):
    session.add(certification)
    session.commit()
    session.refresh(certification)
    return certification

@app.get("/certification{_id}")
def get_certification(certification_id : int, session : Session = Depends(get_session)):
    certification  =  session.get(Certification,certification_id)
    return certification
@app.get("/certification")
def get_certification(session : Session = Depends(get_session)):
    certification = session.exec(select(Certification)).all()
    return certification

@app.delete("/certification",status_code = 204)
def delete_certification(session : Session = Depends(get_session)):
    certification = session.exec(select(Certification)).all()
    for certification in certification:
        session.delete(certification)
        session.commit()
    return  {"details": "all certification deleted "}

@app.delete("certification{certification_id}",status_code  = 204)
def delete_certification(certification_id : int, session : Session = Depends(get_session)):
    certification = session.get(Certification,certification_id)
    if not certification:
        raise HTTPException(status_code = 404, details = "certification not found")
    session.delete(certification)
    session.commit()
    return certification

@app.put("/certification")
def update_certification(data: Certification, session: Session = Depends(get_session)):
   certification =  session.exec(select(Certification)).all()
   if not  certification:
        raise HTTPException(status_code=404, detail=" certification not found")
     
   update_data = data.dict(exclude_unset=True)

   for ce in  certification:
        for key, value in update_data.items():
            setattr(ce, key, value)

   session.commit()

    # [session.refresh(t) for t in transfer]
   for ce in  certification:
        session.refresh(ce)

   return  certification

@app.put("/certification/{id}")
def update_certification(id: int, data : Certification, session: Session = Depends(get_session)):
    certification = session.get(certification, id)
    if not  certification:
        raise HTTPException(status_code=404, detail="certification not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(certification, key, value)
    session.commit()
    session.refresh(certification)
    
    return  certification







@app.post("/Placement")
def create_Placement(placement : Placement, session: Session = Depends(get_session)):
    session.add(placement)
    session.commit()
    session.refresh(placement)
    return placement

@app.get("/placement{_id}")
def get_placement(placement_id : int, session : Session = Depends(get_session)):
    placement =  session.get(Placement,placement_id)
    return placement
@app.get("/placement")
def get_placementn(session : Session = Depends(get_session)):
    placement = session.exec(select(Placement)).all()
    return placement
@app.delete("/placement",status_code = 204)
def delete_placement(session : Session = Depends(get_session)):
    placement = session.exec(select(Placement)).all()
    for placement in placement:
        session.delete(placement)
        session.commit()
    return  {"details": "all placement deleted "}

@app.delete("placement{placement_id}",status_code  = 204)
def delete_placement(placement_id : int, session : Session = Depends(get_session)):
    placement = session.get(Placement,placement_id)
    if not placement:
        raise HTTPException(status_code = 404, details = "placement not found")
    session.delete(placement)
    session.commit()
    return placement

@app.put("/placement")
def update_placement(data: Placement, session: Session = Depends(get_session)):
   placement =  session.exec(select(placement)).all()
   if not  placement:
        raise HTTPException(status_code=404, detail=" placement not found")
     
   update_data = data.dict(exclude_unset=True)

   for pla in  placement:
        for key, value in update_data.items():
            setattr(pla, key, value)

   session.commit()

    # [session.refresh(t) for t in transfer]
   for pla in  placement:
        session.refresh(pla)

   return  placement

@app.put("/placement/{id}")
def update_placement(id: int, data : Placement, session: Session = Depends(get_session)):
    placement = session.get(Placement, id)
    if not  placement:
        raise HTTPException(status_code=404, detail="placement not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(placement, key, value)
    session.commit()
    session.refresh(placement)
    
    return  placement





@app.post("/Package")
def create_Package(package : Package, session: Session = Depends(get_session)):
    session.add(package)
    session.commit()
    session.refresh(package)
    return package

@app.get("/package{package_id}")
def get_package(package_id : int, session : Session = Depends(get_session)):
    package =  session.get(Package,package_id)
    return package
@app.get("/package")
def get_package(session : Session = Depends(get_session)):
    package = session.exec(select(Package)).all()
    return package
@app.delete("/package",status_code = 204)
def delete_package(session : Session = Depends(get_session)):
    package = session.exec(select(Package)).all()
    for package in package:
        session.delete(package)
        session.commit()
    return  {"details": "all package deleted "}

@app.delete("package{package_id}",status_code  = 204)
def delete_package(package_id : int, session : Session = Depends(get_session)):
    package = session.get(Package,package_id)
    if not package:
        raise HTTPException(status_code = 404, details = "package not found")
    session.delete(package)
    session.commit()
    return package
@app.put("/package")
def update_package(data: Package, session: Session = Depends(get_session)):
   package =  session.exec(select(Package)).all()
   if not  package:
        raise HTTPException(status_code=404, detail=" package not found")
     
   update_data = data.dict(exclude_unset=True)

   for pa in package:
        for key, value in update_data.items():
            setattr(pa, key, value)

   session.commit()

    # [session.refresh(t) for t in transfer]
   for pa in  package:
        session.refresh(pa)

   return  package

@app.put("/package/{id}")
def update_package(id: int, data : Package, session: Session = Depends(get_session)):
    package = session.get(Package, id)
    if not package:
        raise HTTPException(status_code=404, detail="package not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(package, key, value)
    session.commit()
    session.refresh(package)
    
    return  package





@app.post("/Batch")
def create_Batch(batch : Batch, session: Session = Depends(get_session)):
    session.add(batch)
    session.commit()
    session.refresh(batch)
    return batch

@app.get("/batch{batch_id}")
def get_batch(batch_id : int, session : Session = Depends(get_session)):
    batch =  session.get(Batch,batch_id)
    return batch
@app.get("/batch")
def get_batch(session : Session = Depends(get_session)):
    batch = session.exec(select(Batch)).all()
    return batch
@app.delete("/batch",status_code = 204)
def delete_batch(session : Session = Depends(get_session)):
    batch = session.exec(select(Batch)).all()
    for batch in batch:
        session.delete(batch)
        session.commit()
    return  {"details": "all batch deleted "}

@app.delete("batch{batch_id}",status_code  = 204)
def delete_batch(batch_id : int, session : Session = Depends(get_session)):
    batch = session.get(Batch,batch_id)
    if not batch:
        raise HTTPException(status_code = 404, details = "batch not found")
    session.delete(batch)
    session.commit()
    return batch
@app.put("/batch")
def update_batch(data: Batch, session: Session = Depends(get_session)):
   batch =  session.exec(select(Batch)).all()
   if not  batch:
        raise HTTPException(status_code=404, detail=" batch not found")
     
   update_data = data.dict(exclude_unset=True)

   for b in batch:
        for key, value in update_data.items():
            setattr(b, key, value)

   session.commit()

    # [session.refresh(t) for t in transfer]
   for b in  batch:
        session.refresh(b)

   return batch

@app.put("/batch/{id}")
def update_batch(id: int, data : Batch, session: Session = Depends(get_session)):
    batch = session.get(Batch, id)
    if not batch:
        raise HTTPException(status_code=404, detail="batch not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(batch, key, value)
    session.commit()
    session.refresh(batch)
    
    return  batch


@app.post("/Attendance")
def create_Batch(attendance : Attendance, session: Session = Depends(get_session)):
    session.add(attendance)
    session.commit()
    session.refresh(attendance)
    return attendance

@app.get("/attendance{attendance_id}")
def get_attendance(attendance_id : int, session : Session = Depends(get_session)):
    attendance =  session.get(Attendance,attendance_id)
    return attendance
@app.get("/attendance")
def get_attendance(session : Session = Depends(get_session)):
    attendance = session.exec(select(Attendance)).all()
    return attendance
@app.delete("/attendance",status_code = 204)
def delete_attendance(session : Session = Depends(get_session)):
    attendance = session.exec(select(Attendance)).all()
    for attendance in attendance:
        session.delete(attendance)
        session.commit()
    return  {"details": "all attendance deleted "}

@app.delete("attendance{attendance_id}",status_code  = 204)
def delete_attendance(attendance_id : int, session : Session = Depends(get_session)):
    attendance = session.get(Attendance,attendance_id)
    if not attendance:
        raise HTTPException(status_code = 404, details = "attendance not found")
    session.delete(attendance)
    session.commit()
    return attendance
@app.put("/attendance")
def update_attendance(data: Attendance, session: Session = Depends(get_session)):
   attendance =  session.exec(select(attendance)).all()
   if not  attendance:
        raise HTTPException(status_code=404, detail=" attendance not found")
     
   update_data = data.dict(exclude_unset=True)

   for a in attendance:
        for key, value in update_data.items():
            setattr(a, key, value)

   session.commit()

    # [session.refresh(t) for t in transfer]
   for a in  attendance:
        session.refresh(a)

   return attendance

@app.put("/attendance/{id}")
def update_attendance(id: int, data : Attendance, session: Session = Depends(get_session)):
    attendance = session.get(attendance, id)
    if not attendance:
        raise HTTPException(status_code=404, detail="attendance not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(attendance, key, value)
    session.commit()
    session.refresh(attendance)
    
    return attendance






@app.post("/Assignment")
def create_Assignment(assignment : Assignment, session: Session = Depends(get_session)):
    session.add(assignment)
    session.commit()
    session.refresh(assignment)
    return assignment

@app.get("/assignment{assignment_id}")
def get_assignment(assignment_id : int, session : Session = Depends(get_session)):
    assignment =  session.get(Assignment,assignment_id)
    return assignment
@app.get("/assignment")
def get_assignment(session : Session = Depends(get_session)):
    assignment = session.exec(select(Assignment)).all()
    return assignment
@app.delete("/assignment",status_code = 204)
def delete_assignment(session : Session = Depends(get_session)):
    assignment = session.exec(select(assignment)).all()
    for assignment in assignment:
        session.delete(assignment)
        session.commit()
    return  {"details": "all assignment deleted "}

@app.delete("assignment{assignment_id}",status_code  = 204)
def delete_assignment(assignment_id : int, session : Session = Depends(get_session)):
    assignment = session.get(assignment,assignment_id)
    if not assignment:
        raise HTTPException(status_code = 404, details = "assignment not found")
    session.delete(assignment)
    session.commit()
    return assignment
@app.put("/assignment")
def update_assignment(data: Assignment, session: Session = Depends(get_session)):
   assignment =  session.exec(select(Assignment)).all()
   if not  assignment:
        raise HTTPException(status_code=404, detail=" assignment not found")
     
   update_data = data.dict(exclude_unset=True)

   for ass in assignment:
        for key, value in update_data.items():
            setattr(ass, key, value)

   session.commit()

    # [session.refresh(t) for t in transfer]
   for ass in  assignment:
        session.refresh(ass)

   return assignment

@app.put("/assignment/{id}")
def update_assignment(id: int, data : Assignment, session: Session = Depends(get_session)):
    assignment = session.get(Assignment, id)
    if not assignment:
        raise HTTPException(status_code=404, detail="assignment not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(assignment, key, value)
    session.commit()
    session.refresh(assignment)
    
    return  assignment



@app.post("/Result")
def create_Result(result : Result, session: Session = Depends(get_session)):
    session.add(result)
    session.commit()
    session.refresh(result)
    return result

@app.get("/result{result_id}")
def get_result(result_id : int, session : Session = Depends(get_session)):
    result =  session.get(Result,result_id)
    return result
@app.get("/result")
def get_result(session : Session = Depends(get_session)):
    result = session.exec(select(Result)).all()
    return result
@app.delete("/result",status_code = 204)
def delete_result(session : Session = Depends(get_session)):
    result = session.exec(select(Result)).all()
    for result in result:
        session.delete(result)
        session.commit()
    return  {"details": "all result deleted "}

@app.delete("result{result_id}",status_code  = 204)
def delete_result(package_id : int, session : Session = Depends(get_session)):
    result = session.get(Result,package_id)
    if not result:
        raise HTTPException(status_code = 404, details = "result not found")
    session.delete(result)
    session.commit()
    return result
@app.put("/result")
def update_result(data: Result, session: Session = Depends(get_session)):
   result =  session.exec(select(Result)).all()
   if not  result:
        raise HTTPException(status_code=404, detail=" result not found")
     
   update_data = data.dict(exclude_unset=True)

   for r in result:
        for key, value in update_data.items():
            setattr(r, key, value)

   session.commit()

    # [session.refresh(t) for t in transfer]
   for r in  result:
        session.refresh(r)

   return  r

@app.put("/result/{id}")
def update_result(id: int, data : Result, session: Session = Depends(get_session)):
    result = session.get(Result, id)
    if not result:
        raise HTTPException(status_code=404, detail="result not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(result, key, value)
    session.commit()
    session.refresh(result)
    
    return  result

@app.post("/Inquiry")
def create_Inquiry(inquiry : Inquiry, session: Session = Depends(get_session)):
    session.add(inquiry )
    session.commit()
    session.refresh(inquiry)
    return inquiry
@app.get("/inquiry")
def get_inquiry (session : Session = Depends(get_session)):
    inquiry  = session.exec(select(Inquiry )).all()
    return inquiry 

@app.get("/inquiry/{inquiry _id}")
def get_inquiry (inquiry_id : int, session : Session = Depends(get_session)):
    inquiry  =  session.get(Inquiry ,inquiry_id)
    return inquiry 

@app.delete("/inquiry",status_code = 204)
def delete_inquiry (session : Session = Depends(get_session)):
    inquiry  = session.exec(select(Inquiry )).all()
    for inquiry  in inquiry :
        session.delete(inquiry )
        session.commit()
    return  {"details": "all inquiry  deleted "}

@app.delete("inquiry/{inquiry _id}",status_code  = 204)
def delete_inquiry(inquiry_id : int, session : Session = Depends(get_session)):
    inquiry  = session.get(Inquiry ,inquiry_id)
    if not inquiry :
        raise HTTPException(status_code = 404, details = "inquiry  not found")
    session.delete(inquiry)
    session.commit()
    return inquiry 
@app.put("/inquiry/")
def update_inquiry(data: Inquiry , session: Session = Depends(get_session)):
   inquiry  =  session.exec(select(Inquiry)).all()
   if not  inquiry :
        raise HTTPException(status_code=404, detail=" inquiry  not found")
     
   update_data = data.dict(exclude_unset=True)

   for i in inquiry :
        for key, value in update_data.items():
            setattr(i, key, value)

   session.commit()

    # [session.refresh(t) for t in transfer]
   for i in  inquiry :
        session.refresh(i)

   return  i

@app.put("/inquiry/{id}")
def update_inquiry(id: int, data : Inquiry , session: Session = Depends(get_session)):
    inquiry  = session.get(Inquiry , id)
    if not inquiry :
        raise HTTPException(status_code=404, detail="inquiry  not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(inquiry , key, value)
    session.commit()
    session.refresh(inquiry )
    
    return inquiry
 
