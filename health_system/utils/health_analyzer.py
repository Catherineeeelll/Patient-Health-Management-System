import os
class HealthAnalyzer:
    @staticmethod
    def calculate_bmi(height, weight):
        """计算 BMI 指数并返回分类。"""
        if height <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive numbers.")

        bmi = weight / ((height / 100) ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        return round(bmi, 2), category

    @staticmethod
    def analyze_blood_pressure(bp_str):
        """分析血压状况。"""
        try:
            systolic, diastolic = map(int, bp_str.split('/'))
        except ValueError:
            raise ValueError("Invalid blood pressure format. Use 'systolic/diastolic'.")

        if systolic < 120 and diastolic < 80:
            return "Normal"
        elif 120 <= systolic < 140 or 80 <= diastolic < 90:
            return "Elevated"
        elif 140 <= systolic or 90 <= diastolic:
            return "Hypertension"
        else:
            return "Unknown"

    def generate_health_report(self, patient):
        """生成健康报告并保存为患者编号命名的txt文件。"""
        bmi, bmi_category = self.calculate_bmi(patient.height, patient.weight)
        blood_pressure_status = self.analyze_blood_pressure(patient.blood_pressure)

        report = (
            f"Health Report for {patient.name} (ID: {patient.patient_id})\n"
            f"--------------------------------------------------\n"
            f"Age: {patient.age} | Gender: {patient.gender}\n"
            f"Height: {patient.height} cm | Weight: {patient.weight} kg\n"
            f"BMI: {bmi} ({bmi_category})\n"
            f"Blood Pressure: {patient.blood_pressure} ({blood_pressure_status})\n"
            f"Blood Sugar: {patient.blood_sugar} mmol/L\n"
            f"Cholesterol: {patient.cholesterol} mmol/L\n"
            f"Check Date: {patient.check_date}\n"
        )

        # 确保 'report' 文件夹存在
        os.makedirs("report", exist_ok=True)

        # 使用患者编号作为文件名，存储到 report 文件夹
        file_name = f"report/{patient.patient_id}_report.txt"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(report)

        return report

