# -*- coding:utf-8 -*-

import pymysql

MYSQL_HOSTS = 'ip地址'
MYSQL_USER = '用户名'
MYSQL_PASSWORD = '密码'
MYSQL_PORT = '端口(默认为3306)'
MYSQL_DB = '你的数据库名'

mysql_db = pymysql.connect(host=MYSQL_HOSTS, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB, charset='utf8')

# 获取操作游标
cursor = mysql_db.cursor()
class mySql:

    @classmethod
    def insert(cls, name, author, novelurl, status, number, category, novelid, collect, click, push, lastupdate):
        insert_sql = ('INSERT INTO novel_d '
                        '(`name`,`author`,`novelurl`,`status`,`number`,`category`,`novelid`,`collect`,`click`,`push`,`lastupdate`)'
                        ' VALUES (%(name)s,%(author)s,%(novelurl)s,%(status)s,%(number)s,%(category)s,%(novelid)s,%(collect)s,%(click)s,%(push)s,%(lastupdate)s)'
                      )

        value = {
            'name': name,
            'author': author,
            'novelurl': novelurl,
            'status': status,
            'number': number,
            'category': category,
            'novelid': novelid,
            'collect': collect,
            'click': click,
            'push': push,
            'lastupdate': lastupdate
        }

        cursor.execute(insert_sql, value)
        mysql_db.commit()

    @classmethod
    def isexists(cls, novelid):
        exists_sql = 'SELECT EXISTS(SELECT 1 FROM novel_d WHERE novelid=%(novelid)s)'
        value = {
            'novelid': novelid
        }
        cursor.execute(exists_sql, value)
        return cursor.fetchall()[0]
