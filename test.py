from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

passwd = 'test'
hash_paswd = pwd_context.hash('test')

print(pwd_context.verify(passwd, hash_paswd))