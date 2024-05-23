class Faculty:
    def __init__(self, name, title, department):
        self.name = name
        self.title = title
        self.department = department

    def __repr__(self):
        return f"Faculty(name={self.name}, title={self.title}, department={self.department})"

class Department:
    def __init__(self, name, faculty_list=None):
        self.name = name
        self.faculty_list = faculty_list if faculty_list is not None else []

    def add_faculty(self, faculty):
        if isinstance(faculty, Faculty):
            self.faculty_list.append(faculty)
        else:
            print("Only Faculty objects can be added")

    def __repr__(self):
        return f"Department(name={self.name}, faculty_list={self.faculty_list})"

class Campus:
    def __init__(self, name, location, departments=None):
        self.name = name
        self.location = location
        self.departments = departments if departments is not None else []

    def add_department(self, department):
        if isinstance(department, Department):
            self.departments.append(department)
        else:
            print("Only Department objects can be added")

    def __repr__(self):
        return f"Campus(name={self.name}, location={self.location}, departments={self.departments})"


# Creating Faculty objects
faculty1 = Faculty(name="Dr. John Doe", title="Professor", department="Computer Science")
faculty2 = Faculty(name="Dr. Jane Smith", title="Associate Professor", department="Mathematics")
faculty3 = Faculty(name="Dr. Emily Brown", title="Assistant Professor", department="Physics")

# Creating Department objects and adding Faculty to them
cs_department = Department(name="Computer Science")
cs_department.add_faculty(faculty1)

math_department = Department(name="Mathematics")
math_department.add_faculty(faculty2)

physics_department = Department(name="Physics")
physics_department.add_faculty(faculty3)

# Creating Campus object and adding Departments to it
main_campus = Campus(name="Main Campus", location="City Center")
main_campus.add_department(cs_department)
main_campus.add_department(math_department)
main_campus.add_department(physics_department)

# Displaying the created objects
print(faculty1)
print(faculty2)
print(faculty3)

print(cs_department)
print(math_department)
print(physics_department)

print(main_campus)