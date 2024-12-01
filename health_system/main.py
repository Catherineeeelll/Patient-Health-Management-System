from models.patient import Patient
from utils.data_manager import DataManager
from utils.health_analyzer import HealthAnalyzer
from datetime import datetime

class HealthSystem:
    def __init__(self):
        self.data_manager = DataManager('data/patient_records.txt')

    def display_menu(self):
        """显示系统主菜单"""
        print("\n---- Patient Health Management System ----")
        print("1. View Patients")
        print("2. Add Patient")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Generate Health Report")
        print("6. Exit")

    def input_patient_data(self):
            """交互式输入患者数据并返回患者对象。"""
            patient_id = input("Enter patient ID (e.g., P101): ").strip()

            # 检查ID是否重复
            existing_patient = self.data_manager.get_patient(patient_id)
            if existing_patient:
                print(f"Error: Patient ID {patient_id} already exists.")
                return None

            name = input("Enter name: ").strip()
            age = input("Enter age: ").strip()
            gender = input("Enter gender (M/F): ").strip()

            # 输入 height 且要进行有效性检查
            while True:
                height = input("Enter height (cm, between 50 and 250): ").strip()
                try:
                    height = float(height)
                    if 50 <= height <= 250:
                        break
                    else:
                        print("Height must be between 50 and 250 cm. Please try again.")
                except ValueError:
                    print("Invalid height input. Please enter a numeric value.")

            # 输入 weight 且要进行有效性检查
            while True:
                weight = input("Enter weight (kg, between 20 and 200): ").strip()
                try:
                    weight = float(weight)
                    if 20 <= weight <= 200:
                        break
                    else:
                        print("Weight must be between 20 and 200 kg. Please try again.")
                except ValueError:
                    print("Invalid weight input. Please enter a numeric value.")

            blood_pressure = input("Enter blood pressure (e.g., 120/80): ").strip()
            blood_sugar = input("Enter blood sugar level: ").strip()
            cholesterol = input("Enter cholesterol level: ").strip()

            # 输入日期并验证格式及合法性
            while True:
                check_date = input("Enter check date (YYYY-MM-DD): ").strip()
                try:
                    # 检查日期格式是否符合 YYYY-MM-DD
                    check_date_obj = datetime.strptime(check_date, "%Y-%m-%d")
                    # 如果日期合法，则不抛出异常
                    break  # 格式正确，跳出循环
                except ValueError:
                    print("Invalid date format or invalid date. Please enter a date in YYYY-MM-DD format.")

            try:
                return Patient(patient_id, name, int(age), gender, height, weight,
                               blood_pressure, float(blood_sugar), float(cholesterol),
                               check_date_obj.strftime("%Y-%m-%d"))
            except ValueError as e:
                print(f"Invalid input: {e}")
                return None

    def display_patients(self):
        """显示所有患者信息。"""
        patients = self.data_manager.load_data()
        if not patients:
            print("No patient records found.")
        else:
            print("\nPatient List:")
            for patient in patients:
                print(patient)

    def update_patient(self):
        """交互式更新患者信息，允许选择修改某个字段。"""
        patient_id = input("Enter Patient ID to update: ").strip()
        patient = self.data_manager.get_patient(patient_id)

        if patient:
            print(f"Current information for {patient_id}:\n{patient}")
            print("\nWhich detail would you like to update?")
            print("1. Name")
            print("2. Age")
            print("3. Gender")
            print("4. Height")
            print("5. Weight")
            print("6. Blood Pressure")
            print("7. Blood Sugar")
            print("8. Cholesterol")
            print("9. Check Date")
            print("10. Update All")

            choice = input("Choose an option (1-10): ").strip()

            # 根据用户的选择更新特定字段
            if choice == '9':  # Check Date
                while True:
                    check_date = input(f"Enter new check date (current: {patient.check_date}): ").strip()
                    try:
                        # 检查日期格式是否符合 YYYY-MM-DD，并且是合法的日期
                        check_date_obj = datetime.strptime(check_date, "%Y-%m-%d")
                        patient.check_date = check_date_obj.strftime("%Y-%m-%d")
                        break  # 格式正确且合法，跳出循环
                    except ValueError:
                        print("Invalid date format or invalid date. Please enter a date in YYYY-MM-DD format.")
            else:
                # 其他字段的更新
                pass

            try:
                self.data_manager.update_patient(patient)
                print(f"Patient {patient_id} updated successfully.")
            except ValueError as e:
                print(f"Error updating patient: {e}")
        else:
            print("Patient not found.")

    def run(self):
        """主系统循环。"""
        while True:
            self.display_menu()  # 显示主菜单
            choice = input("Choose an option: ").strip()
            if choice == '1':
                self.display_patients()
            elif choice == '2':
                patient = self.input_patient_data()
                if patient:
                    try:
                        self.data_manager.add_patient(patient)
                        print("Patient added successfully.")
                    except ValueError as e:
                        print(f"Error adding patient: {e}")
            elif choice == '3':
                self.update_patient()
            elif choice == '4':
                patient_id = input("Enter Patient ID to delete: ").strip()
                # 调用删除方法，并根据返回值进行判断
                success = self.data_manager.delete_patient(patient_id)
                if success:
                    print(f"Patient {patient_id} deleted successfully.")
                else:
                    print(f"Patient with ID {patient_id} not found.")
            elif choice == '5':
                patient_id = input("Enter Patient ID for report: ").strip()
                patient = self.data_manager.get_patient(patient_id)
                if patient:
                    analyzer = HealthAnalyzer()
                    report = analyzer.generate_health_report(patient)
                    print(report)
                else:
                    print("Patient not found.")
            elif choice == '6':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    system = HealthSystem()
    system.run()

