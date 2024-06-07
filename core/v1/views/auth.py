from typing import List

from ninja import NinjaAPI
from core.models.auth import User

from core.v1.schemas.auth import UserSchema, UserCreateSchema, UserUpdateSchema

api1 = NinjaAPI()


@api1.get("user/list/", response=List[UserSchema])
def user_list(request):
    users = User.objects.all()
    return users


@api1.post("user/post/", response=List[UserSchema])
def user_create(request, payload: UserCreateSchema):
    data = payload.dict()
    user = User.objects.create_user(**data)
    return user


@api1.put("user/update/{user_id}", response=List[UserSchema])
def user_update(request, user_id: int, payload: UserUpdateSchema):
    user = User.objects.get_or_404(User, id=user_id)
    data = payload.dict()
    for attr, value in data.items():
        if value is not None:
            setattr(user, attr, value)
    user.save()
    return {"success": True}


@api1.put("user/update/field/{user_id}")
def user_update_field(request, user_id: int, payload: UserUpdateSchema):
    user = User.objects.get_objects_or_404(User, id=user_id)
    for attr, value in payload.dict(exclude_unset=True).items():
        if value is not None:
            setattr(user, attr, value)
    user.save()
    return {"success": True}


@api1.delete("user/delete/{user_id}")
def user_delete(request, user_id: int):
    user = User.objects.get_objects_or_404(User, id=user_id)
    user.delete()
    return {"success": True}
