import web
import psycopg2

render = web.template.render('templates/')

conn = psycopg2.connect(database="hacknj", user="postgres", password="secret")

urls = (
    '/(.*)', 'hacknj'
)
app = web.application(urls, globals())

class hello:
    def GET(self):
        return render.index

if __name__ == "__main__":
    app.run()