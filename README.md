# 📚 E-Book Market Potential Analyzer
### E-Book Decision Support Platform | Machine Learning + Web Application

https://ebook-insight-engine.lovable.app/

[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.6.1-orange?logo=scikitlearn)](https://scikit-learn.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)](https://fastapi.tiangolo.com)
[![Render](https://img.shields.io/badge/Render-Deployment-purple?logo=render)](https://render.com)
[![Lovable](https://img.shields.io/badge/Lovable-Frontend-ff69b4)](https://lovable.dev)

> **End-to-End Machine Learning Decision-Support App**  
> ระบบวิเคราะห์ศักยภาพทางการตลาดของหนังสือ E-Book  
> โดยใช้ Machine Learning เพื่อช่วยประเมินโอกาสการเป็นหนังสือขายดีบนแพลตฟอร์มออนไลน์

---

## 📋 สารบัญ

- [ภาพรวมโครงการ](#-ภาพรวมโครงการ)
- [วัตถุประสงค์ของโครงการ](#-วัตถุประสงค์ของโครงการ)
- [ข้อมูลที่ใช้](#-ข้อมูลที่ใช้)
- [ตัวแปรที่ใช้ในแอป](#-ตัวแปรที่ใช้ในแอป)
- [ขั้นตอนการวิเคราะห์](#-ขั้นตอนการวิเคราะห์)
- [โมเดลที่ใช้](#-โมเดลที่ใช้)
- [โมเดลสุดท้าย](#-โมเดลสุดท้าย)
- [สถาปัตยกรรมระบบ](#-สถาปัตยกรรมระบบ)
- [วิธีใช้งาน](#-วิธีใช้งาน)
- [ตัวอย่างการใช้งาน](#-ตัวอย่างการใช้งาน)
- [โครงสร้างไฟล์](#-โครงสร้างไฟล์)
- [ข้อจำกัดของโครงการ](#-ข้อจำกัดของโครงการ)
- [แนวทางพัฒนาต่อ](#-แนวทางพัฒนาต่อ)
- [Tech Stack](#-tech-stack)

---

## 🎯 ภาพรวมโครงการ

ตลาดหนังสือดิจิทัลหรือ **E-Book** มีการแข่งขันสูงขึ้นอย่างต่อเนื่องบนแพลตฟอร์มออนไลน์ ผู้บริโภคสามารถเปรียบเทียบราคา คะแนนรีวิว จำนวนรีวิว หมวดหมู่ และข้อมูลผู้ขายก่อนตัดสินใจซื้อได้อย่างสะดวก

โครงการนี้จึงพัฒนา **E-Book Market Potential Analyzer** ซึ่งเป็นแอปพลิเคชันต้นแบบที่ใช้ Machine Learning เพื่อช่วยประเมินว่า E-Book รายการหนึ่งมีศักยภาพทางการตลาดมากน้อยเพียงใด

ระบบนี้ไม่ได้ออกแบบมาเพื่อทำนายยอดขายแบบรับประกันผลลัพธ์ แต่ทำหน้าที่เป็น **decision-support tool** ที่ช่วยให้ผู้ใช้สามารถทดลองเปรียบเทียบสถานการณ์ เช่น การปรับราคา การเพิ่มจำนวนรีวิว หรือการเข้าร่วม Kindle Unlimited

---

## 🧭 วัตถุประสงค์ของโครงการ

โครงการนี้มีวัตถุประสงค์เพื่อ:

1. วิเคราะห์ปัจจัยที่เกี่ยวข้องกับความสำเร็จของหนังสือ E-Book
2. สร้างโมเดล Machine Learning เพื่อประเมินโอกาสการเป็น Best Seller
3. เปรียบเทียบโมเดลหลายรูปแบบ เช่น Dummy Classifier, Logistic Regression และ Random Forest
4. จัดการปัญหา class imbalance ของตัวแปรเป้าหมาย
5. เลือกโมเดลสุดท้ายที่เหมาะสมทั้งในด้าน performance และการใช้งานจริง
6. พัฒนาแอปพลิเคชันที่ผู้ใช้สามารถโต้ตอบกับโมเดลได้จริง
7. Deploy โมเดลเป็น API และเชื่อมต่อกับ frontend สำหรับการนำเสนอ

---

## 📊 ข้อมูลที่ใช้

โครงการนี้ใช้ข้อมูลจากชุดข้อมูล **Amazon Kindle Books Dataset 2023** ซึ่งเป็นข้อมูลระดับรายการหนังสือ E-Book บนแพลตฟอร์มออนไลน์

ข้อมูลประกอบด้วยตัวแปรสำคัญ เช่น:

- ชื่อหนังสือ
- ผู้เขียน
- ผู้ขาย
- คะแนนดาว
- จำนวนรีวิว
- ราคา
- สถานะ Kindle Unlimited
- หมวดหมู่หนังสือ
- วันที่เผยแพร่
- สถานะ Best Seller

ตัวแปรเป้าหมายหลักของโครงการคือ:

```text
isBestSeller
```

ซึ่งใช้แทนสถานะว่าหนังสือรายการนั้นถูกจัดเป็น Best Seller หรือไม่

---

## 🔎 ตัวแปรที่ใช้ในแอป

โมเดลสุดท้ายใช้ตัวแปรทั้งหมด 8 ตัว ซึ่งเป็นตัวแปรที่ผู้ใช้ทั่วไปเข้าใจได้และสามารถนำไปใช้จำลองสถานการณ์ได้จริง

| ตัวแปร | ความหมาย |
|---|---|
| `stars` | คะแนนดาวเฉลี่ยของหนังสือ |
| `reviews` | จำนวนรีวิวของหนังสือ |
| `price` | ราคาหนังสือ |
| `book_age_years` | อายุหนังสือโดยนับจากปีที่เผยแพร่ |
| `included_in_kindle_unlimited` | หนังสืออยู่ในระบบ Kindle Unlimited หรือไม่ |
| `published_date_not_available` | ไม่มีข้อมูลวันที่เผยแพร่หรือไม่ |
| `category_grouped` | หมวดหมู่หนังสือ |
| `soldby_grouped` | กลุ่มผู้ขาย |

> ตัวแปร badge เช่น `isEditorsPick` และ `isGoodReadsChoice` ถูกตัดออกจากโมเดลสุดท้าย  
> เพราะเป็นข้อมูลที่ผู้ใช้ไม่สามารถกำหนดหรือทราบได้ล่วงหน้าเสมอไปก่อนวางขายหนังสือ

---

## 🔬 ขั้นตอนการวิเคราะห์

### Step 1 — Data Cleaning & Feature Engineering

ดำเนินการตรวจสอบและเตรียมข้อมูล เช่น:

- ตรวจสอบข้อมูลซ้ำ
- จัดการ missing values
- สร้างตัวแปร `publishedDate_missing`
- แปลงจำนวนรีวิวเป็น `log_reviews`
- แปลงราคาเป็น `log_price`
- คำนวณอายุหนังสือ
- จัดกลุ่มหมวดหมู่หนังสือและผู้ขาย

---

### Step 2 — Exploratory Data Analysis

วิเคราะห์ลักษณะสำคัญของข้อมูล เช่น:

- การกระจายตัวของราคาและจำนวนรีวิว
- สัดส่วนของหนังสือ Best Seller
- ปัญหา class imbalance
- ความสัมพันธ์ระหว่างตัวแปร
- ลักษณะของหมวดหมู่หนังสือและผู้ขาย

ผลจาก EDA พบว่า หนังสือที่เป็น Best Seller มีสัดส่วนเพียงประมาณ **1.68%** ของข้อมูลทั้งหมด ทำให้การประเมินโมเดลต้องใช้ตัวชี้วัดที่เหมาะสมมากกว่า accuracy เพียงอย่างเดียว

---

### Step 3 — Predictive Modeling

สร้างและเปรียบเทียบโมเดลหลายรูปแบบ ได้แก่:

- Dummy Classifier
- Logistic Regression
- Random Forest
- Random Forest แบบ No Badge

โดยใช้ train-test split แบบ stratified เพื่อรักษาสัดส่วนของ class target ให้ใกล้เคียงกันทั้งชุด train และ test

---

### Step 4 — Threshold Tuning

เนื่องจากข้อมูลมี class imbalance สูง จึงไม่ได้ใช้ threshold มาตรฐาน 0.50 เพียงอย่างเดียว แต่มีการทดลอง threshold หลายระดับเพื่อหาจุดตัดที่เหมาะสมระหว่าง precision และ recall

---

### Step 5 — Controlled Scenario Testing

ทดสอบพฤติกรรมของโมเดลด้วยสถานการณ์จำลอง เช่น:

- เพิ่มจำนวนรีวิว
- ลดราคา
- เปิด/ปิด Kindle Unlimited
- เปลี่ยนหมวดหมู่หนังสือ
- เปรียบเทียบผลลัพธ์เมื่อใช้ badge features

ผลการทดสอบพบว่าโมเดลแบบ No Badge มีความเหมาะสมต่อการนำไปใช้จริงมากกว่า เพราะ input มีความเข้าใจง่ายและสอดคล้องกับสิ่งที่ผู้ใช้สามารถควบคุมได้

---

## 🤖 โมเดลที่ใช้

| Model | จุดประสงค์ | หมายเหตุ |
|---|---|---|
| Dummy Classifier | Baseline | ใช้เปรียบเทียบกับโมเดลจริง |
| Logistic Regression | Interpretable Model | ตีความง่าย แต่จับ nonlinear pattern ได้จำกัด |
| Random Forest | Nonlinear Model | จับ interaction ระหว่างตัวแปรได้ดี |
| Random Forest (No Badge) | Final App Model | เหมาะกับการนำไปใช้จริงที่สุด |

---

## 🏆 โมเดลสุดท้าย

โมเดลสุดท้ายที่เลือกใช้ในแอปคือ:

```text
Random Forest (No Badge)
```

Decision threshold ที่ใช้:

```text
0.60
```

### เหตุผลที่เลือกโมเดลนี้

Random Forest แบบ No Badge ถูกเลือกเป็นโมเดลสุดท้าย เนื่องจาก:

- ให้ผลลัพธ์ดีกว่า Logistic Regression ในภาพรวม
- สามารถเรียนรู้ความสัมพันธ์ที่ไม่เป็นเส้นตรงได้ดี
- รองรับตัวแปรทั้งเชิงตัวเลขและเชิงหมวดหมู่
- ไม่ใช้ตัวแปร badge ที่ผู้ใช้ควบคุมไม่ได้
- เหมาะกับการจำลอง scenario ทางธุรกิจ
- ตีความและอธิบายกับผู้ใช้ทั่วไปได้ง่ายกว่า

---

## 🧠 ตัวชี้วัดที่ใช้ประเมินโมเดล

เนื่องจากข้อมูลมี class imbalance สูง งานนี้จึงใช้ตัวชี้วัดหลายตัวร่วมกัน ได้แก่:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- PR-AUC
- Confusion Matrix

> Accuracy เพียงอย่างเดียวไม่เพียงพอ เพราะหากโมเดลทำนายว่า “ไม่เป็น Best Seller” ทุกกรณี ก็ยังอาจได้ accuracy สูงจากสัดส่วน class ที่ไม่สมดุล

---

## 🏗️ สถาปัตยกรรมระบบ

ระบบที่พัฒนาขึ้นประกอบด้วย 3 ชั้นหลัก:

```text
Lovable Frontend
        ↓
Render FastAPI Backend
        ↓
Trained Random Forest Model (.joblib)
```

### Frontend Layer

พัฒนา interface ด้วย **Lovable** เพื่อให้ผู้ใช้สามารถกรอกข้อมูลหนังสือและดูผลลัพธ์ผ่าน dashboard ที่ใช้งานง่าย

### Backend API Layer

พัฒนา backend ด้วย **FastAPI** และ deploy ผ่าน **Render** เพื่อรับข้อมูลจาก frontend และเรียกใช้โมเดล Machine Learning

### Model Layer

ใช้โมเดล Random Forest ที่บันทึกเป็นไฟล์ `.joblib` และโหลดขึ้นมาเพื่อทำนายผลผ่าน API

---

## 🌐 Live Prediction API

API endpoint หลักคือ:

```text
POST /predict
```

ตัวอย่าง request body:

```json
{
  "stars": 4.0,
  "reviews": 5000,
  "price": 9.99,
  "book_age_years": 3,
  "included_in_kindle_unlimited": true,
  "published_date_not_available": false,
  "category_grouped": "Literature & Fiction",
  "soldby_grouped": "Amazon.com Services LLC"
}
```

ตัวอย่าง response:

```json
{
  "estimated_bestseller_score": 0.3812,
  "prediction_result": "Not Likely Best Seller",
  "commercial_potential_level": "Low",
  "decision_threshold": 0.6,
  "model_name": "Random Forest (No Badge)"
}
```

---

## 🚀 วิธีใช้งาน

### 1. Clone repository

```bash
git clone https://github.com/FlukeTU/ebook-market-potential-analyzer.git
cd ebook-market-potential-analyzer
```

### 2. ติดตั้ง dependencies

```bash
pip install -r requirements.txt
```

### 3. รัน FastAPI backend

```bash
uvicorn api:app --reload
```

จากนั้นเปิด:

```text
http://127.0.0.1:8000/docs
```

เพื่อทดสอบ API ผ่าน Swagger UI

---

## 🖥️ วิธีรัน Gradio Prototype

หากต้องการรันแอปต้นแบบแบบ local:

```bash
python app.py
```

ระบบจะสร้าง local URL สำหรับเปิดแอปผ่าน browser

---

## 📁 โครงสร้างไฟล์

```text
ebook-market-potential-analyzer/
│
├── 📁 model_artifacts/
│   ├── final_rf_no_badge_pipeline.joblib     # โมเดล Random Forest สุดท้าย
│   └── final_app_metadata.json               # metadata ของโมเดล
│
├── 📄 api.py                                  # FastAPI backend สำหรับ prediction
├── 📄 app.py                                  # Gradio prototype
├── 📄 requirements.txt                        # Python dependencies
├── 📄 .python-version                         # ระบุ Python version สำหรับ Render
├── 📄 README.md                               # เอกสารอธิบายโปรเจกต์
└── 📄 .gitignore                              # ไฟล์ที่ไม่ต้องการ push ขึ้น GitHub
```

---

## 💡 ตัวอย่างการใช้งาน

สมมติว่านักเขียนอิสระกำลังจะวางขาย E-Book เล่มใหม่ แต่ยังไม่แน่ใจว่าควรตั้งราคาเท่าไร หรือควรเข้าร่วม Kindle Unlimited หรือไม่

ผู้ใช้สามารถกรอกข้อมูลหนังสือ เช่น:

- คะแนนดาวที่คาดว่าจะได้รับ
- จำนวนรีวิว
- ราคา
- อายุหนังสือ
- หมวดหมู่หนังสือ
- สถานะ Kindle Unlimited

จากนั้นระบบจะประเมินคะแนนศักยภาพทางการตลาด และแสดงผลว่า E-Book ดังกล่าวมีแนวโน้มเป็น Best Seller หรือไม่

แอปนี้จึงช่วยให้ผู้ใช้สามารถเปรียบเทียบ scenario ได้ เช่น:

- ถ้าลดราคาจาก 9.99 USD เป็น 4.99 USD คะแนนจะเปลี่ยนอย่างไร
- ถ้าเปิด Kindle Unlimited คะแนนจะเพิ่มขึ้นหรือไม่
- ถ้าจำนวนรีวิวเพิ่มขึ้น ศักยภาพทางการตลาดจะเปลี่ยนแปลงอย่างไร

---

## 👥 กลุ่มผู้ใช้เป้าหมาย

แอปนี้เหมาะสำหรับ:

- นักเขียน E-Book อิสระ
- สำนักพิมพ์ดิจิทัล
- ผู้ขายหนังสือออนไลน์
- นักการตลาดดิจิทัล
- นักวิเคราะห์ตลาดหนังสือ
- นักศึกษา Data Science
- ผู้ที่สนใจการประยุกต์ Machine Learning กับตลาดออนไลน์

---

## 📊 ผลลัพธ์ที่ผู้ใช้จะได้รับ

แอปจะแสดงผลลัพธ์หลัก 4 ส่วน ได้แก่:

| Output | ความหมาย |
|---|---|
| Estimated Bestseller Score | คะแนนศักยภาพการเป็นหนังสือขายดี |
| Prediction Result | ผลการประเมินว่าเข้าข่าย Best Seller หรือไม่ |
| Commercial Potential Level | ระดับศักยภาพทางการตลาด |
| Model Interpretation | คำอธิบายผลลัพธ์จากโมเดล |

---

## ⚠️ ข้อจำกัดของโครงการ

โครงการนี้ยังมีข้อจำกัดที่ควรพิจารณา ได้แก่:

1. ข้อมูลมาจาก Amazon Kindle เพียงแพลตฟอร์มเดียว
2. ตัวแปร `isBestSeller` เป็น proxy ของความสำเร็จ ไม่ใช่ยอดขายหรือรายได้จริง
3. โมเดลยังไม่ครอบคลุมปัจจัยเชิงคุณภาพ เช่น ปกหนังสือ เนื้อหา ชื่อเสียงผู้เขียน หรือกลยุทธ์โฆษณา
4. ข้อมูลมี class imbalance สูง ทำให้การทำนาย Best Seller เป็นโจทย์ที่ยาก
5. ผลลัพธ์จากแอปควรถูกตีความเป็นสัญญาณสนับสนุนการตัดสินใจ ไม่ใช่การรับประกันผลลัพธ์ทางธุรกิจ

---

## 🔮 แนวทางพัฒนาต่อ

ในอนาคตสามารถพัฒนาต่อได้หลายแนวทาง เช่น:

- เพิ่มข้อมูลจากแพลตฟอร์ม E-Book อื่น
- ใช้ข้อมูลข้อความจากชื่อหนังสือหรือคำอธิบายหนังสือด้วย NLP
- ทดลองโมเดล Gradient Boosting เช่น XGBoost หรือ LightGBM
- ปรับ calibration ของ probability ให้แม่นยำขึ้น
- เพิ่มระบบเปรียบเทียบหนังสือหลายเล่ม
- เพิ่มระบบบันทึก scenario ของผู้ใช้
- เพิ่ม dashboard สำหรับสำนักพิมพ์หรือผู้ขายหนังสือออนไลน์
- เพิ่ม explainability เช่น SHAP values

---

## 🛠️ Tech Stack

| ส่วนของระบบ | เครื่องมือ |
|---|---|
| Data Analysis | Python, Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Model Saving | Joblib |
| Local Prototype | Gradio |
| Backend API | FastAPI |
| Deployment | Render |
| Frontend UI | Lovable |
| Version Control | GitHub |
| Notebook Environment | Google Colab |

---

## 🧾 Final Note

โครงการนี้แสดงให้เห็นกระบวนการทำงานแบบ end-to-end ตั้งแต่การเตรียมข้อมูล การวิเคราะห์ข้อมูล การสร้างโมเดล Machine Learning การบันทึกโมเดล การ deploy backend API และการสร้าง web application สำหรับผู้ใช้จริง

จุดเด่นของโครงการนี้ไม่ได้อยู่ที่การสร้างโมเดลเพียงอย่างเดียว แต่อยู่ที่การแปลงโมเดลให้กลายเป็นเครื่องมือสนับสนุนการตัดสินใจที่สามารถทดลองใช้งานได้จริงในบริบทของตลาด E-Book บนแพลตฟอร์มออนไลน์

---

*โครงการนี้เป็นส่วนหนึ่งของรายวิชา EC683 Solo Project*
