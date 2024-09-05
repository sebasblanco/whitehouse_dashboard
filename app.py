import hud, sys

app = hud.QApplication(sys.argv)
dashboard = hud.HUDDashboard()
timeline = hud.Timeline()

dashboard.show()
sys.exit(app.exec_())