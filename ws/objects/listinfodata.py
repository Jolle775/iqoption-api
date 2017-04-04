"""Module for IQ Option Candles websocket object."""
import json

from collections import OrderedDict

from iqoptionapi.ws.objects.base import Base


class ListInfoData(Base):
    def __init__(self):
        super(ListInfoData, self).__init__()
        self.__name = "listInfoData"
        self.__listinfodata_list = []

    @property
    def listinfodata_list(self):
        """Property to get listinfodata list.

        :returns: The list of listinfodata.
        """
        return self.__listinfodata_list

    @listinfodata_list.setter
    def listinfodata_list(self, listinfodata_list):
        """Method to set listinfodata list."""
        self.__listinfodata_list = listinfodata_list

    def get_listinfodata(self, listinfodata):
        """Method to get iteminfodata item.

         :returns: The object of listinfodata.
         """
        try:
            return self.listinfodata_list[listinfodata]
        except IndexError:
            return default

    def add_listinfodata(self, new_listinfodata):
        """Method to add listinfodata."""
        if new_listinfodata is not None:
            self.listinfodata_list.append(new_listinfodata)