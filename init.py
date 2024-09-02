import hud
import sys
import datetime

app = hud.QApplication(sys.argv)
dashboard = hud.HUDDashboard()
timeline = hud.Timeline()

event_date = hud.DateTime(2024, 11, 4, 24, 0, 0)
event = hud.Event(event_date, "Sample Event", "This is a sample event description.")
timeline.add_event(event)

dashboard.show()
sys.exit(app.exec_())