# Copyright 2018-  René Rohner
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class ReaderConfig:

    TEST_CASE_TABLE_NAME = '*** Test Cases ***'

    def __init__(self,
                 file=None,
                 encoding=None,
                 dialect=None,
                 delimiter=None,
                 quotechar=None,
                 escapechar=None,
                 doublequote=None,
                 skipinitialspace=None,
                 lineterminator=None,
                 sheet_name=None,
                 ):

        self.ROBOT_LIBRARY_LISTENER = self

        self.file = file
        self.encoding = encoding
        self.dialect = dialect
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.escapechar = escapechar
        self.doublequote = doublequote
        self.skipinitialspace = skipinitialspace
        self.lineterminator = lineterminator
        self.sheet_name = sheet_name


class TestCaseData:

    def __init__(self,
                 test_case_name='',
                 arguments=None,
                 tags=None,
                 documentation=''
                 ):

        self.test_case_name = test_case_name
        self.arguments = arguments if arguments else {}
        self.tags = tags if tags else []
        self.documentation = documentation