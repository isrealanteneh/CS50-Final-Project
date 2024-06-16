import project

def test_registerStudents():
    assert project.registerStudents("./studentList") == "Folder path does not exist"


def main():
    test_registerStudents()


if __name__ == "__main__":
    main()