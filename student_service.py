
from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


# Sample student database
students = {
    101: {"name": "Aarav Patel", "course": "B.Tech CSE", "semester": 4},
    102: {"name": "Diya Shah", "course": "B.Tech IT", "semester": 2},
    103: {"name": "Rohan Mehta", "course": "B.Tech CSE", "semester": 6},
}


class StudentService(ServiceBase):

    @rpc(Integer, _returns=Unicode)
    def get_student_name(ctx, student_id):
        student = students.get(student_id)

        if student:
            return student["name"]

        return "Student not found"

    @rpc(Integer, _returns=Unicode)
    def get_student(ctx, student_id):
        student = students.get(student_id)

        if student:
            return (
                f"ID: {student_id}, "
                f"Name: {student['name']}, "
                f"Course: {student['course']}, "
                f"Semester: {student['semester']}"
            )

        return "Student not found"


application = Application(
    [StudentService],
    tns="student.soap.service",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11()
)

wsgi_application = WsgiApplication(application)

if __name__ == "__main__":
    print("Student SOAP Service running at http://127.0.0.1:8000")
    print("WSDL: http://127.0.0.1:8000/?wsdl")

    server = make_server("127.0.0.1", 8000, wsgi_application)
    server.serve_forever()
