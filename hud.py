from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QGridLayout
from PyQt5.QtCore import QTimer
from datetime import datetime

class Event:
    def __init__(self, date: datetime, title: str, description: str):
        self.date = date          # DateTime object representing the event date
        self.title = title        # Title of the event
        self.description = description  # Description of the event

class Article:
    def __init__(self, thumbnail: str, url: str):
        self.thumbnail = thumbnail  # URL of the article thumbnail
        self.url = url              # URL of the article

class Timeline:
    def __init__(self):
        self.events = []           # List to hold Event objects

    def add_event(self, event: Event):
        self.events.append(event)  # Method to add an event to the timeline

class DateTime:
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int):
        self.year = year           # Year of the event
        self.month = month         # Month of the event
        self.day = day             # Day of the event
        self.hour = hour           # Hour of the event
        self.minute = minute       # Minute of the event
        self.second = second       # Second of the event

class HUDDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('WHITEHOUSE')
        self.setGeometry(0, 0, 1920, 1080)
        self.setStyleSheet("background-color: black; border: 1px solid white")
        self.timeline = Timeline()
        grid_layout = QGridLayout()

    # Create left sidebar
        # Date
        self.date_time_label = QLabel('Date and Time')
        self.date_time_label.setStyleSheet("color: white; font-size: 18px; border: 1px solid #008080;")
        grid_layout.addWidget(self.date_time_label, 1, 0)

        # Upcoming Events
        self.upcoming_events_label = QLabel('Upcoming Events')
        self.upcoming_events_label.setStyleSheet("color: white; font-size: 18px; border: 1px solid #008080;")
        grid_layout.addWidget(self.upcoming_events_label, 2, 0)

        # Radio
        self.radio_label = QLabel('Radio')
        self.radio_label.setStyleSheet("color: white; font-size: 18px; border: 1px solid #008080;")
        grid_layout.addWidget(self.radio_label, 3, 0)

    # Create right sidebar
        # Headlines
        self.headline1_label = QLabel('Headline 1')
        grid_layout.addWidget(self.headline1_label, 1, 1)
        self.headline2_label = QLabel('Headline 2')
        grid_layout.addWidget(self.headline2_label, 1, 2)
        self.headline3_label = QLabel('Headline 3')
        grid_layout.addWidget(self.headline3_label, 2, 1)
        self.headline4_label = QLabel('Headline 4')
        grid_layout.addWidget(self.headline4_label, 2, 2)
        for i, headline_label in (enumerate([self.headline1_label, self.headline2_label, self.headline3_label, self.headline4_label])):
            headline_label.setStyleSheet("color: white; font-size: 16px; border: 1px solid #008080;")  # Arrange in 2x2 grid
        
        # Videos
        self.videos_label = QLabel('Videos / Highlights')
        self.videos_label.setStyleSheet("color: white; font-size: 18px; border: 1px solid #008080;")
        grid_layout.addWidget(self.videos_label, 3, 1, 1, 2)  # Span 1 row, 2 columns

        self.display_events(grid_layout)
        self.setLayout(grid_layout)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000)  # update every 1000ms (1 second)

    def display_events(self, layout):
        for i, event in enumerate(self.timeline.events):
            event_label = QLabel(f"{event.date.year}-{event.date.month:02d}-{event.date.day:02d} {event.title}: {event.description}")
            event_label.setStyleSheet("color: white; font-size: 16px; border: 1px solid #008080;")
            layout.addWidget(event_label, 2 + i, 0)  # Place events below the upcoming events label

    def updateDateTime(self):
        current_time = "Current Date and Time: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.date_time_label.setText(current_time)