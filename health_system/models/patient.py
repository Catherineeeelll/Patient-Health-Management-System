class Patient:
    def __init__(self, patient_id, name, age, gender, height, weight, blood_pressure, blood_sugar, cholesterol, check_date):
        self.patient_id = patient_id
        self.name = name
        self.age = int(age)
        self.gender = gender
        self.height = float(height)
        self.weight = float(weight)
        self.blood_pressure = blood_pressure
        self.blood_sugar = float(blood_sugar)
        self.cholesterol = float(cholesterol)
        self.check_date = check_date

    def __str__(self):
        """格式化输出患者信息，去除制表符。"""
        return (
            f"ID: {self.patient_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age} years\n"
            f"Gender: {self.gender}\n"
            f"Height: {self.height} cm\n"
            f"Weight: {self.weight} kg\n"
            f"Blood Pressure: {self.blood_pressure}\n"
            f"Blood Sugar: {self.blood_sugar} mmol/L\n"
            f"Cholesterol: {self.cholesterol} mg/dL\n"
            f"Check Date: {self.check_date}\n"
            "--------------------------"
        )

    def validate(self):
        if not self.patient_id.startswith('P'):
            raise ValueError("Patient ID must start with 'P'.")
        if not (0 <= self.age <= 120):
            raise ValueError("Age must be between 0 and 120.")
        if self.gender not in ['M', 'F']:
            raise ValueError("Gender must be 'M' or 'F'.")
        if not (50 <= self.height <= 250):
            raise ValueError("Height must be between 50 and 250 cm.")
        if not (20 <= self.weight <= 200):
            raise ValueError("Weight must be between 20 and 200 kg.")
        # 血压格式验证
        bp_parts = self.blood_pressure.split('/')
        if len(bp_parts) != 2 or not all(part.isdigit() for part in bp_parts):
            raise ValueError("Blood pressure format is incorrect.")
        return True

    def __str__(self):
        # 每列字段对齐，确保表头和数据宽度一致
        return f"{self.patient_id.ljust(12)} {self.name.ljust(10)} {str(self.age).rjust(4)} {self.gender.ljust(6)} " \
               f"{str(self.height).rjust(8)} {str(self.weight).rjust(8)} {self.blood_pressure.ljust(15)} " \
               f"{str(self.blood_sugar).rjust(8)} {str(self.cholesterol).rjust(8)} {self.check_date.ljust(12)}"

    def to_string(self):
        """将患者信息转换为制表符分隔的字符串，确保格式一致。"""
        return (
            f"{self.patient_id}\t"
            f"{self.name}\t"
            f"{self.age}\t"
            f"{self.gender}\t"
            f"{format(self.height, '.1f')}\t"  # 保留1位小数
            f"{format(self.weight, '.1f')}\t"  # 保留1位小数
            f"{self.blood_pressure}\t"
            f"{format(self.blood_sugar, '.1f')}\t"  # 保留1位小数
            f"{format(self.cholesterol, '.1f')}\t"  # 保留1位小数
            f"{self.check_date}"
        )

