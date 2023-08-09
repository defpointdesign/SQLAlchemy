# SQLAlchemy Object Rational Mapper
# 1. Create Tables
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# 1.1 create engine
engine = create_engine("mysql+mysqlconnector://root:root@192.168.31.62:3312/test", echo=False)

# 1.2 create session
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# 1.3 create table
class Student (Base):
    __tablename__='student'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))

# 1.4 migration
# Base.metadata.create_all(engine)


# 2. Insert Data into Tables
# 2.1 create instance of table Class
student1 = Student(name="Oleksii", age=32, grade="no")
student2 = Student(name="Vadim", age=25, grade="no")
student3 = Student(name="Julia", age=25, grade="no")
student4 = Student(name="illia", age=3, grade="no")
student5 = Student(name="Mavpa", age=5, grade="no")

# 2.2 add data to session
# session.add(student1)
# session.add_all([student2, student3])
# session.add(student4)
# session.add(student5)

# 2.3 commit changes to database
# session.commit()


# 3. Read Data from Table
# 3.1 get all data
# students = session.query(Student)
# for student in students:
#     print(student.name, student.age, student.grade)

# 3.2 get data in order
# students = session.query(Student).order_by(Student.name)
# for student in students:
#     print(student.name)

# 3.3 get data by filtering
# student = session.query(Student).filter(Student.name=="Oleksii").first()
# print(student.name, student.age)
#
# students = session.query(Student).filter(or_(Student.name=="Oleksii", Student.name=="Vadim"))
# for student in students:
#     print(student.name, student.age)
#
# # 3.4 count the number of results
# student_count = session.query(Student).filter(or_(Student.name=="Oleksii", Student.name=="Vadim"))
# print(student_count)

# 4. Update Data in Table
# student = session.query(Student).filter(Student.name=="Mavpa").first()  # 4.1 get record
# student.name = "Slon"  # 4.2 change value
# session.commit()  # 4.3 commit change

# 5. Delete Data in Table
student = session.query(Student).filter(Student.name=="Julia").first()  # 4.1 get record # 5.1 get record
session.delete(student)  # 5.2 delete record
session.commit()  # 5.3 commit change

