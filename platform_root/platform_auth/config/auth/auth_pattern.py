# Copyright 2019 NEC Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

AUTH_PATTERN = [
    {
        "url": r"^/api/(?P<org_id>[^/][^/]*)/platform/workspaces/?$",
        "auth": [
            {
                "method": ["POST"],
                "roles": [
                    {"client": "{org_id}-workspaces", "role": "_org-manager"}
                ]
            }
        ]
    },
    {
        "url": r"^/api/(?P<org_id>[^/][^/]*)/workspaces/(?P<ws_id>[^/][^/]*)($|/.*$)",
        "auth": [
            {
                "method": ["*"],
                "roles": [
                    {"client": "{org_id}-workspaces", "role": "{ws_id}"}
                ]
            }
        ]
    },
    {
        "url": r"^/api/(?P<org_id>[^/][^/]*)/platform/workspaces/(?P<ws_id>[^/][^/]*)($|/.*$)",
        "auth": [
            {
                "method": ["*"],
                "roles": [
                    {"client": "{org_id}-workspaces", "role": "{ws_id}"}
                ]
            }
        ]
    }
]
