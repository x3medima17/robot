import tornado.web          # the Tornado web framework
import tornado.httpserver   # the Tornado web server
import tornado.ioloop       # the Tornado event-loop

# handles incoming request, this is the C part in MVC
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # renders the Tornado template
        self.render('index.html')

# prepares the application
app = tornado.web.Application([
        (r"/", MainHandler),
    ], debug=True, template_path='templates')

if __name__ == '__main__':
    # prepares the web server
    srv = tornado.httpserver.HTTPServer(app, xheaders=True)

    # listens incoming request on port 8000
    srv.bind(8000, '')

    # starts the server using 1 process
    # unless you know what you're doing, always set to 1
    srv.start(1)

    # runs all the things
    tornado.ioloop.IOLoop.instance().start()