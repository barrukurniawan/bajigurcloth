def user_formatter(item=None):

    member = ""
    reward = ""
    count = 0
    level = ""

    if item.membership is not None:
        if item.membership == 1:
            member = "yes"

            if int(item.total_transaksi) < 100000:
                level = "silver"
                count = 100000 - int(item.jumlah_transaksi)
                reward = "Ayo Belanja lagi Rp." + str(count) + " untuk dapat diskon 10% Belanja tanpa minimum"
            if int(item.total_transaksi) > 250000 and int(item.total_transaksi) < 750000 :
                level = "gold"
                reward = "Terima Kasih Kesetiannya Member BAJIGUR! Anda mendapat diskon 30% tanpa minimum"
            if int(item.total_transaksi) > 750000:
                level = "platinum"
                reward = "Terima Kasih Kesetiannya Member BAJIGUR! Anda mendapat diskon 50% tanpa minimum"
        else:
            member = "no"

    return {
        "id": item.id,
        "username": item.firstname + " " + item.lastname,
        "email": item.email,
        "membership": member,
        "reward": reward,
        "level": level,
        "total_transaksi": item.total_transaksi,
        "jumlah_transaksi": item.jumlah_transaksi,
        "updated_at": str(item.updated_at),
        "created_at": str(item.created_at),
        "deleted_at": str(item.deleted_at),
    }

def message_formatter(item=None):
    from models import MessageThread, User
    from db import db

    pengirim = 0
    penerima = 0
    nama = ""

    check_msg = MessageThread.query.filter_by(deleted_at=None).filter_by(id=item.message_thread_id).first()
    db.session.commit()

    if check_msg is not None:
        print (item.user_id)
        check_user = User.query.filter_by(deleted_at=None).filter_by(id=item.user_id).first()
        db.session.commit()
        print ("kirim vs terima : ",check_msg.from_user_id, check_msg.to_user_id)
        if item.user_id == check_msg.from_user_id :
            print ("pengirim : ",item.user_id)
            pengirim = 1
            if check_user is not None:
                nama = check_user.firstname + " " + check_user.lastname

        if item.user_id == check_msg.to_user_id :
            penerima = 1
            print ("penerima : ",item.user_id)
            if check_user is not None:
                nama = check_user.firstname + " " + check_user.lastname

    return {
        "id": item.id,
        "message_thread_id": item.message_thread_id,
        "user_id": item.user_id,
        "pengirim": pengirim,
        "penerima": penerima,
        "name": nama,
        "message": item.message,
        "updated_at": str(item.updated_at),
        "created_at": str(item.created_at),
        "deleted_at": str(item.deleted_at),
    }

def message_thread_formatter(item=None):
    from models import User
    from db import db

    nama_pengirim = ""
    nama_penerima = ""

    check_user = User.query.filter_by(deleted_at=None)

    if item.from_user_id is not None:
        pengirim = check_user.filter_by(id=item.from_user_id).first()
        if pengirim is not None:
            nama_pengirim = pengirim.firstname + " " + pengirim.lastname

    if item.to_user_id is not None:
        penerima = check_user.filter_by(id=item.to_user_id).first()
        if penerima is not None:
            nama_penerima = penerima.firstname + " " + penerima.lastname

    db.session.commit()


    return {
        "id": item.id,
        "subject": item.subject,
        "from_user_id": item.from_user_id,
        "message_type": item.message_type,
        "to_user_id": item.to_user_id,
        "nama_pengirim": nama_pengirim,
        "nama_penerima": nama_penerima,
        "updated_at": str(item.updated_at),
        "created_at": str(item.created_at),
        "deleted_at": str(item.deleted_at),
    }