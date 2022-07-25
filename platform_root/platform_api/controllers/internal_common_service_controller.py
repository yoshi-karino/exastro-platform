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

from flask import jsonify
from datetime import datetime

from common_library.common import common


@common.platform_exception_handler
def alive():
    """死活監視

    Returns:
        Response: HTTP Respose
    """
    ret_status = 200
    return jsonify({"result": ret_status, "time": str(datetime.utcnow())}), ret_status
