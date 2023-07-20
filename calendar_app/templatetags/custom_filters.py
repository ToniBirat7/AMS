from django import template

register = template.Library()

@register.filter
def get_attendance_status(student_attendance, data):
    print('****************')
    # print(student_attendance)
    a = {'b' : 1}
    # print(data)
    student_id, date = data.split('_')
    # print(student_id, date)
    formatted_date = str(date)
    student_data = student_attendance.get(int(student_id),{})
    print(student_data.get(formatted_date))
    return student_data.get(formatted_date, 'N/A')

# @register.filter
# def add_date(student, date):
#     return f"{student.id}_{date}"
