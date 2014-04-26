#  Copyright (c) 2010 Wandy Ying
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from DatabaseLibrary import DatabaseLibrary

class Extend_Query(DatabaseLibrary):
    """docstring for Extend_Query"""
    def __init__(self):
        super(Extend_Query, self).__init__()
        #self.arg = arg

    def get_columns(self, selectStatement):
        """
        Uses the input `selectStatement` to query a table in the db which
        will be used to determine the description.
                
        For example, given we have a table `person` with the following data:
        | id | first_name  | last_name |
        |  1 | Wandy | Ying       |
        
        When you do the following:
        | @{queryResults} | Get Columns | select * from person |
        | Log Many | @{queryResults} |
        
        You will get the following:
        ['tase', 'ss', 'bb']
        """
        columns = []
        for columns_description in self.description(selectStatement):
            columns.append(columns_description[0])
        return columns


if __name__ == '__main__':
    a = Extend_Query()
    a.connect_to_database_using_custom_params("sqlite3","'../../db/BWDB.db'")
    print a.get_columns("select * from tableTest")
    a.disconnect_from_database()