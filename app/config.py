import os

from dotenv import load_dotenv

load_dotenv()

class Config:
   ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp", "pdf", 'epub'}
   ALLOWED_REFERRERS = {os.getenv("CLIENT_URL")}

   JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

   UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
   os.makedirs(UPLOAD_FOLDER, exist_ok=True)

