import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver

from subprocess import Popen,PIPE
import robot as rb

from tornado.options import define, options

define("port", default = 9090,help="sss", type = int)

robot = rb.Robot()

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/",MainHandler),
			(r"/photo",PhotoHandler),
			(r"/robot",RobotHandler)
		]
		settings = dict(
			debug = True,
			template_path = "templates",
			static_path = "static"
			)
		tornado.web.Application.__init__(self,handlers,**settings)

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")

class PhotoHandler(tornado.web.RequestHandler):
	def get(self):
		cmd = "raspistill -w 1366 -h 768 -rot 180 -t 3	 -o static/qr.jpg".split(" ")
		process = Popen(cmd, stdout = PIPE, stderr=PIPE)
		out,err = process.communicate()
		self.render("index.html")

class RobotHandler(tornado.web.RequestHandler):
	def post(self):
		action = self.get_argument("action",None)
		print action
		if action == "stop":
			robot.stop()
			return
		direction = self.get_argument("direction",None)
		print direction
		robot.set_move(direction)

if __name__ == "__main__":
	tornado.options.parse_command_line()
	app = Application()
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)

	tornado.ioloop.IOLoop.instance().start()