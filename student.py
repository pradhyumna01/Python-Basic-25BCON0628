def create_student(name, age, marks):
    return {
        "name": name,
        "age": age,
        "marks": marks
    }


def print_student(student):
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Marks: {student['marks']:.2f}")


def main():
    s1 = create_student("Sunny", 20, 85.5)
    print_student(s1)


if __name__ == "__main__":
    main()
