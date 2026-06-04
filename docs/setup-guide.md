# 📖 دليل الإعداد الكامل

## ال��تطلبات الأساسية

### 1. نظام التشغيل
- Linux / macOS / Windows 10+

### 2. البرامج المطلوبة
- Python 3.8+ ([تحميل](https://www.python.org/downloads/))
- Git ([تحميل](https://git-scm.com/))
- Node.js 14+ (اختياري)

### 3. الحسابات المطلوبة
- حساب GitHub
- حساب Telegram
- API Keys من البلوك تشين

---

## خطوات التثبيت

### الخطوة 1: استنساخ المشروع

```bash
git clone https://github.com/HOK-Al/HOK-Al.git
cd HOK-Al
```

### الخطوة 2: إنشاء بيئة افتراضية

```bash
# على Linux/macOS
python3 -m venv venv
source venv/bin/activate

# على Windows
python -m venv venv
venv\Scripts\activate
```

### الخطوة 3: تثبيت المكتبات

```bash
pip install -r requirements.txt
```

### الخطوة 4: الإعداد

```bash
# نسخ ملف الإعدادات
cp .env.example .env

# تحرير الملف وأضف بيانات اعتمادك
nano .env
```

### الخطوة 5: التشغيل

```bash
# بوت التدقيق
python auditor/bot.py

# أو بوت السك
python minter/bot.py
```

---

## إعدادات مهمة

### Telegram Bot Token

1. افتح Telegram وابحث عن `@BotFather`
2. اختر `/newbot`
3. اتبع التعليمات وحصل على Token
4. أضفه في `.env`

### API Keys

#### Etherscan
1. اذهب إلى [etherscan.io](https://etherscan.io)
2. تسجيل حساب جديد
3. اطلب API Key
4. أضفه في `.env`

#### PolygonScan
1. اذهب إلى [polygonscan.com](https://polygonscan.com)
2. تسجيل حساب جديد
3. اطلب API Key
4. أضفه في `.env`

---

## التحقق من الإعداد

```bash
# اختبر الاتصال
python -c "import web3; print('✅ Web3 installed')"

# اختبر Telegram
python -c "import telegram; print('✅ Telegram library installed')"
```

---

## استكشاف الأخطاء

### خطأ: ModuleNotFoundError
```bash
# تأكد من تفعيل البيئة الافتراضية
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# أعد تثبيت المكتبات
pip install -r requirements.txt
```

### خطأ: Token غير صحيح
- تأكد من نسخ Token بشكل صحيح
- تحقق من ملف `.env`
- حاول إنشاء بوت جديد

---

## الخطوات التالية

✅ اقرأ [دليل الاستخدام](../README.md)
✅ اعرض [الأ��ثلة](examples/)
✅ اتصل بـ [الدعم](support.md)
