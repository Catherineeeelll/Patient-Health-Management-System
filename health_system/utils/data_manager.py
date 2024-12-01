import os
from models.patient import Patient  # type: ignore

class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(file_path):
            print(f"Creating file: {file_path}")
            open(file_path, 'w').close()

    def load_data(self):
        """从文件加载患者数据并返回患者对象列表。"""
        patients = []
        if os.path.exists(self.file_path):
            print(f"Loading data from: {self.file_path}")
            with open(self.file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    # 自动处理转义字符并去除空白字符
                    line = line.strip().replace("\\t", "\t")
                    fields = line.split('\t')  # 用 \t 分隔
                    if len(fields) == 10:
                        try:
                            patient = Patient(*fields)
                            patients.append(patient)
                        except ValueError as e:
                            print(f"Error parsing patient data: {e}")
        else:
            print("File not found!")
        print(f"Total patients loaded: {len(patients)}")
        return patients

    def save_data(self, patients):
        """保存患者数据"""
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                for patient in patients:
                    file.write(patient.to_string() + '\n')  # 使用 to_string() 来输出患者数据
        except Exception as e:
            print(f"Failed to save data: {e}")

    def get_patient(self, patient_id):
        """根据患者ID获取患者信息"""
        patients = self.load_data()
        for patient in patients:
            if patient.patient_id == patient_id:
                return patient
        return None

    def add_patient(self, patient):
        """添加新患者并将其追加到文件中，确保换行。"""
        # 检查ID是否唯一
        patients = self.load_data()
        if any(p.patient_id == patient.patient_id for p in patients):
            raise ValueError("Patient ID already exists.")

        # 将新患者数据追加到文件，确保换行
        with open(self.file_path, 'a', encoding='utf-8') as file:
            file.write(patient.to_string() + '\n')  # 确保换行符
        print(f"Patient {patient.patient_id} added successfully.")

    def update_patient(self, updated_patient):
        """更新患者信息"""
        patients = self.load_data()
        for idx, patient in enumerate(patients):
            if patient.patient_id == updated_patient.patient_id:
                patients[idx] = updated_patient
                self.save_data(patients)
                return True
        return False

    def delete_patient(self, patient_id):
        """删除患者信息"""
        patients = self.load_data()

        # 判断患者 ID 是否存在
        patient = next((p for p in patients if p.patient_id == patient_id), None)
        if patient is None:
            return False  # 如果没有找到该患者 ID，返回 False，表示删除失败

        # 如果患者存在，则删除
        patients = [patient for patient in patients if patient.patient_id != patient_id]
        self.save_data(patients)

        # 返回 True，表示删除成功
        return True


