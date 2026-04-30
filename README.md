# 📚 E-Book Market Potential Analyzer
### E-Book Decision Support Platform | Machine Learning + Web Application

https://your-lovable-app-url-here

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