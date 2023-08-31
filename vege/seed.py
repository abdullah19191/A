import random
from faker import Faker


# Import the Student model
from .models import *


def seed_students(num_students):
    fake = Faker()
    departments = Department.objects.all()

    for _ in range(num_students):
        department = random.choice(departments)
        student_id = f"STU-0{random.randint(100,999)}"
        student_id_obj = StudentID.objects.create(student_id=student_id)
        Student.objects.create(
            department=department,
            student_id=student_id_obj,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            age=random.randint(18, 40),
            address=fake.address(),
        )


if __name__ == "__main__":
    num_students_to_generate = 20
    seed_students(num_students_to_generate)
    print(f"{num_students_to_generate} students seeded successfully.")
