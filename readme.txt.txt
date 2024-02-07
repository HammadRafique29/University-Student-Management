Final Project Part2
You will design a program that manages student records at a university. You will need to use a number
of concepts that you learned in class including: use of classes, use of dictionaries and input and output
of comma delimited csv files.
Input:
a) StudentsMajorsList.csv -- contains items listed by row. Each row contains student ID, last
name, first name, major, and optionally a disciplinary action indicator
b) GPAList.csv -- contains items listed by row. Each row contains student ID and the student
GPA.
c) GraduationDatesList.csv – contains items listed by row. Each row contains student ID and
graduation date.
Example StudentsMajorsList.csv, GPAList.csv and GraduationDatesList.csv are provided for reference.
Your code will be expected to work with any group of input files of the appropriate format. Names,
majors, GPAs and graduation dates can and will likely be different from the examples provided.
You can reuse parts of your code from Part 1.
Required Output:
1) Interactive Inventory Query Capability
a. Query the user of an item by asking for a major and GPA with a single query.
i. Print a message(“No such student”) if the major is not in the roster, more that
one major or GPA is submitted. Ignore any other words, so “smart Computer
Science student 3.5” is treated the same as “Computer Science 3.5”.
ii. Print “Your student(s):” with the student ID, first name, last item, GPA. Do not
provide students that have graduated or had disciplinary action . List all the
students within 0.1 of the requested GPA.
iii. Also print “You may, also, consider:” and provide information about the same
student type within 0.25 of the requested GPA . Do not provide students that
have graduated or had disciplinary action.
iv. If there were no students who satisfied neither ii nor iii above – provide the
information about the student within the requested major with closest GPA to
that requested. Do not provide students that have graduated or had disciplinary
action .
v. After output for one query, query the user again. Allow ‘q’ to quit.