import mongoengine

#mongodb://phamhoangphuong-c4e20:123456abc!@ds125932.mlab.com:25932/phamhoangphuong-c4e20

host = "ds125932.mlab.com"
port = 25932
db_name = "phamhoangphuong-c4e20"
user_name = "phuonghoangpham-c4e20"
password = "123456abc"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)