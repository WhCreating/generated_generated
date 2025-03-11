import format_return
import generated

# Пароль(20 символов)
passwd = generated.passwd_generated()
print(passwd)

# Имя для пароля(20 символов)
passwd_name = generated.id_passwd_generated()
print(passwd_name)

# Список паролей(20 паролей)
list_pass = format_return.list_gener()
print(list_pass)

# Словарь паролей(20 пар)
dict_pass = format_return.dict_gener()
print(dict_pass)