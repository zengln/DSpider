# -*- coding: utf-8 -*-


from .mysql import mySql
from DScrapy.items import DscrapyItem


class DscrapyPipeline(object):

    def process_item(self, item, spider):

        if isinstance(item, DscrapyItem):
            number = item['number']
            result = mySql.isexists(number)
            if result[0] == 1:
                print('该小说记录已存在')
                pass
            else:
                mySql.insert(item['name'], item['author'], item['novelurl'], item['status'], item['novelNumber'],
                             item['category'], item['number'], item['collect'], item['click'],
                             item['push'], item['lastUpTime'])

