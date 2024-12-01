# 患者健康记录管理系统

本项目是一个简单的病患健康管理系统，目的是为了帮助医疗机构或个人管理患者健康信息。系统允许用户查看、添加、更新、删除患者信息，并生成健康报告。



- [TOC]

  ------

  

## 项目介绍 

本系统提供了一套简洁的命令行界面（CLI），允许用户执行以下操作：

1. **查看患者信息（View Patients）**：列出所有患者的健康信息。 

2. **添加患者（Add Patient）**：允许用户输入患者信息并保存。 

3. **更新患者信息（Update Patient）**：用户可以选择修改患者的某个字段或更新所有信息。 

4. **删除患者信息（Delete Patient）**：根据患者的 ID 删除指定的患者记录。 

5. **生成健康报告（Generate Health Report）**：根据患者的健康数据生成健康报告。

6. **退出（Exit）**：用户退出系统。

   主页面

   

## 功能特性 

- **患者信息管理**：能够查看、添加、更新和删除患者信息。

- **健康报告生成**：系统基于患者的血糖、血压、胆固醇等数据生成健康报告。

- **数据持久化**：系统将患者信息存储在文件中，可以跨会话持久化数据。

- **错误处理**：系统会对输入的患者信息进行验证，确保数据有效性。

- **界面交互**：简洁直观的命令行交互界面，易于使用。



## 安装与运行 

### 一、环境要求 

- **Python 版本**：Python 3.6 或以上 
- **操作系统**：Windows、macOS、Linux

### 二、安装步骤

- **克隆本仓库**：

  ```bash
  git clone 
  
  https://github.com/Catherineeeelll/Patient-Health-Management-System
  ```

- **进入项目目录**：

  ```bash
  cd health-system
  ```

### 三、安装依赖

- 本系统主要使用 Python 标准库，无需额外安装第三方库。

### 四、运行程序

- **运行主程序**：

  ```bash
  python main.py
  ```



## 系统结构

```perl
health-system/
│
├── main.py              # 主程序入口，启动系统并提供交互式菜单
├── models/              # 存放数据模型
│   ├── __init__.py      #空文件
│   └── patient.py       # 定义患者类（Patient）
├── utils/               # 存放工具类
│   ├── __init__.py      #空文件
│   ├── data_manager.py  # 数据管理类，负责文件的读取与写入
│   └── health_analyzer.py  # 健康报告生成器
├── data/                # 存储患者数据的文件夹
│   └── patient_records.txt  # 存储患者信息的文本文件
└── README.md            # 项目的文档
```

### 主要模块

- **main.py**：程序的入口，负责启动系统并显示菜单。

- **models/patient.py**：定义了患者类（Patient），该类包括患者的各项健康数据和一个 `to_string` 方法用于输出患者信息。

- **utils/data_manager.py**：负责与患者数据文件的交互，包括加载、保存、添加、更新和删除患者信息。

- **utils/health_analyzer.py**：基于患者的健康数据生成健康报告。

  

#### 1.main.py

- `__init__(self)`: 初始化方法，创建 `HealthSystem` 实例，负责调用其他模块

- `input_patient_data(self)`: 交互式地输入患者数据并返回患者对象。 

- `display_patients(self)`: 显示患者列表，遍历所有患者对象并输出信息。 

- `update_patient(self)`: 允许用户更新患者信息。用户可以选择更新某个特定字段或更新所有信息。 

- `run(self)`: 系统主循环，提供用户操作菜单并根据用户输入调用相应功能（如查看患者、添加患者、更新患者等）。

  ##### 测试脚本：

  ```python
  # main_test.py
  from main import HealthSystem
  
  if __name__ == "__main__":
      system = HealthSystem()
      system.run()
  ```

  

#### 2.models/patient.py

- `__init__(self, patient_id, name, age, gender, height, weight, `

- `blood_pressure, blood_sugar, cholesterol, check_date)`: 初始化患者对象，接受并保存患者的所有基本信息。

- `__str__(self)`: 定义 `Patient` 对象的字符串输出格式，用于打印患者信息。 

- `to_string(self)`: 返回患者数据的字符串形式，用于写入到文件中。

  ##### 测试脚本：

  ```python
  # patient_test.py
  from models.patient import Patient
  
  if __name__ == "__main__":
      # 创建一个患者实例
      patient = Patient("P101", "Jway", 19, "M", 190.0, 70.0, "120/80", 6.0, 6.0, "2024-02-01")
      
      # 打印患者信息
      print(patient)
      # 输出：P101, Jway, 19, M, 190.0, 70.0, 120/80, 6.0, 6.0, 2024-02-01
  
  ```

  

#### 3.data/patient_records.txt

- `patient_records.txt` 是系统的患者数据存储文件，所有的患者信息都保存在这个文件中。该文件存储了所有患者的基本信息和健康数据。

  ##### 示例患者记录

  ```yaml
  P100    骆芳   39  F   153.0   45.0    123/81  5.3  4.0  2024-04-23
  ```



#### 4.utils/data_manager.py

- `__init__(self, file_path)`: 初始化方法，检查患者数据文件是否存在。如果文件不存在，则创建空文件。 

- `load_data(self)`: 从患者数据文件中加载所有患者数据，并返回一个 `Patient` 对象列表。

- `save_data(self, patients)`: 将修改后的患者数据保存回文件。

- `get_patient(self, patient_id)`: 根据患者 ID 获取患者信息。

- `add_patient(self, patient)`: 向文件中添加新的患者数据。

- `update_patient(self, updated_patient)`: 更新患者信息，并将更新后的数据保存到文件。

- `delete_patient(self, patient_id)`: 删除指定患者信息，并保存更新后的数据。

  ##### 测试脚本：

  ```python
  # data_manager_test.py
  from utils.data_manager import DataManager
  from models.patient import Patient
  
  if __name__ == "__main__":
      # 创建数据管理对象并加载数据
      data_manager = DataManager('data/patient_records.txt')
      
      # 加载患者数据
      patients = data_manager.load_data()
      print(f"Loaded patients: {patients}")
      
      # 创建并添加新患者
      new_patient = Patient("P103", "Catherine", 19, "F", 172.0, 50.0, "120/80", 6.0, 6.0, "2024-12-01")
      data_manager.add_patient(new_patient)
      print(f"Added patient: {new_patient}")
      
      # 更新患者数据
      new_patient.age = 20
      data_manager.update_patient(new_patient)
      print(f"Updated patient: {new_patient}")
      
      # 删除患者
      data_manager.delete_patient("P103")
      print("Patient P103 deleted.")
  
  ```

  

#### 5.utils/health_analyzer.py

- `generate_health_report(self, patient)`: 生成健康报告，根据患者的健康数据（如血糖、血压、胆固醇）进行分析，并生成相应的健康报告。

  ##### 测试脚本：

  ```python
  # health_analyzer_test.py
  from utils.health_analyzer import HealthAnalyzer
  from models.patient import Patient
  
  if __name__ == "__main__":
      # 创建健康分析器实例
      analyzer = HealthAnalyzer()
      
      # 创建一个患者实例
      patient = Patient("P101", "Jway", 19, "M", 190.0, 70.0, "120/80", 6.0, 6.0, "2024-02-01")
      
      # 生成健康报告
      report = analyzer.generate_health_report(patient)
      print(report)
  
  ```

  ## 执行说明

  1. **运行系统主程序**：
     运行 `main_test.py` 脚本启动系统主控制程序，您可以通过命令行交互方式查看、添加、更新或删除患者信息。

     ```bash
     python main_test.py
     ```

  2. **测试患者数据模型**：
     运行 `patient_test.py` 验证患者数据模型的创建和字符串输出功能。

     ```bash
     python patient_test.py
     ```

  3. **测试数据管理功能**：
     运行 `data_manager_test.py` 测试数据加载、添加、更新和删除患者功能。

     ```bash
     python data_manager_test.py
     ```

  4. **生成健康报告**：
     运行 `health_analyzer_test.py` 生成并输出患者的健康报告。

     ```bash
     python health_analyzer_test.py
     ```



## 使用示例

1. **启动程序**： 启动程序后，系统会展示一个菜单，让用户选择不同的操作。

2. **查看患者信息**： 选择 `1` 来查看当前所有的患者记录。系统会列出每个患者的详细信息。

3. **添加患者**： 选择 `2` 来添加新的患者。系统会提示用户逐项输入患者信息，并验证输入的有效性。

4. **更新患者信息**： 选择 `3` 来更新患者的某项信息。用户可以选择修改姓名、年龄、血压等字段，也可以选择更新全部信息。

5. **删除患者**： 选择 `4` 来删除指定患者。系统会检查输入的患者 ID 是否存在，如果不存在则返回错误提示。

6. **生成健康报告**： 选择 `5` 来生成指定患者的健康报告，报告包括血糖、血压、胆固醇等数据分析。

7. **退出程序**： 选择 `6` 来退出系统。

   

## 注意事项

1. **数据格式**：确保患者信息按规定格式输入，否则系统可能无法正确解析数据。
2. **唯一性检查**：系统会检查患者 ID 是否唯一，避免重复的患者记录。
3. **文件路径**：`patient_records.txt` 存储患者信息的文件路径，系统启动时会检查该文件是否存在。



## 结语

欢迎提出问题或提交改进建议。感谢您的参与！
