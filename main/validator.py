from uuid import UUID
def validate_uuid(value):
    try:
        uuid_obj = UUID(value)
        return uuid_obj
    except ValueError:
        return None
