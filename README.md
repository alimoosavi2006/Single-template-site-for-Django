# Single Template Site for Django

یک پروژهٔ تمرینی از قالب تک‌صفحه‌ای (Single Page ) که برای تمرین دورهٔ :contentReference[oaicite:0]{index=0} ایجاد شده است.  
قالب با استفاده از HTML، CSS، JavaScript ساخته شده و دانش پایه‌ای کار با :contentReference[oaicite:1]{index=1} در پروژه وارد شده است.

---

## فهرست مطالب  
- [ویژگی‌ها](#ویژگی‌ها)  
- [پیش‌نیازها](#پیش‌نیازها)  
- [نصب و اجرا](#نصب-و-اجرا)  
- [نمونه‌تصویر](#نمونه‌تصویر)  
- [ساختار پروژه](#ساختار-پروژه)  
- [بهبودها و مسیر آینده](#بهبودها-و-مسیر-آینده)  
- [لایسنس](#لایسنس)  
- [تماس](#تماس)  

---

## ویژگی‌ها  
- قالب تک‌صفحه‌ای ساده، مناسب برای تمرین طراحی وب  
- استفاده از HTML5 و CSS3 برای ساختار و ظاهر  
- افزوده شدن Javascript برای تعاملات پایه‌ای  
- انتخاب اولیه برای ورود به دنیای Django (بخش Python مختصر برای تمرین)  

---

## پیش‌نیازها  
- مرورگر وب (Chrome, Firefox یا معادل)  
- اگر می‌خواهید بخش Django را اجرا کنید: Python ≥ 3 و Django  
- برای مشاهده صرفاً رابط کاربری: کافی است فایل `index.html` را در مرورگر باز کنید  

---

## نصب و اجرا  

### الف) اجرای رابط کاربری (بدون Django)  
```bash
git clone https://github.com/alimoosavi2006/Single-template-site-for-Django.git  
cd Single-template-site-for-Django  
# فایل index.html را در مرورگر باز کنید یا سروری محلی ساده اجرا کنید

  git clone https://github.com/alimoosavi2006/Single-template-site-for-Django.git  
cd Single-template-site-for-Django  
# فرض بر این است که محیط مجازی (virtualenv) فعال شده باشد  
pip install django  
python manage.py runserver  
# سپس در مرورگر به http://127.0.0.1:8000 مراجعه کنید  





