import uuid


class BaseUser:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class BaseDevice:

    def __init__(
            self,
            token,
            model,
            os_name,
            os_version
    ):
        self.token = token
        self.model = model
        self.os_name = os_name
        self.os_version = os_version


class WebUser(BaseUser):

    def __init__(self, email, *args, **kwargs):
        super(WebUser, self).__init__(*args, **kwargs)
        self.email = email


class MobileUser(BaseUser):

    def __init__(self, phone_number, user_device, *args, **kwargs):
        super(MobileUser, self).__init__(*args, **kwargs)
        self.device = user_device
        self.mobile_number = phone_number

    def __eq__(self, other):
        return self.mobile_number == other.mobile_number


device = BaseDevice(uuid.uuid4(), "NOKIA", "SIMBIAN", "0.0.1")
mobuser1 = MobileUser(123, device, first_name="ali", last_name="alavi", age=12)

print(type(mobuser1.device))

# class.method resolution order
print(MobileUser.mro())

print(hasattr(mobuser1, 'newattr'))
setattr(mobuser1, 'newattr', 'value')
print(hasattr(mobuser1, 'newattr'))
print(getattr(mobuser1, 'newattr', None))

device = BaseDevice(uuid.uuid4(), "ANDROID", "OREO", "10")
mobuser2 = MobileUser(123, device, first_name="javad", last_name="alavi", age=22)

print(mobuser1 == mobuser2)
