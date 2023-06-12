from typing import List, Union

from beanie import PydanticObjectId

from models.admin import Admin
from models.student import Student

admin_collection = Admin
student_collection = Student


async def add_admin(new_admin: Admin) -> Admin:
    return await new_admin.create()


async def retrieve_students() -> List[Student]:
    return await student_collection.all().to_list()


async def add_student(new_student: Student) -> Student:
    return await new_student.create()


async def retrieve_student(id: PydanticObjectId) -> Student:
    student = await student_collection.get(id)
    if student:
        return student


async def delete_student(id: PydanticObjectId) -> bool:
    student = await student_collection.get(id)
    if student:
        await student.delete()
        return True


async def update_student_data(id: PydanticObjectId, data: dict) -> Union[bool, Student]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": dict(des_body)}
    student = await student_collection.get(id)
    if student:
        await student.update(update_query)
        return student
    return False
