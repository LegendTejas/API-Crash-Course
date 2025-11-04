from passlib.context import CryptContext

# Initialize password hashing context using bcrypt
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    @staticmethod
    def bcrypt(password: str):
        """Hash a plain password using bcrypt algorithm."""
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(plain_password: str, hashed_password: str):
        """Verify a plain password against its hashed version."""
        return pwd_cxt.verify(plain_password, hashed_password)
