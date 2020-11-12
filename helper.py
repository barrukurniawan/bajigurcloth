from flask import request
import re

class Helper():

    def pagination(total, paginate, limit, page):

      current_page = re.sub('&page=|&page=\\d+', '', request.url)

      if '?' not in current_page:
          current_page = current_page + '?'

      prev_page_num = paginate.prev_num
      if prev_page_num is None:
          prev_page_num = 1
      next_page_num = paginate.next_num
      if next_page_num is None:
          next_page_num = 1

      return {
          'total_rows': total,
          'rows_per_page': limit,
          'current_page': request.url,
          'total_page': paginate.pages,
          'prev_page_num': prev_page_num,
          'next_page_num': next_page_num
      }

class Formatter(object):

    def __init__(self, template, data, **kwargs):
        self.__template__ = template
        self.items = data

        if "includes" in kwargs:
            self.result = self.formatter(includes=kwargs["includes"])
        else:
            self.result = self.formatter()

    def formatter(self, includes=None, filter=None, request=None):

      try:
          iter(self.items)
      except TypeError:
          data = list()

          if includes is None:
              data.append(self.__template__(item=self.items))
          else:
              data.append(self.__template__(item=self.items, includes=includes))

          return data

      data = []
      for item in self.items:
          if includes is None:
              data.append(self.__template__(item=item))
          else:
              data.append(self.__template__(item=item, includes=includes))

      return data