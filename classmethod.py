import uuid


class BaseDevice:
    # static list
    devices = []

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
        self.devices.append(self)

    # Has class itself
    @classmethod
    def create_instance(cls, *args, **kwargs):
        if kwargs.get('token', None) is not None:
            for device in BaseDevice.devices:
                if device.token == kwargs['token']:
                    return device
        return cls(*args, **kwargs)

    # Its only a static method
    @staticmethod
    def print_class_type():
        print("BaseDevice")


an_id = uuid.uuid4()

dev1 = BaseDevice.create_instance(token=an_id, model="model",
                                  os_name="os_name", os_version="os_version")

dev2 = BaseDevice.create_instance(token=an_id, model="model2",
                                  os_name="another", os_version="os_version")

dev3 = BaseDevice.create_instance(token=uuid.uuid4(), model="model2",
                                  os_name="another", os_version="os_version")

print(BaseDevice.devices)
print(type(dev1))
print(dev1.__dict__)

BaseDevice.print_class_type()
