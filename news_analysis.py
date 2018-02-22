import psycopg2


def connect():
        return psycopg2.connect("dbname=news")


'''query to implment the first question'''
query1 = (
          "select articles.title, count(*) as num "
          "from articles, log "
          "where log.path like concat ('%', articles.slug, '%') "
          "group by articles.title, log.path "
          "order by num desc "
          "limit 3")
'''query to implment the second question'''
query2 = (
          "select authors.name, count(*) as num "
          "from articles, authors, log "
          "where articles.author = authors.id "
          "and log.path like concat ('%', articles.slug, '%') "
          "group by authors.name "
          "order by num desc ")
'''query to implment the third question'''
query3 = (
          "select * from "
          "(select to_char(time,'YYYY-MM-DD') as day, "
          "round(100.0*sum "
          "(case when status!='200 OK' then 1 else 0 end)/count(*),2) "
          "as error_percent "
          "from log "
          "group by day) as error "
          "where error_percent>1")


def articles(query1):
        '''Get the results for the most popular three articles of all time'''
        db = connect()
        cursor = db.cursor()
        cursor.execute(query1)
        results = cursor.fetchall()
        for row in results:
                title = row[0]
                num = row[1]
                print("%s - %d views" % (title, num))
        db.close()


def authors(query2):
        '''Get the results for the most popular article authors of all time'''
        db = connect()
        cursor = db.cursor()
        cursor.execute(query2)
        results = cursor.fetchall()
        for row in results:
                name = row[0]
                num = row[1]
                print("%s - %d views" % (name, num))
        db.close()


def error(query3):
        '''Days with more than 1% of requests lead to errors'''
        db = connect()
        cursor = db.cursor()
        cursor.execute(query3)
        results = cursor.fetchall()
        for row in results:
                day = row[0]
                error_percent = row[1]
                print("%s - %.2f%%" % (day, error_percent))
        db.close()


if __name__ == "__main__":
        print "What are the most popular three articles of all time?\n"
        articles(query1)
        print "\n"
        print "Who are the most popular article authors of all time?\n"
        authors(query2)
        print "\n"
        print "On which days did more than 1% of requests lead to errors?\n"
        error(query3)
        print "\n"
