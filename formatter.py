def user_formatter(item=None):

    member = ""

    if item.membership is not None:
        if item.membership == 1:
            member = "yes"
        else:
            member = "no"

    return {
        "id": item.id,
        "username": item.first_name + " " + item.last_name,
        "email": item.email,
        "membership": member,
        "updated_at": str(item.updated_at),
        "created_at": str(item.created_at),
        "deleted_at": str(item.deleted_at),
    }

def point_formatter(item=None):

    return {
        "id": item.id,
        "level": item.level,
        "point": item.point,
        "updated_at": str(item.updated_at),
        "created_at": str(item.created_at),
        "deleted_at": str(item.deleted_at),
    }

def user_point_formatter(item=None):

    return {
        "id": item.id,
        "user_id": item.user_id,
        "total_point": item.total_point,
        "updated_at": str(item.updated_at),
        "created_at": str(item.created_at),
        "deleted_at": str(item.deleted_at),
    }

def user_point_log_formatter(item=None):

    return {
        "id": item.id,
        "user_point_id": item.user_point_id,
        "total_point": item.total_point,
        "updated_at": str(item.updated_at),
        "created_at": str(item.created_at),
        "deleted_at": str(item.deleted_at),
    }

def voucher_formatter(item=None):

    return {
        "id": item.id,
        "code": item.code,
        "discount_type": item.discount_type,
        "value_type": item.value_type,
        "discount_value": item.discount_value,
        "valid_from": item.valid_from,
        "valid_to": item.valid_to,
        "limit": item.limit,
        "updated_at": str(item.updated_at),
        "created_at": str(item.created_at),
        "deleted_at": str(item.deleted_at),
    }

def voucher_log_formatter(item=None):

    return {
        "id": item.id,
        "user_id": item.user_id,
        "voucher_id": item.voucher_id,
        "updated_at": str(item.updated_at),
        "created_at": str(item.created_at),
        "deleted_at": str(item.deleted_at),
    }