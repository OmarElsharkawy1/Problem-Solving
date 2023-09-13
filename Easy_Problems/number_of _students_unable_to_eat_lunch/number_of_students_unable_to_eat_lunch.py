def countStudents(students, sandwiches):
    # Continue the loop until one of the stopping conditions is met
    while True:
        # Check if the student at the front of the line wants the sandwich at the front of the stack
        if students[0] == sandwiches[0]:
            # If they do, remove the student and the sandwich from their respective lists
            students.remove(students[0])
            sandwiches.remove(sandwiches[0])
        else:
            # If the student doesn't want the current sandwich, move them to the end of the line
            students.append(students[0])
            students.remove(students[0])
        
        # Check if all students have been served a sandwich (empty line)
        if len(students) == 0:
            break
        
        # Check if the remaining sandwich is not wanted by any student (impossible to serve)
        if sandwiches[0] not in students:
            break

    # Return the number of unserved students (students still in line)
    return len(students)