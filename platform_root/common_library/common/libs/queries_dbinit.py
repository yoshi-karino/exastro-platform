#   Copyright 2022 NEC Corporation
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

SQL_CREATE_ORGANIZATION_PRIVATE = """
CREATE TABLE T_ORGANIZATION_PRIVATE
(
    ID INT NOT NULL,
    INFORMATIONS JSON NOT NULL,
    CREATE_TIMESTAMP DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CREATE_USER VARCHAR(40),
    LAST_UPDATE_TIMESTAMP DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    LAST_UPDATE_USER VARCHAR(40),
    PRIMARY KEY (ID)
)
"""

SQL_CREATE_WORKSPACE = """
CREATE TABLE T_WORKSPACE
(
    WORKSPACE_ID VARCHAR(36) NOT NULL,
    WORKSPACE_NAME VARCHAR(255) NOT NULL,
    INFORMATIONS JSON NOT NULL,
    CREATE_TIMESTAMP DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CREATE_USER VARCHAR(40),
    LAST_UPDATE_TIMESTAMP DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    LAST_UPDATE_USER VARCHAR(40),
    PRIMARY KEY (WORKSPACE_ID)
)
"""

SQL_INSERT_ORGANIZATION_DBINFO = """
INSERT INTO T_ORGANIZATION_DB (ORGANIZATION_ID, DB_HOST, DB_PORT, DB_DATABASE, DB_USER, DB_PASSWORD, CREATE_USER, LAST_UPDATE_USER)
VALUES (%(organization_id)s, %(db_host)s, %(db_port)s, %(db_database)s, %(db_user)s, %(db_password)s, %(create_user)s, %(last_update_user)s)
"""
