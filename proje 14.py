import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget, QInputDialog, QMessageBox, QProgressBar, QComboBox, QDialog, QDateEdit

class Project:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

class Task:
    def __init__(self, name, responsible):
        self.name = name
        self.responsible = responsible
        self.progress = 0

class Employee:
    def __init__(self, name):
        self.name = name
        self.tasks = []

class ProjectManagementSystem:
    def __init__(self):
        self.projects = []

    def add_project(self, name, start_date, end_date):
        project = Project(name, start_date, end_date)
        self.projects.append(project)

    def add_task_to_project(self, project_index, task_name, responsible, progress):
        task = Task(task_name, responsible)
        task.progress = progress
        project = self.projects[project_index]
        project.add_task(task)

    def update_task_progress(self, project_index, task_index, progress):
        project = self.projects[project_index]
        task = project.tasks[task_index]
        task.progress = progress

class ProjectManagementApp(QWidget):
    def __init__(self):
        super().__init__()

        self.pms = ProjectManagementSystem()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label_welcome = QLabel("İş Takip ve Yönetim Sistemi")
        layout.addWidget(self.label_welcome)

        self.button_add_project = QPushButton("Proje Ekle")
        self.button_add_project.clicked.connect(self.show_add_project_dialog)
        layout.addWidget(self.button_add_project)

        self.list_widget_projects = QListWidget()
        self.list_widget_projects.itemClicked.connect(self.update_tasks_list)
        layout.addWidget(self.list_widget_projects)

        self.label_tasks = QLabel("Görevler:")
        layout.addWidget(self.label_tasks)

        self.list_widget_tasks = QListWidget()
        layout.addWidget(self.list_widget_tasks)

        self.label_progress = QLabel("İlerleme Durumu:")
        layout.addWidget(self.label_progress)

        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        self.label_progress_level = QLabel("İlerleme Durumu (Kademeli):")
        layout.addWidget(self.label_progress_level)

        self.combo_progress_level = QComboBox()
        self.combo_progress_level.addItems(["%0", "%25", "%50", "%75", "%100"])
        layout.addWidget(self.combo_progress_level)

        self.button_add_task = QPushButton("Görev Ekle")
        self.button_add_task.clicked.connect(self.show_add_task_dialog)
        layout.addWidget(self.button_add_task)

        self.button_save_progress = QPushButton("İlerlemeyi Kaydet")
        self.button_save_progress.clicked.connect(self.save_progress)
        layout.addWidget(self.button_save_progress)

        self.setLayout(layout)
        self.setWindowTitle("İş Takip ve Yönetim Sistemi")

    def show_add_project_dialog(self):
        name, ok = QInputDialog.getText(self, "Proje Ekle", "Proje Adı:")
        if ok:
            start_date = QDateEdit()
            end_date = QDateEdit()
            start_date.setCalendarPopup(True)
            end_date.setCalendarPopup(True)
            layout = QVBoxLayout()
            layout.addWidget(QLabel("Başlangıç Tarihi:"))
            layout.addWidget(start_date)
            layout.addWidget(QLabel("Bitiş Tarihi:"))
            layout.addWidget(end_date)
            dialog = QDialog()
            dialog.setLayout(layout)
            dialog.setWindowTitle("Proje Tarihlerini Seç")
            button_save = QPushButton("Kaydet")
            button_save.clicked.connect(lambda: self.save_project(name, start_date.date().toString("dd/MM/yyyy"), end_date.date().toString("dd/MM/yyyy")))
            layout.addWidget(button_save)
            dialog.exec_()

    def save_project(self, name, start_date, end_date):
        self.pms.add_project(name, start_date, end_date)
        self.update_projects_list()

    def show_add_task_dialog(self):
        project_index = self.list_widget_projects.currentRow()
        if project_index != -1:
            task_name, ok = QInputDialog.getText(self, "Görev Ekle", "Görev Adı:")
            if ok:
                responsible, ok = QInputDialog.getText(self, "Görev Ekle", "Sorumlu Kişi:")
                if ok:
                    progress_level_index = self.combo_progress_level.currentIndex()
                    progress_levels = [0, 25, 50, 75, 100]
                    progress = progress_levels[progress_level_index]
                    self.pms.add_task_to_project(project_index, task_name, responsible, progress)
                    QMessageBox.information(self, "Başarı", "Görev '{}' eklendi.".format(task_name))
                    self.update_tasks_list()
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir proje seçin.")

    def save_progress(self):
        project_index = self.list_widget_projects.currentRow()
        task_index = self.list_widget_tasks.currentRow()
        progress_level_index = self.combo_progress_level.currentIndex()
        progress_levels = [0, 25, 50, 75, 100]
        progress = progress_levels[progress_level_index]
        self.pms.update_task_progress(project_index, task_index, progress)
        QMessageBox.information(self, "Başarı", "İlerleme durumu kaydedildi.")
        self.update_tasks_list()

    def update_projects_list(self):
        self.list_widget_projects.clear()
        for project in self.pms.projects:
            self.list_widget_projects.addItem(project.name)

    def update_tasks_list(self):
        project_index = self.list_widget_projects.currentRow()
        if project_index != -1:
            project = self.pms.projects[project_index]
            self.list_widget_tasks.clear()
            for task in project.tasks:
                self.list_widget_tasks.addItem("{} - Sorumlu: {} - İlerleme: {}%".format(task.name, task.responsible, task.progress))
                self.progress_bar.setValue(task.progress)
        else:
            self.list_widget_tasks.clear()
            self.progress_bar.setValue(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    project_management_app = ProjectManagementApp()
    project_management_app.show()
    sys.exit(app.exec_())
